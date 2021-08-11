import cv2
import numpy as np
from djitellopy import tello
import time

edu = tello.Tello()
edu.connect()

print(edu.get_battery())

edu.streamon()

edu.takeoff()
edu.send_rc_control(0, 0, 22, 0)
time.sleep(2.5)

w, h = 352, 288
fbRange = [8200, 8800]
pid = [0.4, 0.4, 0]
pError = 0


def findBody(img):
    bodyCascade = cv2.CascadeClassifier("Resources/haarcascade_fullbody.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bodys = bodyCascade.detectMultiScale(imgGray, 1.05, 3)
    myBodyListC = []
    myBodyListArea = []
    for (x, y, w, h) in bodys:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        myBodyListC.append([cx, cy])
        myBodyListArea.append(area)
    if len(myBodyListArea) != 0:
        i = myBodyListArea.index(max(myBodyListArea))
        return img, [myBodyListC[i], myBodyListArea[i]]
    else:
        return img, [[0, 0], 0]


def trackBody(edu, info, w, pid, pError):
    area = info[1]
    x, y = info[0]
    fb = 0
    error = x - w // 2
    speed = pid[0] * error + pid[1] * (error - pError)
    speed = int(np.clip(speed, -100, 100))

    if area > fbRange[0] and area < fbRange[1]:
        fb = 0
    elif area > fbRange[1]:
        fb = -20
    elif area < fbRange[0] and area != 0:
        fb = 20

    if x == 0:
        speed = 0
        error = 0
    edu.send_rc_control(0, fb, 0, speed)
    return error


while True:
    img = edu.get_frame_read().frame
    img = cv2.resize(img, (w, h))
    img, info = findBody(img)
    pError = trackBody(edu, info, w, pid, pError)
    cv2.imshow("Tello_Body_Cam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        edu.land()
        break

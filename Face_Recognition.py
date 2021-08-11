import numpy as np
import face_recognition as fr
import cv2
import os

video_capture = cv2.VideoCapture(0)

image_face1 = fr.load_image_file('Faces/face1.jpeg')
face_encoding_face1 = fr.face_encodings(image_face1, None, 10, 'small')[0]

image_face2 = fr.load_image_file('Faces/face2.jpg')
face_encoding_face2 = fr.face_encodings(image_face2, None, 10, 'small')[0]

image_face3 = fr.load_image_file('Faces/face3.jpg')
face_encoding_face3 = fr.face_encodings(image_face3, None, 30, 'small')[0]

image_face4 = fr.load_image_file('Faces/face4.jpeg')
face_encoding_face4 = fr.face_encodings(image_face4, None, 30, 'small')[0]

known_face_encodings = [face_encoding_face1, face_encoding_face2, face_encoding_face3, face_encoding_face4]
known_face_names = ["face1","face2","face3","face4"]

while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]

    face_locations = fr.face_locations(rgb_frame)
    face_encodings = fr.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = fr.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = fr.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0,0,255), 2)
        cv2.rectangle(frame, (left, bottom-35), (right, bottom), (0,0,255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name, (left+6, bottom-6), font, 1.0, (255,255,255), 1)

    cv2.imshow('Face_Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
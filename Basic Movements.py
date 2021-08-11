import time
from djitellopy import tello
import cv2


x = 100                 # Enter the distance to be advanced in centimeters.
z = x // 25             # Time required to advance 1 meters.
y = 6                   # The time required for a 90 degree angle turn.



edu = tello.Tello()                     # I chose the name of the drone as "edu"
edu.connect()                           # Connect to Tello Drone
print(edu.get_battery())                # Battery charge rate
edu.takeoff()                           # Drone take off
edu.send_rc_control(0, 0, 22, 0)        # Move up 22 cm/s
time.sleep(2.5)                         # 2,5 sec delay

edu.send_rc_control(0, 25, 0, 0)        # Move forward 25 cm/s
time.sleep(z)                           # Delay of z seconds

edu.send_rc_control(0,0,0,0)            # Wait
time.sleep(1)                           # 1 sec delay

edu.send_rc_control(0, 0, 0, 25)        # Turn clockwise 25 cm/s
time.sleep(y)                           # Delay of y seconds

edu.send_rc_control(0,0,0,0)            # Wait
time.sleep(1)                           # 1 sec delay

edu.send_rc_control(0, 25, 0, 0)        # Move forward 25 cm/s
time.sleep(z)                           # Delay of z seconds

edu.send_rc_control(0,0,0,0)            # Wait
time.sleep(1)                           # 1 sec delay

edu.send_rc_control(0, 0, 0, 25)        # Turn clockwise 25 cm/s
time.sleep(y)                           # Delay of y seconds

edu.send_rc_control(0,0,0,0)            # Wait
time.sleep(1)                           # 1 sec delay

edu.send_rc_control(0, 25, 0, 0)        # Move forward 25 cm/s
time.sleep(z)                           # Delay of z seconds

edu.send_rc_control(0,0,0,0)            # Wait
time.sleep(1)                           # 1 sec delay

edu.send_rc_control(0, 0, 0, 25)        # Turn clockwise 25 cm/s
time.sleep(y)                           # Delay of y seconds

edu.send_rc_control(0,0,0,0)            # Wait
time.sleep(1)                           # 1 sec delay

edu.send_rc_control(0, 25, 0, 0)        # Move forward 25 cm/s
time.sleep(z)                           # Delay of z seconds

edu.send_rc_control(0,0,0,0)            # Wait
time.sleep(1)                           # 1 sec delay

edu.send_rc_control(0, 0, 0, 25)        # Turn clockwise 25 cm/s
time.sleep(y)                           # Delay of y seconds

edu.send_rc_control(0,0,0,0)            # Wait
time.sleep(1)                           # 1 sec delay

edu.land()                              # Drone landing

if cv2.waitKey(1) & 0xFF == ord('q'):  # Press and hold Q key for 1 second to land the drone in emergency
    edu.land()
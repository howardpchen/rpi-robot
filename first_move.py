import gpiozero
import time

robot = gpiozero.Robot(right=(17,18), left=(27,22))
for i in range(2):
    robot.forward()
    time.sleep(0.5)
    robot.left()
    time.sleep(0.25)

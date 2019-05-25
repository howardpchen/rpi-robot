import gpiozero
import cwiid

robot = gpiozero.Robot(right=(17,18), left=(27,22))

print("Press 1+2 button together")
wii = cwiid.Wiimote()

print("Connection established")
wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
xmax = 0
ymax = 0

while(True):
    x = (wii.state['acc'][cwiid.X] - 95) - 25
    y = (wii.state['acc'][cwiid.Y] - 95) - 25

    x = min(25, max(-25, x))
    y = min(25, max(-25, y))

    forward_value = (float(x)/50)*2
    turn_value = (float(y)/50)*2

    if(turn_value < 0.3) and (turn_value > -0.3):
        robot.value = (forward_value, forward_value)
    else:
        robot.value = (-turn_value, turn_value)

    # print(forward_value, " ", turn_value)

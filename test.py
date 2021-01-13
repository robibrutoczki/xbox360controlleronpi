import math
import xbox
import time


def angleFromCoords(x, y):
    angle = 0.0
    if x == 0.0 and y == 0.0:
        angle = 90.0
    elif x >= 0.0 and y >= 0.0:
        # first quadrant
        angle = math.degrees(math.atan(y/x)) if x != 0.0 else 90.0
    elif x < 0.0 and y >= 0.0:
        # second quadrant
        angle = math.degrees(math.atan(y/x))
        angle += 180.0
    elif x < 0.0 and y < 0.0:
        # third quadrant
        angle = math.degrees(math.atan(y/x))
        angle += 180.0
    elif x >= 0.0 and y < 0.0:
        # third quadrant
        angle = math.degrees(math.atan(y/x)) if x != 0.0 else -90.0
        angle += 360.0
    return angle


joy = xbox.Joystick()

while not joy.Back():
    if joy.Start():
        print("Start")

    elif joy.A():
        print("a")
    elif joy.B():
        print("B")
    elif joy.X():
        print("X")
    elif joy.Y():
        print("Y")

# Dpad
    elif joy.dpadUp():
        print("dpadUp()")
    elif joy.dpadDown():
        print("dpadDown()")
    elif joy.dpadLeft():
        print("dpadLeft()")
    elif joy.dpadRight():
        print("dpadRight()")

# Triggers
   # bottom Triggers

    elif joy.rightTrigger():
        print("rightTrigger")
    elif joy.leftTrigger():
        print("leftTrigger")

    # top Triggers

    elif joy.leftBumper():
        print("leftBumper")
    elif joy.rightBumper():
        print("rightBumper")

# Thumbsticks

    elif joy.leftThumbstick():
        print("leftTumbstick")
    elif joy.rightThumbstick():
        print("rightTumbstick")

# Servo LEFT STICK :

    x, y = joy.leftStick()
    angle = angleFromCoords(x, y)
    print(angle)
    if angle > 180 and angle < 270:
        angle = 180

    elif angle >= 270:
        angle = 0

# Servo RIGHT STICK :
    x, y = joy.rightStick()
    angle = angleFromCoords(x, y)
    print(angle)
    if angle > 180 and angle < 270:
        angle = 180

    elif angle >= 270:
        angle = 0


joy.close()

Hello 

This is a simple file to use xbox 360 controller on Pi.

U need a Pi ,
Xbox MICROSOFT USB wireless receiver (other brands might not work),
Xbox360 wireless controller 

Install : sudo apt-get install xboxdrv

Clone this folder, u need both file in your project.

Use test.py as your template for a project,but xbox.py is a must.
U might run it as : sudo python test.py
 

Change print to some orders to controll your robot etc.

There is a math for the angles for thumbstick.

According to Xboxdrv it should work with :
(Note : I only tested it on Xbox360 wireless controller via the USB wireless receiver)

Xbox1 controller, both official and third party
Xbox360 USB controller
Xbox360 wireless controller via the USB wireless receiver
Xbox360 USB guitar and drum kit
Thrustmaster Dual Power 3 Gamepad
any joystick support by Linux via the evdev interface

Enjoy.

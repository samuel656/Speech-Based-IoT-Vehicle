Project Title: Voice-Driven Intelligence on Wheels: A Speech-Based Smart Vehicle Powered by IoT

Step 1: Create the python virtual environment in Raspberry Pi OS
python -m venv project

Step 2: Activate virtual environment
Source bin/activate

Step 3: Installing all the required libraries by using pip command
Libraries: tensorflow,librosa,jupyternotebook,numpy,pandas,gpiozero,GPIO
EX: pip intall tensorflow, etc

Step 4: configuring raspberry pi pins
COMPONENT	GPIO PIN

MOTOR	Right Forward=18, Right Backward=17
Left Forward=23, Left Backward=22
Ultrasonic Sensor	Echo=27, Trigger=24
LED	Front right=2, Front Left=3
Back right=19, Back Left=26
Sensor	21
Buzzer	10

Step 5: run python code “car1.py”
Python car1.py

Step 6: After running code give voice input like turn right, turn left, stop, reverse, lights on, lights off, go forward, blow horn, speed up, slow down

Step 7: Gesture control operations in key board
Go forward=	Up arrow key
Reverse=	Down arrow key
Stop=	Release the Key
Turn Left=	Left arrow key
Turn right=	Right arow key
Blow horn	= Key “b” or “B”
Lights on=	Key “l” or “L”
Lights off=	Release key
Speed up=	Key “u” or “U”
Slow down=	Key “d” or “B”

Step 8: press ctrl+c to stop executing the code

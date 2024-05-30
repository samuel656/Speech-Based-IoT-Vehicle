from gpiozero import Motor, DistanceSensor,Servo
from gpiozero import Buzzer
from gpiozero import LED
import curses


rightmotor = Motor(forward=18, backward=17)
leftmotor = Motor(forward=23, backward=22)

# Define ultrasonic sensor
sensor = DistanceSensor(echo=27, trigger=24)

#servo motor
servo_pin=21

fr=2
fl=3
br=19
bl=26
led1=LED(fr)
led2=LED(fl)
led3=LED(br)
led4=LED(bl)

b=10
buzzer=Buzzer(b)

def left():
    print('Left ...')
    rightmotor.forward()
    leftmotor.backward()
    led2.on()
    led4.on()
    led1.off()
    led3.off()

def right():
    print('Right ...')
    rightmotor.backward()
    leftmotor.forward()
    led1.on()
    led2.off()
    led3.on()
    led4.off()

def forward():
    print('Forwarding ...')
    leftmotor.forward()
    rightmotor.forward()
    led1.on()
    led2.on()
    led3.off()
    led4.off()
    
def reverse():
    print('Reversing ...')
    rightmotor.backward()
    leftmotor.backward()
    led3.on()
    led4.on()
    led1.off()
    led2.off()
    #buzzer.on()

def lightson():
    led1.on()
    led2.on()

def lightsoff():
    led1.off()
    led2.off()

def blowhorn():
    buzzer.on()
    
speed = 0.5

def speedup():
    global speed
    if speed < 1.0:
        speed += 0.1

def slowdown():
    global speed
    if speed > 0.1:
        speed -= 0.1

    
def stop():
    print('Stopping ...')
    leftmotor.stop()
    rightmotor.stop()
    led1.off()
    led2.off()
    led3.on()
    led4.on()

    
actions = {
    curses.KEY_UP: forward,
    curses.KEY_DOWN: reverse,
    curses.KEY_LEFT: left,
    curses.KEY_RIGHT: right,
    ord('L'): lightson,
    ord('B'): blowhorn,
    ord('U'): speedup,
    ord('D'): slowdown,
}

def main(window):
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            # KEY PRESSED
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY RELEASED
            stop()

curses.wrapper(main)
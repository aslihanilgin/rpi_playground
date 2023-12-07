# Author: https://www.hackster.io/rajeshjiet/led-blink-using-raspberry-pi-b38dbe#:~:text=LED%20Blinking%20using%20a%20Raspberry,off%20state%20using%20Python%20programming.

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

while True:
    print("in the loop")
    GPIO.output(18, GPIO.HIGH)
    sleep(1)
    GPIO.output(18, GPIO.LOW)
    sleep(1)

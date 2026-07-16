import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

UP = 25
DOWN = 12

GPIO.setup(UP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(UP) == 0:
        print("UP PRESSED")
        time.sleep(0.3)

    if GPIO.input(DOWN) == 0:
        print("DOWN PRESSED")
        time.sleep(0.3)

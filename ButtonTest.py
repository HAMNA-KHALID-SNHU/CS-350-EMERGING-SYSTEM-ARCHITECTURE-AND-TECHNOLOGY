import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

BUTTON = 24

GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(BUTTON) == 0:
            print("Button Pressed")
            time.sleep(0.3)
except KeyboardInterrupt:
    GPIO.cleanup()

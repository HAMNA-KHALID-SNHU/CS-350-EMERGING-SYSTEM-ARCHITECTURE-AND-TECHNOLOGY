import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

RED = 17
BLUE = 21

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

try:
    while True:
        GPIO.output(RED, True)
        GPIO.output(BLUE, False)
        time.sleep(1)

        GPIO.output(RED, False)
        GPIO.output(BLUE, True)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

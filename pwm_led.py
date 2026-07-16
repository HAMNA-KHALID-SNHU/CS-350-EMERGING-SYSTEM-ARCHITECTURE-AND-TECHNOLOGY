import RPi.GPIO as GPIO
import time

# Use Broadcom (BCM) pin numbering
GPIO.setmode(GPIO.BCM)

# Set GPIO18 as output pin
GPIO.setup(18, GPIO.OUT)

# Create PWM instance on GPIO18 at 100 Hz frequency
pwm = GPIO.PWM(18, 100)

# Start PWM with 0% duty cycle (LED off)
pwm.start(0)

try:
    while True:
        # Gradually increase brightness (fade in)
        for duty in range(0, 101, 5):
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.1)

        # Gradually decrease brightness (fade out)
        for duty in range(100, -1, -5):
            pwm.ChangeDutyCycle(duty)
            time.sleep(0.1)

# Handle program interruption (Ctrl+C)
except KeyboardInterrupt:
    print("Program stopped by user")

# Stop PWM and clean up GPIO settings
pwm.stop()
GPIO.cleanup()
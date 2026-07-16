import RPi.GPIO as GPIO
import time
from RPLCD.gpio import CharLCD

# -----------------------
# GPIO SETUP
# -----------------------
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# YOUR WORKING PINS (DO NOT CHANGE)
RED = 17      # Pin 11
BLUE = 21     # Pin 40
BUTTON = 24   # Pin 18

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# -----------------------
# LCD SETUP (SAFE PINS)
# -----------------------
lcd = CharLCD(
    cols=16,
    rows=2,
    pin_rs=22,
    pin_e=23,
    pins_data=[5, 6, 13, 26],
    numbering_mode=GPIO.BCM
)

# -----------------------
# TIMING
# -----------------------
DOT = 0.5
DASH = 1.5
GAP = 0.25
LETTER = 0.75
WORD = 3

# -----------------------
# STATE VARIABLES
# -----------------------
state = 0
next_state = 0

# -----------------------
# MORSE FUNCTIONS
# -----------------------
def dot():
    GPIO.output(RED, True)
    time.sleep(DOT)
    GPIO.output(RED, False)
    time.sleep(GAP)

def dash():
    GPIO.output(BLUE, True)
    time.sleep(DASH)
    GPIO.output(BLUE, False)
    time.sleep(GAP)

# -----------------------
# MESSAGE FUNCTIONS
# -----------------------
def message_hi():
    # H = ....
    for _ in range(4):
        dot()
    time.sleep(LETTER)

    # I = ..
    for _ in range(2):
        dot()
    time.sleep(WORD)

def message_ok():
    # O = ---
    for _ in range(3):
        dash()
    time.sleep(LETTER)

    # K = -.-
    dash()
    dot()
    dash()
    time.sleep(WORD)

# -----------------------
# MAIN LOOP
# -----------------------
try:
    while True:

        # BUTTON PRESS
        if GPIO.input(BUTTON) == 0:
            next_state = 1 - state
            print("State change requested")
            time.sleep(0.3)

        # LCD DISPLAY + MESSAGE
        if state == 0:
            lcd.clear()
            lcd.write_string("Message: HI")
            print("Displaying: HI")
            message_hi()
        else:
            lcd.clear()
            lcd.write_string("Message: OK")
            print("Displaying: OK")
            message_ok()

        # STATE SWITCH AFTER MESSAGE
        state = next_state

except KeyboardInterrupt:
    lcd.clear()
    GPIO.cleanup()

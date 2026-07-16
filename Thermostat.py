import time
import board
import adafruit_dht
import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD

# -----------------------
# GPIO SETUP
# -----------------------
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

RED = 17      # heating LED
BLUE = 21     # cooling LED

STATE_BTN = 24   # state toggle
UP_BTN = 25      # increase temp
DOWN_BTN = 12    # decrease temp

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

GPIO.setup(STATE_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(UP_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DOWN_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# -----------------------
# SENSOR SETUP
# -----------------------
dht = adafruit_dht.DHT22(board.D4)

# -----------------------
# LCD SETUP
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
# VARIABLES
# -----------------------
set_point = 72
state = 0  # 0=OFF, 1=HEAT, 2=COOL

last_uart = time.time()

# -----------------------
# FUNCTIONS
# -----------------------
def read_temp_f():
    temp_c = dht.temperature
    return (temp_c * 9/5) + 32

def get_state_name(s):
    if s == 0:
        return "OFF"
    elif s == 1:
        return "HEAT"
    else:
        return "COOL"

# -----------------------
# MAIN LOOP
# -----------------------
try:
    while True:
        try:
            temp = read_temp_f()

            print(f"Temp: {temp:.1f}F | Set: {set_point} | State: {get_state_name(state)}")

            # -----------------------
            # BUTTONS
            # -----------------------

            if GPIO.input(STATE_BTN) == 0:
                state = (state + 1) % 3
                print("State changed:", get_state_name(state))
                time.sleep(0.4)

            if GPIO.input(UP_BTN) == 0:
                set_point += 1
                print("Set temp increased:", set_point)
                time.sleep(0.3)

            if GPIO.input(DOWN_BTN) == 0:
                set_point -= 1
                print("Set temp decreased:", set_point)
                time.sleep(0.3)

            # -----------------------
            # STATE LOGIC
            # -----------------------

            if state == 0:  # OFF
                GPIO.output(RED, False)
                GPIO.output(BLUE, False)

            elif state == 1:  # HEAT
                if temp < set_point:
                    GPIO.output(RED, True)   # heating ON
                    GPIO.output(BLUE, False)
                else:
                    GPIO.output(RED, True)   # solid
                    GPIO.output(BLUE, False)

            elif state == 2:  # COOL
                if temp > set_point:
                    GPIO.output(BLUE, True)
                    GPIO.output(RED, False)
                else:
                    GPIO.output(BLUE, True)
                    GPIO.output(RED, False)

            # -----------------------
            # LCD DISPLAY
            # -----------------------

            lcd.clear()

            line1 = f"T:{temp:.1f}F S:{set_point}"
            line2 = f"Mode:{get_state_name(state)}"

            lcd.write_string(line1[:16])
            lcd.cursor_pos = (1, 0)
            lcd.write_string(line2[:16])

            # -----------------------
            # UART OUTPUT (EVERY 30 SEC)
            # -----------------------

            if time.time() - last_uart > 30:
                uart_data = f"{get_state_name(state)},{temp:.1f},{set_point}"
                print("UART:", uart_data)
                last_uart = time.time()

            time.sleep(2)

        except RuntimeError:
            print("Sensor read error")
            time.sleep(2)

except KeyboardInterrupt:
    lcd.clear()
    GPIO.cleanup()

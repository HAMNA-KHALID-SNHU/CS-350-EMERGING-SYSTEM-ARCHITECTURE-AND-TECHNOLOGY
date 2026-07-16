from RPLCD.gpio import CharLCD
from RPi import GPIO
import time

GPIO.setwarnings(False)

lcd = CharLCD(
    numbering_mode=GPIO.BOARD,
    cols=16,
    rows=2,
    pin_rs=15,
    pin_e=16,
    pins_data=[31, 29, 31, 37],
    auto_linebreaks=True
)

# IMPORTANT: give LCD time to stabilize
time.sleep(1)

lcd.clear()
time.sleep(0.5)

lcd.write_string("Hello Hamna!")
time.sleep(2)

lcd.clear()
time.sleep(0.5)

lcd.write_string("LCD Working :)")
time.sleep(5)

lcd.clear()
GPIO.cleanup()

from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

lcd = CharLCD(
    cols=16,
    rows=2,
    pin_rs=22,
    pin_e=23,
    pins_data=[5, 6, 13, 26],
    numbering_mode=GPIO.BCM
)

time.sleep(1)

lcd.clear()
lcd.write_string("Hello Hamna!")
time.sleep(2)

lcd.clear()
lcd.write_string("LCD Working :)")
time.sleep(5)

lcd.clear()
GPIO.cleanup()

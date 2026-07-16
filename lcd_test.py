import board
import digitalio
import time
import adafruit_character_lcd.character_lcd as characterlcd

# Define LCD pins
lcd_rs = digitalio.DigitalInOut(board.D22)
lcd_en = digitalio.DigitalInOut(board.D23)
lcd_d4 = digitalio.DigitalInOut(board.D5)
lcd_d5 = digitalio.DigitalInOut(board.D6)
lcd_d6 = digitalio.DigitalInOut(board.D13)
lcd_d7 = digitalio.DigitalInOut(board.D26)

# LCD dimensions
lcd_columns = 16
lcd_rows = 2

# Initialize LCD
lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en,
    lcd_d4, lcd_d5, lcd_d6, lcd_d7,
    lcd_columns, lcd_rows
)

# Display message
lcd.message = "Hello Hamna!\nLCD Working :)"

time.sleep(10)

lcd.clear()

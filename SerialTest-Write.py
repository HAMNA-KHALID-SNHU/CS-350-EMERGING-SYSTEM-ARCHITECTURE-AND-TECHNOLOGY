import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)

counter = 0

try:
    while True:
        counter += 1
        message = f"Write counter: {counter}\n"
        ser.write(message.encode())
        print(f"Sent: {message.strip()}")
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped by user")

finally:
    ser.close()

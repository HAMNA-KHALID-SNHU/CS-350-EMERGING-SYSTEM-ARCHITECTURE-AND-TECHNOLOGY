import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

try:
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            print(data)

except KeyboardInterrupt:
    print("Stopped by user")

finally:
    ser.close()

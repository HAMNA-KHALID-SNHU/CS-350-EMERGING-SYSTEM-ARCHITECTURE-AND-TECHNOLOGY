import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

print("Client started. Type ON, OFF, or QUIT")

try:
    while True:
        command = input("Enter command: ").strip().upper()
        ser.write((command + "\n").encode())

        if command in ["QUIT", "EXIT"]:
            print("Closing client...")
            break

except KeyboardInterrupt:
    print("Client interrupted")

finally:
    ser.close()

import serial
from gpiozero import LED

led = LED(17)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

state = "OFF"
running = True

print("Server started. Waiting for commands...")

try:
    while running:
        if ser.in_waiting > 0:
            command = ser.readline().decode().strip().upper()
            print(f"Received: {command}")

            match command:
                case "ON":
                    if state != "ON":
                        led.on()
                        state = "ON"
                        print("LED turned ON")
                    else:
                        print("LED already ON")

                case "OFF":
                    if state != "OFF":
                        led.off()
                        state = "OFF"
                        print("LED turned OFF")
                    else:
                        print("LED already OFF")

                case "EXIT" | "QUIT":
                    print("Exiting program...")
                    running = False

                case _:
                    print("Invalid command")

except KeyboardInterrupt:
    print("Program interrupted")

finally:
    led.off()
    ser.close()
    print("Clean exit complete")

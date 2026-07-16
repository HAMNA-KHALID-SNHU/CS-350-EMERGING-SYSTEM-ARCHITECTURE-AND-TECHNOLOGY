import time
import board
import adafruit_dht

# GPIO4 = Pin 7
dhtDevice = adafruit_dht.DHT22(board.D4)

while True:
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity

        print(f"Temp: {temperature:.1f} C  Humidity: {humidity:.1f}%")

    except RuntimeError:
        print("Reading error, retrying...")

    except Exception as error:
        print(error)
        break

    time.sleep(2)

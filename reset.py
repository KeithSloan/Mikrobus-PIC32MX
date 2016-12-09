# External module imports
import RPi.GPIO as GPIO
import time

delay = 1

# Declare Pins
mclrPin = 4 # AN  GPIO4 -> MCLR
blenPin = 5 # RST GPIO5 -> RB9

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
# GPIO 4 MCLR pin set as output
GPIO.setup(mclrPin, GPIO.OUT, initial=GPIO.HIGH)
# GPIO 5 BootLoad Enable pin set as output
GPIO.setup(blenPin, GPIO.OUT, initial=GPIO.HIGH)

# Press BOOTLOAD-EN
print("Press BOOTLOAD-EN")
GPIO.output(blenPin, GPIO.LOW)
time.sleep(delay)

# Press Reset
print("Press Reset")
GPIO.output(mclrPin, GPIO.LOW)
time.sleep(delay)

# Release RESET
print("Release Reset")
GPIO.output(mclrPin, GPIO.HIGH)
time.sleep(delay)

# Release BOOTLOAD-EN
print("Release BOOTLOAD-EN")
GPIO.output(blenPin, GPIO.HIGH)
time.sleep(delay)

# cleanup GPIO
GPIO.cleanup()

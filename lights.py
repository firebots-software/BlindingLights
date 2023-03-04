import time
from rpi_ws281x import *

# LED strip configuration:
LED_COUNT = 7  # Number of LED pixels.
LED_PIN = 12  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

# Intialize the library (must be called once before other functions).
strip.begin()

# Define some colors
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
YELLOW = Color(255, 255, 0)
PURPLE = Color(255, 0, 255)
CYAN = Color(0, 255, 255)
WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)
ORANGE = Color(255, 172, 28)

# Define a function to set all pixels to a given color.
def set_color(color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

# Set all pixels to red.

while True:
	set_color(PURPLE)
	time.sleep(1)

# Set all pixels to yellow.
	set_color(YELLOW)
	time.sleep(1)

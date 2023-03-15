import time
import ntcore as NetworkTables
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

inst = NetworkTables.NetworkTableInstance.getDefault()

#start a NT4 client
inst.startClient4("Test Client")

# connect to a roboRIO with team number TEAM
inst.setServerTeam(3501)

# starting a DS client will try to get the roboRIO address from the DS application
inst.startDSClient()

# connect to a specific host/port
inst.setServer("host", NetworkTables.NetworkTableInstance.kDefaultPort4)

lights_nt = inst.getTable('Lights')
purpleSub = lights_nt.getBooleanTopic("Purple").subscribe()

while True:
    # boolean if all the lights are purple (for the cube)
	
	isPurple = purpleSub.get()
	# Define a function to set all pixels to a given color.
	def set_color(color):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, color)
		strip.show()

	if isPurple:
		set_color(PURPLE)
		time.sleep(1)
	else:
		set_color(YELLOW)
		time.sleep(1)


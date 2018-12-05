try:
	import RPi.GPIO as GPIO
	GPIO.setmode(GPIO.BCM)
	RED = 25
	GREEN = 24
	BLUE = 23
	button = 10
	GPIO.setup(BLUE, GPIO.OUT)
	GPIO.setup(RED, GPIO.OUT)
	GPIO.setup(GREEN, GPIO.OUT)
	GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	def locked():
		print('Locked on target')
		GPIO.output(GREEN, 255)
		GPIO.output(BLUE, 0)
		GPIO.output(RED, 0)	
	def unlocked():
		print('Target not locked')
		GPIO.output(BLUE, 255)
		GPIO.output(GREEN, 0)
		GPIO.output(RED, 255)
	def disabled():
		print('Disabled')
		GPIO.output(BLUE, 255)
		GPIO.output(GREEN, 0)
		GPIO.output(RED, 0)
	def error():
		print('Something went wrong')
		GPIO.output(RED, 255)
		GPIO.output(GREEN, 0)
		GPIO.output(BLUE, 0)
	def initializing():
		print('Initializing')
		GPIO.output(RED, 255)
		GPIO.output(GREEN, 255)
		GPIO.output(BLUE, 255)
	def buttonPress():
	    if GPIO.input(button) == GPIO.HIGH:
	        print("Button was pushed!")
	        return True
	    else:
	        print("Button was not pushed!")
	    	return False

except:
	pass
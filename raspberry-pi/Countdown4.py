import time    
import board
import digitalio
import pwmio 
from adafruit_motor import servo

led1 = digitalio.DigitalInOut(board.GP19)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP20)
led2.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP16)  
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
pwm_servo = pwmio.PWMOut(board.GP5, duty_cycle=2 ** 15, frequency=50)  # set up servo
servo = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

servo1.angle = 0

     if button.value == False: # Button initializes code
     for x in range (10,0,-1):  
     GreenLed.value = True #Turns led on intially
     time.sleep(0.5) # sleep half second
     print(x) # continues  countdown
     led1.value = False #turns led off
     time.sleep(0.5) # sleep other half second
     while True:
     print("Takeoff!") 
     RedLed.value = True #Red Led turns on at end of countdown
     time.sleep(0.5) # Led turns off
     while True:
          print("liftoff!")     #say liftoff
          led2.value = True
          servo.angle = 180  #Turn Servo from 0 degrees to 180
          time.sleep(0.5)

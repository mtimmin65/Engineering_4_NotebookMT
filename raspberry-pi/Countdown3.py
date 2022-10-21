import time 
import board
import digitalio

GreenLed = digitalio.DigitalInOut(board.GP13)  
GreenLed.direction = digitalio.Direction.OUTPUT
RedLed = digitalio.DigitalInOut(board.GP18)
RedLed.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP16) 
button.direction = digitalio.Direction.INPUT # Leds are output, Button is an Input
button.pull = digitalio.Pull.UP 

while True: 
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


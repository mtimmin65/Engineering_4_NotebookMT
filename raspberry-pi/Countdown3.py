import time 
import board
import digitalio

GreenLed = digitalio.DigitalInOut(board.GP13)  
GreenLed.direction = digitalio.Direction.OUTPUT
RedLed = digitalio.DigitalInOut(board.GP18)
RedLed.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP16) 
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP 

while True: 
     if button.value == False:
          for x in reversed(range(11)):
               led1.value = True #light bright
               time.sleep(0.5) #light snooze
               print(x)
               led1.value = False #light off
               time.sleep(0.5)
          while True:
               print("liftoff!") #says dis
               led2.value = True
               time.sleep(0.5)


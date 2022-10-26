import time 
import board
import digitalio 

GreenLed = digitalio.DigitalInOut(board.GP19)
GreenLed.direction = digitalio.Direction.OUTPUT 
RedLed = digitalio.DigitalInOut(board.GP20) 
RedLed.direction = digitalio.Direction.OUTPUT 

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
 

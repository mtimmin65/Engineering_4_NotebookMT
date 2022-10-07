import board  
import adafruit_mpu6050
import busio 
import time
import digitalio 
import terminalio
import displayio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle



displayio.release_displays()


sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP0)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)



def area(x1,y1,x2,y2,x3,y3):
    float(x1)
    float(y1)
    float(x2)
    float(y2)
    float(x3)
    float(y3)
    a1 = int(1/2*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
    area = abs(a1)
    return area

while True: 

    try:
        print('Enter x1,y1')
        x1y1 = input()
        xlist = x1y1.split(",")
        x1=float(xlist[0])
        y1=float(xlist[1])
        print('Enter x2,y2')
        x2y2 = input() 
        x2list = x2y2.split(",")
        x2=float(x2list[0])
        y2=float(x2list[1])
        print('Enter x3,y3')
        x3y3 = input()
        x3list = x3y3.split(",")
        x3=float(x3list[0])
        y3=float(x3list[1])

        splash = displayio.Group()  #create the display group
        hline = Line(0,32,128,32, color=0xFFFF00,)
        splash.append(hline) 
        h2line = Line (64,0,64,64, color=0xFFFF00,)
        splash.append(h2line)
       # circle = Circle(int(x1) + 64, 32 - int(y1), 1, outline=0xFFFF00)
    #    splash.append(circle)
      #  circle2 = Circle(int(x2) + 64, 32 - int(y2), 1, outline=0xFFFF00)
      #  splash.append(circle2)
      #  circle3 = Circle(int(x3) + 64, 32 - int(y3), 1, outline=0xFFFF00)
      #  splash.append(circle3)
        circle3 = Circle(64,32,1, outline=0xFFFF00)
        splash.append(circle3)
        triangle = Triangle(int(x1) + 64, 32 - int(y1), 64 + int(x2), 32 - int(y2), 64 + int(x3), 32 - int(y3), outline=0xFFFF00)
      #  triangle = Triangle(int(x1), int(y1), int(x2), int(y2), int(x3), int(y3))     
        splash.append(triangle) 

        #triangle = Triangle((1/2*(int(x1)*(int(y2)-int(y3)))), color=0xFFFF00,)
        #splash.append(triangle)
        #triangle2 = Triangle((1/2*(int(x2)*(int(y3)-int(y1)))), outline=0xFFFF00)
        #splash.append(triangle2)
        #triangle3 = Triangle((1/2*(int(x3)*(int(y1)-int(y2)))), outline = 0xFFFF00)
        #splash.append(triangle3)
        display.show(splash)

        
    except: 
        print("Error, points are not a valid triangle")

    else:
        print(area(x1,y1,x2,y2,x3,y3))   
     
    


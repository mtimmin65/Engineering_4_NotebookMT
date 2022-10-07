import board
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
from adafruit_display_text import label 
import adafruit_displayio_ssd1306
import terminalio 
import displayio

displayio.release_displays()


display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP15)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x3d)


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

        
    except: 
        print("Error, points are not a valid triangle")

    else:
        print(area(x1,y1,x2,y2,x3,y3))   

import board
import digitalio
import time 

# RGB LED 1
led1 = digitalio.DigitalInOut(board.GP1) # red
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP2) # green
led2.direction = digitalio.Direction.OUTPUT
led3 = digitalio.DigitalInOut(board.GP3) # blue
led3.direction = digitalio.Direction.OUTPUT

# RGB LED 2
led4 = digitalio.DigitalInOut(board.GP5) # red
led4.direction = digitalio.Direction.OUTPUT
led5 = digitalio.DigitalInOut(board.GP6) # green
led5.direction = digitalio.Direction.OUTPUT
led6 = digitalio.DigitalInOut(board.GP7) # blue
led6.direction = digitalio.Direction.OUTPUT

while True:
    led1.value = True     
    led2.value = False    
    led3.value = False
    led4.value = False
    led5.value = True
    led6.value = False
    time.sleep(0.5)

    led1.value = False    
    led2.value = True   
    led3.value = False
    led4.value = False
    led5.value = False
    led6.value = True
    time.sleep(0.5)

    led1.value = False    
    led2.value = False  
    led3.value = True
    led4.value = True
    led5.value = True
    led6.value = True
    time.sleep(0.5)

    led1.value = True   
    led2.value = True   
    led3.value = True
    led4.value = True
    led5.value = False
    led6.value = False
    time.sleep(0.5)
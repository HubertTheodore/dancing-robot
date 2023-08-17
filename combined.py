import adafruit_matrixkeypad
import digitalio
import board
import busio
import displayio
import time
import pwmio
import terminalio
from adafruit_display_text import label
from adafruit_st7789 import ST7789
from adafruit_motor import servo


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


# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.GP14, duty_cycle=2 ** 15, frequency=50) #left leg
pwm2 = pwmio.PWMOut(board.GP4, duty_cycle=2 ** 15, frequency=50) #right leg

pwm3 = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50) #left foot
pwm4 = pwmio.PWMOut(board.GP28, duty_cycle=2 ** 15, frequency=50) #right foot


# Create a servo object, my_servo.
my_servo1 = servo.Servo(pwm) #left leg
my_servo2 = servo.Servo(pwm2) #right leg
leftFoot = servo.Servo(pwm3)
rightFoot = servo.Servo(pwm4)

#https://docs.circuitpython.org/projects/st7789/en/latest/examples.html
# First set some parameters used for shapes and text
BORDER = 20
FONTSCALE = 2
BACKGROUND_COLOR = 0x00FF00  # Bright Green
FOREGROUND_COLOR = 0xAA0088  # Purple
TEXT_COLOR = 0xFFFF00

# Release any resources currently in use for the displays
displayio.release_displays()

tft_cs = board.GP9
tft_dc = board.GP8
spi_mosi = board.GP11
spi_clk = board.GP10
spi = busio.SPI(spi_clk, spi_mosi)
spi_rst = board.GP12
spi_bl = board.GP13

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=spi_rst)
display = ST7789(
    display_bus, rotation=270, width=240, height=135, rowstart=40, colstart=53
)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = BACKGROUND_COLOR

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(
    display.width - BORDER * 2, display.height - BORDER * 2, 1
)
inner_palette = displayio.Palette(1)
inner_palette[0] = FOREGROUND_COLOR
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)

# Draw a label
text = "Hello!"
text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
text_width = text_area.bounding_box[2] * FONTSCALE
text_group = displayio.Group(
    scale=FONTSCALE,
    x=display.width // 2 - text_width // 2,
    y=display.height // 2,
)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)
time.sleep(1)

del splash[2]

text = "Please choose a dance!"
text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
text_width = text_area.bounding_box[2] * FONTSCALE
text_group = displayio.Group(
    scale=FONTSCALE,
    x=display.width // 2 - text_width // 2,
    y=display.height // 2,
)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)
time.sleep(1)


cols = [digitalio.DigitalInOut(x) for x in (board.GP18, board.GP17, board.GP16)]
rows = [digitalio.DigitalInOut(x) for x in (board.GP22, board.GP21, board.GP20, board.GP19)]
keys = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        ('*', 0, '#'))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

def redBlue():
    led1.value = True     
    led2.value = False    
    led3.value = False
    led4.value = False
    led5.value = True
    led6.value = False

def blueGreen():
    led1.value = False    
    led2.value = True   
    led3.value = False
    led4.value = False
    led5.value = False
    led6.value = True

def greenAll():
    led1.value = False    
    led2.value = False  
    led3.value = True
    led4.value = True
    led5.value = True
    led6.value = True

def allRed():
    led1.value = True   
    led2.value = True   
    led3.value = True
    led4.value = True
    led5.value = False
    led6.value = False

def turnOffLEDs():
    led1.value = False  
    led2.value = False  
    led3.value = False
    led4.value = False
    led5.value = False
    led6.value = False

def fancyFeet():
    time.sleep(1)
    del splash[2] # removes current text
    text = "Fancy Feet!"
    text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
    text_width = text_area.bounding_box[2] * FONTSCALE
    text_group = displayio.Group(
        scale=FONTSCALE,
        x=display.width // 2 - text_width // 2,
        y=display.height // 2,
    )
    text_group.append(text_area)  # Subgroup for text scaling
    splash.append(text_group)
    # move 1-in and out (works)
    for i in range(4):
        my_servo1.angle = 90
        my_servo2.angle = 90
        leftFoot.angle = 90
        rightFoot.angle = 90
        redBlue()

        time.sleep(0.5)
        my_servo1.angle = 40
        my_servo2.angle = 140
        blueGreen()

        time.sleep(0.5)
        my_servo1.angle = 90
        my_servo2.angle = 90
        greenAll()

    # move 2- up and down (works)


    for i in range(4):
        time.sleep(0.5)

        my_servo1.angle = 90
        my_servo2.angle = 90
        leftFoot.angle = 60
        rightFoot.angle = 120
        allRed()

        time.sleep(0.5)
        leftFoot.angle = 90
        rightFoot.angle = 90
        redBlue()
def footTap():
    del splash[2] # removes current text
    text = "Foot Tap!"
    text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
    text_width = text_area.bounding_box[2] * FONTSCALE
    text_group = displayio.Group(
        scale=FONTSCALE,
        x=display.width // 2 - text_width // 2,
        y=display.height // 2,
    )
    text_group.append(text_area)  # Subgroup for text scaling
    splash.append(text_group)

    # move 3- right foot up and down/ foot tap
    for i in range(4):

        my_servo1.angle = 45
        my_servo2.angle = 90
        leftFoot.angle = 90
        rightFoot.angle = 90
        blueGreen()

        time.sleep(0.5)
        leftFoot.angle = 90
        rightFoot.angle = 130
        greenAll()

        time.sleep(0.5)
        leftFoot.angle = 90
        rightFoot.angle = 90
        allRed()

    # move 3.5- left foot up and down/ foot tap (DOUBLE CHECK/ TEST THIS!)
    for i in range(4):

        my_servo1.angle = 90
        my_servo2.angle = 125
        leftFoot.angle = 90
        rightFoot.angle = 90
        redBlue()
        time.sleep(0.5)

        leftFoot.angle = 50
        rightFoot.angle = 90
        blueGreen()
        time.sleep(0.5)

        leftFoot.angle = 90
        rightFoot.angle = 90
        greenAll()



def simpleWeirdUpAndDown():
    del splash[2] # removes current text
    text = "Up and Down!"
    text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
    text_width = text_area.bounding_box[2] * FONTSCALE
    text_group = displayio.Group(
        scale=FONTSCALE,
        x=display.width // 2 - text_width // 2,
        y=display.height // 2,
    )
    text_group.append(text_area)  # Subgroup for text scaling
    splash.append(text_group)

    # move 4 - alternating up and down/ walking in place
    my_servo1.angle = 70
    my_servo2.angle = 110
    leftFoot.angle = 90
    rightFoot.angle = 90
    allRed()
    time.sleep(0.5)

    for i in range(3):
        for angle in range(90, 0, -5):  # 0 - 90 degrees, -5 degrees at a time.
            #90 to 0
            leftFoot.angle = angle
            if i != 0:
                rightFoot.angle = 180 - (90-angle)
            # 180 to 90
            # 90 85 80
            if angle % 20 == 0:
                redBlue()
            elif angle % 15 == 0:
                blueGreen()
            elif angle % 10 == 0:
                greenAll()
            else:
                allRed()
            time.sleep(0.05)

        for angle in range(0, 90, 5):  # 0 - 90 degrees, -5 degrees at a time.
            leftFoot.angle = angle

            # #90 to 180
            # 0 5 10 15
            rightFoot.angle = 90 + angle
            if angle % 20 == 0:
                redBlue()
            elif angle % 15 == 0:
                blueGreen()
            elif angle % 10 == 0:
                greenAll()
            else:
                allRed()

            time.sleep(0.05)
            
    my_servo1.angle = 90
    my_servo2.angle = 90
    rightFoot.angle = 90
    leftFoot.angle = 90

def weirdUpDownMove():

    del splash[2] # removes current text
    text = "UP AND DOWN!"
    text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
    text_width = text_area.bounding_box[2] * FONTSCALE
    text_group = displayio.Group(
        scale=FONTSCALE,
        x=display.width // 2 - text_width // 2,
        y=display.height // 2,
    )
    text_group.append(text_area)  # Subgroup for text scaling
    splash.append(text_group)

    my_servo1.angle = 70
    my_servo2.angle = 110
    leftFoot.angle = 90
    rightFoot.angle = 90
    time.sleep(1)

    for i in range(3):
        for angle in range(90, 30, -5):  # 90 - 0 degrees, -5 degrees at a time.
            #90 to 0
            leftFoot.angle = angle

            rightFoot.angle = 180 - (90-angle)

            if angle >= 20:
                my_servo1.angle = angle - 20 # 70-0
                my_servo2.angle = angle + 20 #110 -> 40

            if angle % 20 == 0:
                redBlue()
            elif angle % 15 == 0:
                blueGreen()
            elif angle % 10 == 0:
                greenAll()
            else:
                allRed()

            time.sleep(0.05)

        for angle in range(30, 90, 5):  # 0 - 90 degrees, 5 degrees at a time.
            leftFoot.angle = angle

            # #90 to 180
            # 0 5 10 15
            rightFoot.angle = 90 + angle


            my_servo1.angle = angle/5 * 90.0/18.0 # 0-140
            my_servo2.angle = angle/5 * 90.0/18.0 + 40 #40-180
            if angle % 20 == 0:
                redBlue()
            elif angle % 15 == 0:
                blueGreen()
            elif angle % 10 == 0:
                greenAll()
            else:
                allRed()
            time.sleep(0.05)

        for angle in range(90, 0, -5):  # 0 - 90 degrees, -5 degrees at a time.
            #90 to 0
            # leftFoot.angle = angle

            # rightFoot.angle = 180 - (90-angle)

            if angle >= 20:
                my_servo1.angle = angle + 50 # 140 -> 70
                my_servo2.angle = angle + 90 #180 -> 110
            if angle % 20 == 0:
                redBlue()
            elif angle % 15 == 0:
                blueGreen()
            elif angle % 10 == 0:
                greenAll()
            else:
                allRed()

    my_servo1.angle = 90
    my_servo2.angle = 90
    rightFoot.angle = 90
    leftFoot.angle = 90
    
def oneLeg():

    del splash[2] # removes current text
    text = "One Leg!"
    text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
    text_width = text_area.bounding_box[2] * FONTSCALE
    text_group = displayio.Group(
        scale=FONTSCALE,
        x=display.width // 2 - text_width // 2,
        y=display.height // 2,
    )
    text_group.append(text_area)  # Subgroup for text scaling
    splash.append(text_group)


    my_servo1.angle = 90
    my_servo2.angle = 35
    rightFoot.angle = 90
    leftFoot.angle = 90
    redBlue()
    time.sleep(1)

    my_servo1.angle = 90
    my_servo2.angle = 45
    rightFoot.angle = 160
    leftFoot.angle = 105
    blueGreen()

    time.sleep(1)
    for i in range(160, 180, 1):
        rightFoot.angle = i
        if i % 20 == 0:
            redBlue()
        elif i % 15 == 0:
            blueGreen()
        elif i % 10 == 0:
            greenAll()
        else:
            allRed()

    leftFoot.angle = 130

    time.sleep(1)
    for j in range(4):
        for i in range(10,170,5):
            print("Here")
            my_servo2.angle = i
            rightFoot.angle = i
            if i % 20 == 0:
                redBlue()
            elif i % 15 == 0:
                blueGreen()
            elif i % 10 == 0:
                greenAll()
            else:
                allRed()
            time.sleep(0.03)
        for i in range(170,10,-5):
            print("here2")
            my_servo2.angle = i
            rightFoot.angle = i
            if i % 20 == 0:
                redBlue()
            elif i % 15 == 0:
                blueGreen()
            elif i % 10 == 0:
                greenAll()
            else:
                allRed()
            time.sleep(0.03)

    my_servo1.angle = 90
    my_servo2.angle = 90
    rightFoot.angle = 90
    leftFoot.angle = 90


def threeStepsAndShake():
    
    del splash[2] # removes current text
    text = "Three Steps and Shake!"
    text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
    text_width = text_area.bounding_box[2] * FONTSCALE
    text_group = displayio.Group(
        scale=FONTSCALE,
        x=display.width // 2 - text_width // 2,
        y=display.height // 2,
    )
    text_group.append(text_area)  # Subgroup for text scaling
    splash.append(text_group)
    
    for h in range(3):
        my_servo1.angle = 90
        my_servo2.angle = 90
        rightFoot.angle = 90
        leftFoot.angle = 90
        allRed()
        time.sleep(0.03)
        
        my_servo1.angle = 90
        my_servo2.angle = 35
        rightFoot.angle = 90
        leftFoot.angle = 90
        redBlue()
        time.sleep(1)

        my_servo1.angle = 90
        my_servo2.angle = 45
        rightFoot.angle = 160
        leftFoot.angle = 105
        blueGreen()

        time.sleep(0.5)
        for i in range(160, 180, 1):
            rightFoot.angle = i
            if i % 20 == 0:
                redBlue()
            elif i % 15 == 0:
                blueGreen()
            elif i % 10 == 0:
                greenAll()
            else:
                allRed()

        leftFoot.angle = 130
        greenAll()
        time.sleep(0.5)
        
        rightFoot.angle = 120
        my_servo1.angle = 115
        allRed()
        time.sleep(0.5)
        
        my_servo1.angle = 40
        my_servo2.angle = 140
        rightFoot.angle = 90
        leftFoot.angle = 90
        
    time.sleep(1)
    for j in range(4):
        for i in range(40, 140, 5):
            my_servo1.angle = i
            #140->40
            time.sleep(0.03)
            my_servo2.angle = i
            if i % 20 == 0:
                redBlue()
            elif i % 15 == 0:
                blueGreen()
            elif i % 10 == 0:
                greenAll()
            else:
                allRed()
        
        my_servo1.angle = 90
        my_servo2.angle = 90
        rightFoot.angle = 90
        leftFoot.angle = 90

while True:
    key = keypad.pressed_keys
    if key == [1]:
        fancyFeet()
    elif key == [2]:
        footTap()
    elif key == [3]:
        simpleWeirdUpAndDown()
    elif key == [4]:
        weirdUpDownMove()
    elif key == [5]:
        oneLeg()
    elif key == [6]:
        threeStepsAndShake()
    elif key == [0]:
        fancyFeet()
        footTap()
        simpleWeirdUpAndDown()
        weirdUpDownMove()
        oneLeg()
        threeStepsAndShake()
    time.sleep(0.1)
    turnOffLEDs()



# Group number: G28
# Group member: Helen Hua, Hubert Theodore, Blaire Pham, Jiawen Liu
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
led1 = digitalio.DigitalInOut(board.GP1)  # red
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP2)  # green
led2.direction = digitalio.Direction.OUTPUT
led3 = digitalio.DigitalInOut(board.GP3)  # blue
led3.direction = digitalio.Direction.OUTPUT

# RGB LED 2
led4 = digitalio.DigitalInOut(board.GP5)  # red
led4.direction = digitalio.Direction.OUTPUT
led5 = digitalio.DigitalInOut(board.GP6)  # green
led5.direction = digitalio.Direction.OUTPUT
led6 = digitalio.DigitalInOut(board.GP7)  # blue
led6.direction = digitalio.Direction.OUTPUT


# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.GP14, duty_cycle=2 ** 15, frequency=50)  # left leg
pwm2 = pwmio.PWMOut(board.GP4, duty_cycle=2 ** 15, frequency=50)  # right leg

pwm3 = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)  # left foot
pwm4 = pwmio.PWMOut(board.GP28, duty_cycle=2 ** 15, frequency=50)  # right foot


# Create a servo object, my_servo.
my_servo1 = servo.Servo(pwm)  # left leg
my_servo2 = servo.Servo(pwm2)  # right leg
leftFoot = servo.Servo(pwm3)
rightFoot = servo.Servo(pwm4)

buzzer = pwmio.PWMOut(board.GP27, frequency=432, duty_cycle=0, variable_frequency=True)
# Setting up notes for the buzzer
# Referenced from https://www.circuitbasics.com/how-to-use-buzzers-with-raspberry-pi/
tones = {"B0": 31, "C1": 33, "CS1": 35, "D1": 37, "DS1": 39, "E1": 41, "F1": 44, "FS1": 46, "G1": 49, "GS1": 52, "A1": 55, "AS1": 58,
"B1": 62, "C2": 65,  "CS2": 69, "D2": 73, "DS2": 78, "E2": 82, "F2": 87, "FS2": 93, "G2": 98, "GS2": 104, "A2": 110, "AS2": 117,
"B2": 123, "C3": 131, "CS3": 139, "D3": 147, "DS3": 156, "E3": 165, "F3": 175, "FS3": 185, "G3": 196, "GS3": 208, "A3": 220, "AS3": 233,
"B3": 247, "C4": 262, "CS4": 277, "D4": 294, "DS4": 311, "E4": 330, "F4": 349, "FS4": 370, "G4": 392, "GS4": 415, "A4": 440, "AS4": 466,
"B4": 494, "C5": 523, "CS5": 554, "D5": 587, "DS5": 622, "E5": 659, "F5": 698, "FS5": 740, "G5": 784, "GS5": 831, "A5": 880, "AS5": 932,
"B5": 988, "C6": 1047, "CS6": 1109, "D6": 1175, "DS6": 1245, "E6": 1319, "F6": 1397, "FS6": 1480, "G6": 1568, "GS6": 1661, "A6": 1760,
"AS6": 1865, "B6": 1976, "C7": 2093, "CS7": 2217, "D7": 2349, "DS7": 2489, "E7": 2637, "F7": 2794, "FS7": 2960, "G7": 3136, "GS7": 3322,
"A7": 3520, "AS7": 3729, "B7": 3951, "C8": 4186, "CS8": 4435, "D8": 4699, "DS8": 4978
}

#  Transpose songs for the buzzer
song1 = ["D5", "G5", "G5", "A5", "G5" , "FS5", "E5", "E5", "P", "E5", "A5", "A5", "B5", "A5", "G5", "FS5", "D5", "D5", "B5", "B5", "P", 
         "B5", "C6", "B5", "A5", "G5", "E5", "P", "D5", "D5", "E5", "A5", "FS5", "G5"] # WE WISH YOU A MERRY XMAS
song2 = ["F5", "DS5", "GS5", "P", "GS5", "GS5", "AS5", "P", "AS5", "AS5", "C6", "P", "GS5", "GS5", "DS5", "P",
         "F5", "DS5", "GS5", "P", "GS5", "GS5", "AS5", "AS5", "GS5"]  # dango~
song3 = ["G5", "B5", "B5", "G5", "G5", "E5", "P", "B5", "A5", "B5","C6", "B5", "A5", "P", "G5", "B5", "B5", "G5", "G5", "E5", "P"]  # HAVANA
song4 = ["E5", "FS5", "GS5", "FS5", "E5","E5", "E5", "FS5", "FS5", "P", "CS5" ,"E5", "FS5", "GS5", "E5", "E5", "FS5", "FS5"]  # SHAPE OF YOU

song5 = ["C5", "P", "C5", "P", "C5", "D5", "E5", "P", "E5", "D5", "E5", "F5", "G5", "G5", "P", "C6", "C6", "C6",  "G5",  "G5",  "G5", 
         "E5",  "E5", "E5",  "C5",  "C5", "C5", "P", "G5", "F5", "E5", "D5", "C5"] #  ROW ROW ROW YOUR BOAT

song6 = ["C5", "D5", "F5", "D5", "A5", "P", "A5", "G5", "G5", "P",
           "C5", "D5", "F5", "D5", "G5", "P", "G5", "F5", "F5", "E5", "D5", "P",
           "C5", "D5", "F5", "D5", "F5", "F5", "G5", "E5", "E5", "D5", "C5", "C5", "P", "C5", "G5", "G5", "F5"
         ]  # NEVER GONNA GIVE YOU UP 

song0 = ["C5", "C5", "G5", "G5", "A5", "A5", "G5",  "G5", "G5",   
         "F5",  "F5" , "E5", "E5", "D5", "D5", "E5", "D5", "E5", "C5", "C5", "C5",  
         "G5",   "G5",   "F5",   "F5",   "E5",   "E5", "F5", "E5", "F5", "D5", "D5", "D5",
        #  crazy part
         
         "D5", "C5", "B4", "C5", "B4", "C5", "A5", "G5", "FS5", "G5", "F5", "G5", "F5", "G5", "FS5", "A5", "C6", "B5", "D6", "C6", "B5", "A5",
         "A5", "G5", "E6", "D6", "C6", "B5", "A5", "G5", "G5", "F5", "D6", "C6", "B5", "A5", "G5", "F5", "F5", "E5", "C6", "B5", "A5", "G5", "F5", "E5", "D5", "A5", "G5", "B4", "C5", "C5", "C5",  
         # outro
         "C5",   "C5",   "G5",  "G5",   "A5",   "A5",   "G5",  "G5", "G5",   
         "F5", "F5",   "F5" , "F5",  "E5", "E5", "E5", "E5", "D5", "D5",   "D5", "D5",  "E5", "E5", "D5", "D5", "E5", "E5", "C5", "C5", "C5", "C5"
         ]  # FANCY TWINKLE TWINKLE LITTLE STAR - credits to your lie in april + Mozart + musescore

songRick = ["C5", "D5", "F5", "D5", "A5", "A5", "G5", "G5",
           "C5", "D5", "F5", "D5", "G5",  "G5", "F5", "F5", "E5", "D5", 
           "C5", "D5", "F5", "D5", "F5", "F5", "G5", "E5", "E5", "D5", "C5", "C5", "C5", "G5", "G5", "F5"
         ]  # NEVER GONNA GIVE YOU UP 
songExtra = ["F5", "F5",   "F5", "F5", "A5",   "F5", "F5", "A5",   "A5", "A5", "AS5", "C6", "F5", "F5",   "F5",    "A5", "A5", "F5", "E5",  "E5", "E5", "E5",  
          "F5", "F5",   "F5", "F5", "A5",   "F5", "F5", "A5",   "A5", "A5", "AS5", "C6", "F5", "F5",   "F5",   "A5",  "A5",  "A5", "G5",   "G5", "G5", "G5",  
          "F5",   "F5", "G5",   "G5", "A5", "A5", "F5", "G5", "A5", "F5", "F5", "G5",   "G5", "A5", "A5", "F5", "G5", "A5", "F5", "F5", "G5",   "G5", "A5", "F5", "G5", "A5", "F5",   "F5",   "F5", "F5"
        ]  # NEW JEANS- OMG 
pianoPlay = ["C5", "D5", "E5", "F5", "G5", "A5", "B5", "C6", "D6", "E6"]

def playtone(frequency):
    buzzer.duty_cycle = 2**15
    buzzer.frequency = (frequency)
    time.sleep(0.1)
    buzzer.duty_cycle = 0
    
    
# https://docs.circuitpython.org/projects/st7789/en/latest/examples.html
# Main functionality: LCD
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

text = "Choose a number!"
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

col_pins = [board.GP18, board.GP17, board.GP16]
row_pins = [board.GP22, board.GP21, board.GP20, board.GP19]

rows = [digitalio.DigitalInOut(pin) for pin in row_pins]
cols = [digitalio.DigitalInOut(pin) for pin in col_pins]

# Define the keys on the keypad
keys = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        ('*', 0, '#'))

# Reference code from 
# https://github.com/adafruit/Adafruit_CircuitPython_MatrixKeypad/blob/7d48dba6064a44545b839ef09f74ffd6a4dc0cfc/adafruit_matrixkeypad.py#L34
# Extra functionality: keypad
def read_keypad():
    for pin in rows + cols:
        pin.direction = digitalio.Direction.INPUT
        pin.pull = digitalio.Pull.UP
        
    for r in range(len(rows)):
        row = rows[r]
        row.direction = digitalio.Direction.OUTPUT
        row.value = False

        for c in range(len(cols)):
            col = cols[c]
            if not col.value:
                return keys[r][c]

        row.direction = digitalio.Direction.INPUT
        row.pull = digitalio.Pull.UP

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
    
# Main functionality : Dances
def fancyFeet():
    time.sleep(1)
    del splash[2]  # removes current text
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
    j = 0
    
    for i in range(6):
        my_servo1.angle = 90
        my_servo2.angle = 90
        leftFoot.angle = 90
        rightFoot.angle = 90
        redBlue()
        
        # time.sleep(0.3)
        
        if (j < len(song1) and song1[j] != "P"):
            playtone(tones[song1[j]])
            j = j + 1
        else:
            time.sleep(0.3)
            buzzer.duty_cycle = 0
            j = j + 1

        my_servo1.angle = 40
        my_servo2.angle = 140
        blueGreen()
        
        if (j < len(song1) and song1[j] != "P"):
            playtone(tones[song1[j]])
            j = j + 1
        else:
            time.sleep(0.3)
            buzzer.duty_cycle = 0
            j = j + 1
        
        my_servo1.angle = 90
        my_servo2.angle = 90
        greenAll()
        
        # time.sleep(0.3)
        
        if (j < len(song1) and song1[j] != "P"):
            playtone(tones[song1[j]])
            j = j + 1
        else:
            time.sleep(0.3)
            buzzer.duty_cycle = 0
            j = j + 1
        
        allRed()

    # move 2- up and down (works)
    for i in range(6):

        redBlue()
            
        if (j < len(song1) and song1[j] != "P"):
            playtone(tones[song1[j]])
            j = j + 1
        else:
            time.sleep(0.3)
            buzzer.duty_cycle = 0
            j = j + 1
            
        my_servo1.angle = 90
        my_servo2.angle = 90
        leftFoot.angle = 60
        rightFoot.angle = 120
        blueGreen()
        
        # time.sleep(0.3)
        
        if (j < len(song1) and song1[j] != "P"):
            playtone(tones[song1[j]])
            j = j + 1
        else:
            time.sleep(0.3)
            buzzer.duty_cycle = 0
            j = j + 1

        leftFoot.angle = 90
        rightFoot.angle = 90
        greenAll()
def footTap():
    del splash[2]  # removes current text
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
    j = 0
    # move 3- right foot up and down/ foot tap
    for i in range(4):

        my_servo1.angle = 45
        my_servo2.angle = 90
        leftFoot.angle = 90
        rightFoot.angle = 90
        allRed()
        
        if (j < len(song2) and song2[j] != "P"):
            playtone(tones[song2[j]])
            j = j + 1
        else:
            time.sleep(0.3)
            buzzer.duty_cycle = 0
            j = j + 1

        leftFoot.angle = 90
        rightFoot.angle = 130
        redBlue()
        time.sleep(0.5)
        leftFoot.angle = 90
        rightFoot.angle = 90
        blueGreen()
        
        if (j < len(song2) and song2[j] != "P"):
            playtone(tones[song2[j]])
            j = j + 1
        else:
            time.sleep(0.3)
            buzzer.duty_cycle = 0
            j = j + 1
        greenAll()

    # move 3.5- left foot up and down/ foot tap (DOUBLE CHECK/ TEST THIS!)
    for i in range(4):

        my_servo1.angle = 90
        my_servo2.angle = 125
        leftFoot.angle = 90
        rightFoot.angle = 90
        allRed()
        time.sleep(0.2)
        
        if (j < len(song2) and song2[j] != "P"):
            playtone(tones[song2[j]])
            j = j + 1
        else:
            time.sleep(0.3)
            buzzer.duty_cycle = 0
            j = j + 1

        redBlue()

        leftFoot.angle = 50
        rightFoot.angle = 90
        time.sleep(0.2)
        
        if (j < len(song2) and song2[j] != "P"):
            playtone(tones[song2[j]])
            j = j + 1
        else:
            time.sleep(0.3)
            buzzer.duty_cycle = 0
            j = j + 1

        leftFoot.angle = 90
        rightFoot.angle = 90
        blueGreen()

def simpleWeirdUpAndDown():
    del splash[2]  # removes current text
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
    j = 0
    # move 4 - alternating up and down/ walking in place
    my_servo1.angle = 70
    my_servo2.angle = 110
    leftFoot.angle = 90
    rightFoot.angle = 90
    greenAll()
    time.sleep(0.5)

    for i in range(3):
        for angle in range(90, 0, -5):  # 0 - 90 degrees, -5 degrees at a time.
            # 90 to 0
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

            if (j < len(song3) and song3[j] != "P"):
                playtone(tones[song3[j]])
                j = j + 1
            else:
                buzzer.duty_cycle = 0
                j = j + 1

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
        
            if (j < len(song3) and song3[j] != "P"):
                playtone(tones[song3[j]])
                j = j + 1
            else:
                buzzer.duty_cycle = 0
                j = j + 1
        j = 0
    my_servo1.angle = 90
    my_servo2.angle = 90
    rightFoot.angle = 90
    leftFoot.angle = 90
    time.sleep(1)

def weirdUpDownMove():

    del splash[2]  # removes current text
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
    j = 0
    
    my_servo1.angle = 70
    my_servo2.angle = 110
    leftFoot.angle = 90
    rightFoot.angle = 90
    time.sleep(1)

    for i in range(3):
        for angle in range(90, 50, -5):  # 90 - 0 degrees, -5 degrees at a time.
            # 90 to 0
            leftFoot.angle = angle

            rightFoot.angle = 180 - (90-angle)

            if angle >= 20:
                my_servo1.angle = angle - 20  # 70-0
                my_servo2.angle = angle + 20  # 110 -> 40

            if angle % 20 == 0:
                redBlue()
            elif angle % 15 == 0:
                blueGreen()
            elif angle % 10 == 0:
                greenAll()
            else:
                allRed()
            
            if (j < len(song4) and song4[j] != "P"):
                playtone(tones[song4[j]])
                j = j + 1
            elif (j >= len(song4)):
                j = 0
            else:
                buzzer.duty_cycle = 0
                j = j + 1

        for angle in range(50, 90, 5):  # 0 - 90 degrees, 5 degrees at a time.
            leftFoot.angle = angle

            # #90 to 180
            # 0 5 10 15
            rightFoot.angle = 90 + angle
            
            my_servo1.angle = angle/5 * 90.0/18.0  # 0-140
            my_servo2.angle = angle/5 * 90.0/18.0 + 40  # 40-180
            if angle % 20 == 0:
                redBlue()
            elif angle % 15 == 0:
                blueGreen()
            elif angle % 10 == 0:
                greenAll()
            else:
                allRed()
            
            if (j < len(song4) and song4[j] != "P"):
                playtone(tones[song4[j]])
                j = j + 1
            elif (j >= len(song4)):
                j = 0
            else:
                buzzer.duty_cycle = 0
                j = j + 1

        for angle in range(90, 30, -5):  # 0 - 90 degrees, -5 degrees at a time.
            # 90 to 0
            # leftFoot.angle = angle

            # rightFoot.angle = 180 - (90-angle)

            if angle >= 20:
                my_servo1.angle = angle + 50  # 140 -> 70
                my_servo2.angle = angle + 90  # 180 -> 110
            
            if angle % 20 == 0:
                redBlue()
            elif angle % 15 == 0:
                blueGreen()
            elif angle % 10 == 0:
                greenAll()
            else:
                allRed()
                
            if (j < len(song4) and song4[j] != "P"):
                playtone(tones[song4[j]])
                j = j + 1
            elif (j >= len(song4)):
                j = 0
            else:
                buzzer.duty_cycle = 0
                j = j + 1

    my_servo1.angle = 90
    my_servo2.angle = 90
    rightFoot.angle = 90
    leftFoot.angle = 90

def oneLeg():

    del splash[2]  # removes current text
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
    j = 0
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
        for i in range(10, 170, -10):
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
            if (j < len(song5) and song5[j] != "P"):
                playtone(tones[song5[j]])
                j = j + 1
            elif (j >= len(song5)):
                j = 0
            else:
                buzzer.duty_cycle = 0
                j = j + 1
        for i in range(170, 10, -10):
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
            if (j < len(song5) and song5[j] != "P"):
                playtone(tones[song5[j]])
                j = j + 1
            elif (j >= len(song5)):
                j = 0
            else:
                buzzer.duty_cycle = 0
                j = j + 1

    my_servo1.angle = 90
    my_servo2.angle = 90
    rightFoot.angle = 90
    leftFoot.angle = 90


def threeStepsAndShake():

    del splash[2]  # removes current text
    text = "Three Steps!"
    text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
    text_width = text_area.bounding_box[2] * FONTSCALE
    text_group = displayio.Group(
        scale=FONTSCALE,
        x=display.width // 2 - text_width // 2,
        y=display.height // 2,
    )
    text_group.append(text_area)  # Subgroup for text scaling
    splash.append(text_group)
    j = 0
    
    for h in range(3):
        my_servo1.angle = 90
        my_servo2.angle = 90
        rightFoot.angle = 90
        leftFoot.angle = 90
        
        if (j < len(song6) and song6[j] != "P"):
            playtone(tones[song6[j]])
            j = j + 1
        elif (j >= len(song6)):
            j = 0
        else:
            buzzer.duty_cycle = 0
            j = j + 1
        
        redBlue()
        time.sleep(0.5)
        my_servo1.angle = 90
        my_servo2.angle = 35
        rightFoot.angle = 90
        leftFoot.angle = 90
        blueGreen()
        time.sleep(1)

        my_servo1.angle = 90
        my_servo2.angle = 45
        rightFoot.angle = 160
        leftFoot.angle = 105
        greenAll()

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
        if (j < len(song6) and song6[j] != "P"):
            playtone(tones[song6[j]])
            j = j + 1
        elif (j >= len(song6)):
            j = 0
        else:
            buzzer.duty_cycle = 0
            j = j + 1

        rightFoot.angle = 120
        my_servo1.angle = 115
        
        if (j < len(song6) and song6[j] != "P"):
            playtone(tones[song6[j]])
            j = j + 1
        elif (j >= len(song6)):
            j = 0
        else:
            buzzer.duty_cycle = 0
            j = j + 1

        my_servo1.angle = 40
        my_servo2.angle = 140
        rightFoot.angle = 90
        leftFoot.angle = 90
        allRed()

    time.sleep(1)
    for j in range(4):
        for i in range(40, 140, 5):
            my_servo1.angle = i
            redBlue()
            # 140->40
            time.sleep(0.03)
            my_servo2.angle = i
            blueGreen()
            
            if (j < len(song6) and song6[j] != "P"):
                playtone(tones[song6[j]])
                j = j + 1
            elif (j >= len(song6)):
                j = 0
            else:
                buzzer.duty_cycle = 0
                j = j + 1

        my_servo1.angle = 90
        my_servo2.angle = 90
        rightFoot.angle = 90
        leftFoot.angle = 90

# Extra functionality        
def piano():
    del splash[2]  # removes current text
    text = "In piano"
    text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
    text_width = text_area.bounding_box[2] * FONTSCALE
    text_group = displayio.Group(
        scale=FONTSCALE,
        x=display.width // 2 - text_width // 2,
        y=display.height // 2,
    )
    text_group.append(text_area)  # Subgroup for text scaling
    splash.append(text_group)
    
    while True:  # Reads keypad and plays note
        key = read_keypad()
        if key == 1:
            print(key)
            playtone(tones[pianoPlay[1]])
        elif key == 2:
            print(key)
            playtone(tones[pianoPlay[2]])
        elif key == 3:
            playtone(tones[pianoPlay[3]])
        elif key == 4:
            playtone(tones[pianoPlay[4]])
        elif key == 5:
            playtone(tones[pianoPlay[5]])
        elif key == 6:
            playtone(tones[pianoPlay[6]])
        elif key == 0:
            playtone(tones[pianoPlay[0]])
        elif key == 7:
            playtone(tones[pianoPlay[7]])
        elif key == 8:
            playtone(tones[pianoPlay[8]])
        elif key == 9:
            playtone(tones[pianoPlay[9]])
        elif key == '#':
            break
        
def bequiet():  # Turns off buzzer
    buzzer.duty_cycle = 0

def playsong(mysong):  # Plays a given song
    for i in range(len(mysong)):
        if (mysong[i] == "P"):
            bequiet()
        else:
            playtone(tones[mysong[i]])
        time.sleep(0.3)
    bequiet()

while True:  # Reads keypad and performs a dance
    
    key = read_keypad()
    
    if key == 1:
        fancyFeet()
    elif key == 2:
        footTap()
    elif key == 3:
        simpleWeirdUpAndDown()
    elif key == 4:
        weirdUpDownMove()
    elif key == 5:
        oneLeg()
    elif key == 6:
        threeStepsAndShake()
    elif key == 7:
        playsong(songExtra)
    elif key == 8:
        playsong(song0)
    elif key == 9:
        playsong(songRick)
    elif key == 0:
        fancyFeet()
        footTap()
        simpleWeirdUpAndDown()
        weirdUpDownMove()
        oneLeg()
        threeStepsAndShake()
    elif key == '*':
        piano()
        del splash[2]  # removes current text
        text = "Choose a number:"
        text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
        text_width = text_area.bounding_box[2] * FONTSCALE
        text_group = displayio.Group(
            scale=FONTSCALE,
            x=display.width // 2 - text_width // 2,
            y=display.height // 2,
        )
        text_group.append(text_area)  # Subgroup for text scaling
        splash.append(text_group)
    time.sleep(0.1)
    turnOffLEDs()
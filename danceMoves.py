# Dance moves
# group 28
# Student names: Helen Hua, Blaire Pham, Jiawen Liu, Hubert Theodore

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.GP1, duty_cycle=2 ** 15, frequency=50)

pwm3 = pwmio.PWMOut(board.GP2, duty_cycle=2 ** 15, frequency=50)
pwm4 = pwmio.PWMOut(board.GP3, duty_cycle=2 ** 15, frequency=50)


# Create a servo object, my_servo.
my_servo1 = servo.Servo(pwm) #left leg
my_servo2 = servo.Servo(pwm2) #right leg
leftFoot = servo.Servo(pwm3)
rightFoot = servo.Servo(pwm4)


# SEQUENCE 1:
#  Our most basic and reliable dance sequence. Almost always works regardless of robot's weight distribution 
def fancyFeetWork():
    # move 1-in and out (works)
    for i in range(4):
        my_servo1.angle = 90
        my_servo2.angle = 90
        leftFoot.angle = 90
        rightFoot.angle = 90
        time.sleep(0.5)

        my_servo1.angle = 40
        my_servo2.angle = 140
        time.sleep(0.5)
        my_servo1.angle = 90
        my_servo2.angle = 90

    # move 2- up and down (works)
    for i in range(4):
        time.sleep(0.5)

        my_servo1.angle = 90
        my_servo2.angle = 90
        leftFoot.angle = 60
        rightFoot.angle = 120
        time.sleep(0.5)

        leftFoot.angle = 90
        rightFoot.angle = 90


# SEQUENCE 2:
# should also work regardless of weight distribution. May tip over if it's way too front heavy
def footTap():
    # move 3- right foot up and down/ foot tap 
    for i in range(4):

        my_servo1.angle = 0
        my_servo2.angle = 90
        leftFoot.angle = 90
        rightFoot.angle = 90
        time.sleep(0.5)

        leftFoot.angle = 90
        rightFoot.angle = 130
        time.sleep(0.5)
        leftFoot.angle = 90
        rightFoot.angle = 90

    # move 3.5- left foot up and down/ foot tap (DOUBLE CHECK/ TEST THIS!)
    for i in range(4):

        my_servo1.angle = 90
        my_servo2.angle = 180
        leftFoot.angle = 90
        rightFoot.angle = 90
        time.sleep(0.5)

        leftFoot.angle = 50
        rightFoot.angle = 90
        time.sleep(0.5)

        leftFoot.angle = 90
        rightFoot.angle = 90


# Sequence 3:
# Should work regardless of weight distribution
def simpleWeirdUpAndDown():
    # move 4 - alternating up and down/ walking in place
    my_servo1.angle = 70
    my_servo2.angle = 110
    leftFoot.angle = 90
    rightFoot.angle = 90
    time.sleep(0.5)

    for i in range(3):
        for angle in range(90, 0, -5):  # 0 - 90 degrees, -5 degrees at a time.
            #90 to 0
            leftFoot.angle = angle
            if i != 0:
                rightFoot.angle = 180 - (90-angle)
            # 180 to 90
            # 90 85 80 
            
            time.sleep(0.05)
        
        for angle in range(0, 90, 5):  # 0 - 90 degrees, -5 degrees at a time.
            leftFoot.angle = angle

            # #90 to 180
            # 0 5 10 15
            rightFoot.angle = 90 + angle
            time.sleep(0.05)


# Sequence 4:
# can't be too front heavy, can easily change code to adapt to weight
def weirdUpDownMove():
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

                
            time.sleep(0.05)
        
        for angle in range(30, 90, 5):  # 0 - 90 degrees, 5 degrees at a time.
            leftFoot.angle = angle

            # #90 to 180
            # 0 5 10 15
            rightFoot.angle = 90 + angle

            
            my_servo1.angle = angle/5 * 140.0/18.0 # 0-140
            my_servo2.angle = angle/5 * 140.0/18.0 + 40 #40-180
            time.sleep(0.05)
        
        for angle in range(90, 0, -5):  # 0 - 90 degrees, -5 degrees at a time.
            #90 to 0
            # leftFoot.angle = angle
            
            # rightFoot.angle = 180 - (90-angle)
            
            if angle >= 20:
                my_servo1.angle = angle + 50 # 140 -> 70
                my_servo2.angle = angle + 90 #180 -> 110

            

# SEQUENCE 5: 
# Needs to be top heavy; Changing the code to match it's weight is going to be pretty hard
def oneLeg():
    time.sleep(2)
    my_servo1.angle = 90
    my_servo2.angle = 35
    rightFoot.angle = 90
    leftFoot.angle = 90
    time.sleep(2)

    my_servo1.angle = 90
    my_servo2.angle = 45
    rightFoot.angle = 160
    leftFoot.angle = 105
    time.sleep(2)
    
    for i in range(160, 180, 1):
        rightFoot.angle = i

    time.sleep(2)

    # for i in range(45, 25, -1):
    #     my_servo2.angle = i
    
    # time.sleep(1)
    leftFoot.angle = 130

    time.sleep(1)
    for j in range(4):
        for i in range(10,170,5):
            my_servo2.angle = i
            rightFoot.angle = i
        for i in range(170,10,-5):
            my_servo2.angle = i
            rightFoot.angle = i
    
    
    time.sleep(1)
    my_servo1.angle = 90
    my_servo2.angle = 90
    rightFoot.angle = 90
    leftFoot.angle = 90
    time.sleep(2)

    #time.sleep(100)

# SEQUENCE 6:
# mass has to be centered. Can easily change code to adapt to weight distribution 
# (when he has mass, he can't head bang forward at all, he instantly tips over)
def headBang():
    my_servo1.angle = 90
    my_servo2.angle = 90
    rightFoot.angle = 90
    leftFoot.angle = 90
    
    time.sleep(1)
    my_servo1.angle = 0
    my_servo2.angle = 180
    rightFoot.angle = 90
    leftFoot.angle = 90
    time.sleep(2)

    for j in range(4):
        for i in range(90,150, 3):
            leftFoot.angle = i
            #90->20
            rightFoot.angle = 180-i

        for i in range(150,90, -3):
            # 160 -> 90, 90->60
            leftFoot.angle = i
            #20->90, 90->120
            rightFoot.angle = 180-i

        # with weights inside of him, he cant go the other way, he will instantly tip over
        for i in range(60, 90, -1):
            leftFoot.angle = i
            #120->90
            rightFoot.angle = 180 - i


### MAIN
while True:
    oneLeg()
    fancyFeetWork()
    footTap()
    weirdUpDownMove()
    simpleWeirdUpAndDown()
    # headBang()

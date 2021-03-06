# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries

"""Simple test for using adafruit_motorkit with a stepper motor"""
import threading
import time
import board
# from adafruit_motorkit import MotorKit
# from adafruit_motor import stepper
import RPi.GPIO as GPIO
#import digitalio

# busy = False
# kit = MotorKit(i2c=board.I2C())
# #goingUpSwitchButton = digitalio.DigitalInOut(board.D3)
# #goingUpSwitchButton.direction = digitalio.Direction.INPUT
# numTurns = 0
# MAX_TURNS = 220
# MIN_TURNS = 0

upSwitch1 = 5
downSwitch2 = 11

# def elevator_go_up():
#   global busy
#   
#   if busy :
#       print("elevator going up is already busy\n")
#       return
#   
#   global numTurns
#   global MAX_TURNS
#   if  numTurns >= MAX_TURNS:
#       printf("Already reached the top\n")
#       numTurns = MAX_TURNS
#       busy = False
#       return;
#     
#   print("Going up\n")
#   while numTurns <= MAX_TURNS:
#     kit.stepper1.onestep(direction=stepper.FORWARD)
#     time.sleep(0.005)
#     numTurns = numTurns + 1

# def elevator_go_down():
#     global busy
#     if busy :
#         print("elevator going up is already busy\n")
#         return
#     
#     global numTurns
#     global MAX_TURNS
#     global MIN_TURNS
#     
#     if  numTurns <= MIN_TURNS:
#         print("Already reached the bottom\n")
#         numTurns = MIN_TURNS
#         busy = False
#         return;
#     
#     print("Going down\n")
#     while numTurns >= MIN_TURNS:
#         kit.stepper1.onestep(direction=stepper.BACKWARD)
#         time.sleep(0.005)
#         numTurns = numTurns - 1
        
# 
def main():
    print("Hello elevator\n")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(upSwitch1, GPIO.IN)
    GPIO.setup(downSwitch2, GPIO.IN)
    
    while True:
        print('Switch status = ', GPIO.input(switch))
        time.sleep(1.0)
        
    
if __name__ == "__main__":
    main()
# for i in range(100):
#     kit.stepper1.onestep(direction=stepper.FORWARD)
#     time.sleep(0.005)
# 
# for i in range(100):
#     kit.stepper1.onestep(direction=stepper.BACKWARD)
#     time.sleep(0.005) 



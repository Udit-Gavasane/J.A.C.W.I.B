__author__ = 'Udit-Gavasane'

import socket
import math
import sys
import time
import RPi.GPIO as GPIO



def client_program():
    

    cli_soc = socket.socket()  # instantiate
    cli_soc.connect(('192.168.2.11', 5500))


    while True:
        
        data = cli_soc.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal
        
        steering_angle = int(data)

        speed = 20
        lastTime = 0
        lastError = 0
        
        now = time.time()
        dt = now - lastTime

        kp = 0.4
        kd = kp * 0.65


        deviation = steering_angle - 90
        error = abs(deviation)
        
        if deviation < 10 and deviation > -10:
            deviation = 0
            error = 0
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            steering.stop()

        elif deviation > 10:
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            steering.start(100)
            

        elif deviation < -10:
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            steering.start(100)

        derivative = kd * (error - lastError) / dt
        proportional = kp * error
        PD = int(speed + derivative + proportional)
        spd = abs(PD)
        print(spd)
        
        if spd > 35:
            spd = 35
        
        
        throttle.start(spd)

        lastError = error
        lastTime = time.time()

        
        
        
    cli_soc.close()  # close the connection
    

    
if __name__ == '__main__':
    GPIO.setwarnings(False)

    #throttle
    throttlePin = 25 # Physical pin 22
    in3 = 24 # physical Pin 16 
    in4 = 23 # physical Pin 18

    #Steering of front wheels
    steeringPin = 22 # Physical Pin 15
    in1 = 17 # Physical Pin 11
    in2 = 27 # Physical Pin 13


    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)

    GPIO.setup(throttlePin,GPIO.OUT)
    GPIO.setup(steeringPin,GPIO.OUT)

    # Steering
    # in1 = 1 and in2 = 0 -> Left
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    steering = GPIO.PWM(steeringPin,1000)
    steering.stop()

    # Throttle
    # in3 = 1 and in4 = 0 -> Forward
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    throttle = GPIO.PWM(throttlePin,1000)
    throttle.stop()

    client_program()
    
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    throttle.stop()
    steering.stop()
    
    
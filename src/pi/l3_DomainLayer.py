import Lane_Detection as ld
import cv2
import time
import serial

class AICar:
    curr_steering_angle = 90
    ser = None
    received = None
    
    def __init__(self):
        self.ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=0.001)
        self.received = []
        self.ser.write(b'begin\n')
        time.sleep(3)
        
        print("Car object created.")
        
    def startAIDriving(self):
        detector = ld.LaneDetector(320, 240)
        
        self.ser.write(str.encode(str('1 ')))
        time.sleep(0.03)
        
        print("AI driving started...")
        detector.drive(self.ser)
        
        while self.ser.inWaiting() > 0:
            line = self.ser.readline()
            if line:
                self.received.append(line.decode().strip())
        
        print("AI driving stopped.")
        
    def startManualDriving(self):
        input("Not implemented. Press any key to exit.")
        
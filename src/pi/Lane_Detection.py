import cv2
import l4_InfrastructureLayer as il
import math
import time
import serial

class LaneDetector:
    curr_steering_angle = None
    camera = None
    received = None
    
    def __init__(self, width, height):
        self.camera = cv2.VideoCapture(0)
        self.camera.set(3, width)
        self.camera.set(4, height)
        
        self.curr_steering_angle = 90
        time.sleep(3)
        
    def drive(self, ser):
        while(self.camera.isOpened()):
            _, frame = self.camera.read()
            try:
                edges = il.detect_edges(frame)
                cropped_edges = il.region_of_interest(edges)
                line_segments = il.detect_line_segments(cropped_edges)
                lane_lines = il.average_slope_intercept(frame, line_segments)
                lane_lines_image = il.display_lines(frame, lane_lines)
            except OverflowError:
                print("Overflow error!")
            try:
                final_frame, self.curr_steering_angle = il.steer(frame, lane_lines, self.curr_steering_angle)
            except ValueError:
                print("Running out of lines!")
            cv2.imshow("Edges", edges) 
            cv2.imshow("Lane_lines_image", lane_lines_image)  
            cv2.imshow("The frame", final_frame)
            
            ser.write(str.encode(str(self.curr_steering_angle) + ' '))
            time.sleep(0.03)
            print(self.curr_steering_angle)
            
            if cv2.waitKey(1) & 0xff == ord('q'):
                ser.write(str.encode(str("0")))
                time.sleep(0.03)
                ser.close()
                exit()
    
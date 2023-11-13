import threading
import time
import detection 
import speed 
import pygame 
import randomSpeed

stop_gps_thread = False
pygame.mixer.init()

def play_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

def run_detection_and_speed():
    global stop_gps_thread
    while not stop_gps_thread:
        # Call your detection function
        current_class_name = detection.detect(**vars())
        # Process the detected class, check for speed limit signs, and speed from GPS
        if current_class_name and current_class_name == "60kmph":
            #current_speed = speed.get_speed()
            current_speed = randomSpeed.random_speed()

            while current_speed > 60:
                print ("You are exceeding speed limit. Slow Down !!!")
                play_audio('yolov5\\audio\\slow_down.mp3')
                
            # Compare current_speed with the speed limit and trigger an alert if exceeded
            

# Start the GPS speed reading thread
gps_thread = threading.Thread(target=speed.get_speed)
gps_thread.start()

# Start the detection and speed tracking
run_detection_and_speed()

try:
    while True:
        pass
except KeyboardInterrupt:
    stop_gps_thread = True
    gps_thread.join()  # Wait for the GPS speed reading thread to finish
    gps_thread.terminate()

import pygame
import time

audio_files = {
    '60kmph': 'yolov5\\audio\\60kmph.mp3',
    'pedestrian-crossing': 'yolov5\\audio\\pedestrian_crossing.mp3',
    'traffic_light_red': 'yolov5\\audio\\red.mp3',
}

pygame.mixer.init()

def play_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
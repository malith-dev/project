import time
from speed import get_speed

def speed_tracking_process(result_queue):
    while True:
        speed = get_speed()
        result_queue.put(speed)
        time.sleep(1)
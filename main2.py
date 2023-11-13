import multiprocessing
import time
from detection import detect
from speed_tracker import speed_tracking_process

def traffic_sign_detection_process(result_queue):
    current_class_name = detect()
    result_queue.put(current_class_name)

if __name__ == '__main__':
    result_queue = multiprocessing.Queue()

    detection_process = multiprocessing.Process(target=traffic_sign_detection_process, args=(result_queue,))
    tracking_process = multiprocessing.Process(target=speed_tracking_process, args=(result_queue,))

    try:
        detection_process.start()
        tracking_process.start()

        while True:
            if not result_queue.empty():
                result = result_queue.get()
                # Add your logic to handle the result

            time.sleep(1)

    except KeyboardInterrupt:
        detection_process.terminate()
        tracking_process.terminate()
        detection_process.join()
        tracking_process.join()

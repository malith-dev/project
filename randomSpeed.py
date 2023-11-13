import random

def random_speed():
    """
    Generate a random speed value for testing.
    """
    # Assuming the speed is in kilometers per hour (km/h)
    min_speed = 60
    max_speed = 120  # You can adjust the maximum speed based on your requirements

    # Generate a random speed value between min_speed and max_speed
    speed = random.uniform(min_speed, max_speed)
    rounded_speed = round(speed, 4)
    return rounded_speed






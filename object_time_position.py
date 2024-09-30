import time
import random  # Simulating the object's position

# Assuming the robotic arm class is defined as above
class ConveyorBelt:
    def __init__(self, speed):
        self.speed = speed  # Speed in units per second
        self.objects = []   # List to store detected objects

    def detect_object(self):
        """Simulates object detection and returns its initial position."""
        if random.random() > 0.8:  # Simulate a 20% chance of detecting an object
            object_position = random.randint(5, 15)  # Random position on the conveyor
            print(f"Object detected at position {object_position}")
            self.objects.append(object_position)

    def get_object_position(self, initial_position, time_elapsed):
        """Calculate the current position of the object based on the elapsed time."""
        return initial_position - self.speed * time_elapsed  # Moving towards the robot

class PickAndPlaceRobot():
    def __init__(self):
        super().__init__()

    def track_and_pick_object(self, conveyor, initial_position):
        time_elapsed = 0
        while True:
            # Calculate object's position as time goes on
            current_position = conveyor.get_object_position(initial_position, time_elapsed)
            print(f"Object at position {current_position} after {time_elapsed} seconds")

            # If the object reaches the robot's picking zone (e.g., position 0)
            if current_position <= 0:
                print("Object is within reach. Picking the object.")
                self.pick_object(base_angle=45, arm_angle=30)  # Example angles
                break  # Exit after picking
            time.sleep(1)  # Simulate a time delay for tracking
            time_elapsed += 1

if __name__ == "__main__":
    # Initialize conveyor with a speed of 1 unit per second
    conveyor = ConveyorBelt(speed=1)

    # Initialize the robot
    robotic_arm = PickAndPlaceRobot()

    # Simulate continuous conveyor operation
    for _ in range(10):  # Simulate 10 time steps for the conveyor belt
        conveyor.detect_object()  # Detect objects at random intervals

        if conveyor.objects:
            # For each detected object, track and pick it
            initial_object_position = conveyor.objects.pop(0)
            robotic_arm.track_and_pick_object(conveyor, initial_object_position)

        time.sleep(1)  # Simulate the conveyor belt moving forward

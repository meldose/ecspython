from neurapy.robot import Robot
import time
import math

# Define constants for conveyor tracking
CONVEYOR_SPEED = 0.1  # m/s
SORT_POSITION_COBOT1 = [0.5, 0.0, 0.3]  # XYZ coordinates for cobot 1 pick position
PICK_POSITION_COBOT2 = [1.0, 0.0, 0.3]  # XYZ coordinates for cobot 2 pick position
DROP_POSITION = [1.5, 0.0, 0.3]  # XYZ coordinates for drop position
CONVEYOR_LENGTH = 2.0  # Length of the conveyor in meters

# Cobot class for representing cobots in the system
class Cobot1:
    def __init__(self,name,sort_position):
        self.name = name
        self.sort_position= sort_position
        
    def move_to_position(self, position):
        print(f"{self.name} moving to position {position}")
        # Simulate move time
        time.sleep(4)

    def sort_object(self):
        print(f"{self.name} sorting object")
        # Simulate sorting process
        time.sleep(4)
        
class Cobot2:
    def __init__(self,name,pick_position):
        self.name = name
        self.pick_position= pick_position
        

    def move_to_position(self, position):
        print(f"{self.name} moving to position {position}")
        # Send command to move cobot to the given position
        time.sleep(4)  # Simulating move time

    def pick_object(self):
        print(f"{self.name} picking up object")
        # Send command to pick the object
        time.sleep(4)

    def place_object(self, position):
        print(f"{self.name} placing object at {position}")
        # Send command to place the object
        time.sleep(4)

# Function to track conveyor and coordinate cobots
def conveyor_tracking(cobot1, cobot2):
    conveyor_position = 0.0  # Starting position of objects on the conveyor
    
    while conveyor_position <= CONVEYOR_LENGTH:
        # Update the position of the object on the conveyor
        conveyor_position += CONVEYOR_SPEED
        print(f"Object at conveyor position: {conveyor_position:.2f} meters")
        
        # If object reaches Cobot 1 sort position
        if math.isclose(conveyor_position, SORT_POSITION_COBOT1[0], abs_tol=0.05):
            print("Cobot 1 is ready to sort the item in the conveyor belt")
            cobot1.move_to_position(SORT_POSITION_COBOT1)
            cobot1.sort_object()

        # If object reaches Cobot 2 pick position
        elif math.isclose(conveyor_position, PICK_POSITION_COBOT2[0], abs_tol=0.05):
            print("Cobot 2 is ready to pick")
            cobot2.move_to_position(PICK_POSITION_COBOT2)
            cobot2.pick_object()

            # After Cobot 2 picks the object, it places it at the drop position
            cobot2.move_to_position(DROP_POSITION)
            cobot2.place_object(DROP_POSITION)

            # Once the object is dropped, reset for the next object
            conveyor_position = 0.0

        time.sleep(4)  # Simulate conveyor movement

# Main execution
if __name__ == "__main__":
    # Initialize cobots
    cobot1 = Cobot1(name="Cobot1", sort_position=SORT_POSITION_COBOT1)
    cobot2 = Cobot2(name="Cobot2", pick_position=PICK_POSITION_COBOT2)

    # Start conveyor tracking and coordination
    conveyor_tracking(cobot1, cobot2)

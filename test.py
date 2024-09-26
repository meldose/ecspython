import random
import time

# Assuming these robots are imported from neurapy.robot
from neurapy.robot import robot

class Camera:
    def __init__(self):
        self.item_detected = False
        self.item_position = None
        self.item_type = None

    def detect_item(self):
        self.item_detected = random.choice([True])
        if self.item_detected:
            self.item_position = (random.randint(0, 150), random.randint(0, 80))  # Random position on conveyor
            self.item_type = random.choice(["circle", "square", "rectangle", "oval", "star"])
        else:
            self.item_position = None
            self.item_type = None
        return self.item_detected, self.item_position, self.item_type

    def send_signal(self):
        if self.item_detected:
            print("Signal: Item detected, sending signal to sorting robot.")
            return True
        return False


class RobotHandler:
    def __init__(self, sorting_robot, picking_robot, conveyor_speed=0.2):
        self.sorting_robot = sorting_robot
        self.picking_robot = picking_robot
        self.conveyor_speed = conveyor_speed  # Conveyor speed in meters per second
        self.detection_time = None

    def activate_robots(self):
        self.sorting_robot.activate_servo_interface('position')
        self.picking_robot.activate_servo_interface('position')

    def deactivate_robots(self):
        self.sorting_robot.deactivate_servo_interface()
        self.picking_robot.deactivate_servo_interface()

    def sort_item(self, detected_position):
        self.detection_time = time.time()
        sorting_pose = self.sorting_robot.get_current_cartesian_pose()

        while True:
            current_time = time.time()
            conveyor_position_offset = self.conveyor_speed * (current_time - self.detection_time)
            updated_sorting_position = detected_position[:]
            updated_sorting_position[1] += conveyor_position_offset  # Update Y-coordinate

            self.sorting_robot.movelinear_online(updated_sorting_position, velocity=[0.15]*7, acceleration=[2.]*7)

            if self.sorting_robot.reaches_target_position(updated_sorting_position):
                print("Object sorted")
                break

    def pick_item(self, sorted_position):
        picking_pose = self.picking_robot.get_current_cartesian_pose()

        while True:
            current_time = time.time()
            conveyor_position_offset = self.conveyor_speed * (current_time - self.detection_time)
            updated_picking_position = sorted_position[:]
            updated_picking_position[1] += conveyor_position_offset  # Update Y-coordinate

            self.picking_robot.movelinear_online(updated_picking_position, velocity=[0.15]*7, acceleration=[2.]*7)

            if self.picking_robot.reaches_target_position(updated_picking_position):
                print("Object picked")
                break


class ConveyorTrackingSystem:
    def __init__(self, sorting_robot, picking_robot):
        self.camera = Camera()
        self.robot_handler = RobotHandler(sorting_robot, picking_robot)
        self.boxes = {
            "Box-a": [],
            "Box-b": [],
            "Box-c": [],
            "Box-d": [],
            "Box-e": []
        }

    def run(self):
        self.robot_handler.activate_robots()

        for _ in range(5):
            print("Camera scanning for items on the conveyor belt")
            item_detected, position, item_type = self.camera.detect_item()
            print("##############################################################")
            if item_detected:
                print(f"Item detected at position {position}, identified as {item_type}.")

                if self.camera.send_signal():
                    self.robot_handler.sort_item(position)

                    box_mapping = {
                        "circle": "Box-a",
                        "square": "Box-b",
                        "rectangle": "Box-c",
                        "oval": "Box-d",
                        "star": "Box-e"
                    }

                    # After sorting, pick the item
                    self.robot_handler.pick_item(position)

                    # Place item in the correct box
                    box = box_mapping.get(item_type)
                    if box:
                        self.boxes[box].append(1)  # Add the item to the corresponding box
                        print(f"Item of type {item_type} placed in {box}.")
                    else:
                        print(f"Error: No box found for item type {item_type}.")

            else:
                print("No item detected.")

            time.sleep(4)

        print("\nFinal Box Contents:")
        for item_type, box in self.boxes.items():
            print(f"{item_type.capitalize()} box contains: {len(box)} items.")

        self.robot_handler.deactivate_robots()


# Assuming you have robots `robot1` and `robot2` defined elsewhere
# from neurapy.robot import Robot

# robot1 = Robot()
# robot2 = Robot()

if __name__ == "__main__":
    tracking_system = ConveyorTrackingSystem(robot1, robot2)
    tracking_system.run()

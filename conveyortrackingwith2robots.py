from neurapy.robot import Robot
import random
import time
r = Robot()


class Camera:
    def __init__(self):
        self.item_detected = False
        self.item_position = None
        self.item_type = None  # This could represent size, color, or other criteria

    def detect_item(self):
        # Randomly simulate item detection
        self.item_detected = random.choice([True, False])
        if self.item_detected:
            self.item_position = (random.randint(0, 100), random.randint(0, 100))  # Random position on conveyor
            self.item_type = random.choice(["circle", "square", "rectangle"])  # Simulate different item types
        else:
            self.item_position = None
            self.item_type = None
        return self.item_detected, self.item_position, self.item_type

class Cobot:
    def __init__(self, name):
        self.name = name
        self.is_busy = False

    def sort_item(self, position, item_type):
        if not self.is_busy:
            print(f"{self.name} is moving to sort the item at position {position}, identified as {item_type}.")
            self.is_busy = True
            time.sleep(2)  # Simulate sorting time
            print(f"{self.name} has sorted the item (type: {item_type}) and placed it in the sorted area.")
            self.is_busy = False
            return True  # Sorting done
        else:
            print(f"{self.name} is currently busy sorting.")
            return False

    def pick_sorted_item(self):
        if not self.is_busy:
            print(f"{self.name} is moving to pick up the sorted item from the sorted area.")
            self.is_busy = True
            time.sleep(2)  # Simulate picking up sorted item
            print(f"{self.name} has picked the sorted item from the sorted area.")
            self.is_busy = False
        else:
            print(f"{self.name} is currently busy picking up items.")

class ConveyorTrackingSystem:
    def __init__(self):
        self.camera = Camera()
        self.cobot1 = Cobot("Cobot 1 (Sorter)")
        self.cobot2 = Cobot("Cobot 2 (Picker)")
        self.sorted_items = []  # List to track sorted items ready for pickup

    def run(self):
        while True:
            print("Camera scanning for items...")
            item_detected, position, item_type = self.camera.detect_item()

            if item_detected:
                print(f"Item detected at position {position}, identified as {item_type}.")

                # Assign cobot1 to sort the item
                if not self.cobot1.is_busy:
                    sorting_done = self.cobot1.sort_item(position, item_type)
                    if sorting_done:
                        # Add the sorted item to the list of items to be picked
                        self.sorted_items.append(item_type)
                else:
                    print(f"{self.cobot1.name} is busy. Waiting for sorting to complete.")
            else:
                print("No item detected.")

            # Cobot2 picks sorted items if available
            if self.sorted_items and not self.cobot2.is_busy:
                self.cobot2.pick_sorted_item()
                self.sorted_items.pop(0)  # Remove the item from the sorted list after it is picked

            # Wait before the next camera scan
            time.sleep(3)

# Running the conveyor tracking system
if __name__ == "__main__":
    tracking_system = ConveyorTrackingSystem()
    tracking_system.run()

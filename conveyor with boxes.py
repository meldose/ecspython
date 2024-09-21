# from neurapy.robot import Robot
import random
import time

# Defining a Class called Camera
class Camera:
    def __init__(self):
        self.item_detected = True  # An item is detected and taken into consideration
        self.item_position = None
        self.item_type = None  # This could represent size, color, or other criteria

    # Defining a function called detect item
    def detect_item(self):
        # Randomly simulate item detection
        self.item_detected = random.choice([True])
        if self.item_detected:
            self.item_position = (random.randint(0, 150), random.randint(0, 80))  # Random position on conveyor placed
            self.item_type = random.choice(["circle", "square", "rectangle", "oval", "star"]) # Simulate different item types
            
        else:
            self.item_position = None
            self.item_type = None
        return self.item_detected, self.item_position, self.item_type

# Defining a Class called Cobot  
class Cobot:
    def __init__(self, name):
        self.name = name
        self.is_busy = False  # Set cobot to not busy initially

    def sort_item(self, position, item_type):
        if not self.is_busy:
            print(f"{self.name} is moving to sort the item at position {position}, identified as {item_type}.")
            self.is_busy = True
            time.sleep(2)  # Simulate sorting time
            print(f"{self.name} has sorted the item (type: {item_type}) and placed it in the conveyor belt for Cobot2")
            self.is_busy = False
            return True  # Sorting done
        else:
            print(f"{self.name} is currently busy sorting.")
            return False

#     # defining a function called pick_sorted_item 
#     def pick_sorted_item(self, item_type, boxes):
#         if not self.is_busy:
#             print(f"{self.name} is moving to pick up the sorted item of type {item_type} from the sorted area.")
#             self.is_busy = True
#             time.sleep(2)  # Simulate picking up sorted item
#             print(f"{self.name} has picked the sorted item of type {item_type} from the sorted area.")

# ########################################DONE#############################################################
#             # Place the picked item in the correct box

#             if item_type in boxes:
#                 boxes[item_type].append(boxes)  # Add the item to the corresponding box
#                 print(f"{self.name} has placed the item of type {item_type} in the {boxes} box.")
#             else:
#                 print(f"Error: No box found for item type {item_type}.")
            
#             self.is_busy = False
#         else:
#             print(f"{self.name} is currently busy picking up items.")

# defining a function called pick_sorted_item 
    def pick_sorted_item(self, item_type, boxes):
        box_mapping = { # Mapping between item types and box names
        "circle": "Box-a", 
        "square": "Box-b",
        "rectangle": "Box-c",
        "oval": "Box-d",
        "star": "Box-e"
    }
        if not self.is_busy:
            print(f"{self.name} is moving to pick up the sorted item of type {item_type} from the sorted area.")
        self.is_busy = True
        time.sleep(2)  # Simulate picking up sorted item
        print(f"{self.name} has picked the sorted item of type {item_type} from the sorted area.")

        ########################################DONE#############################################################
        # Place the picked item in the correct box
        box_name = box_mapping.get(item_type)
        if box_name:
            boxes[box_name].append(1)  # Add the item to the corresponding box
            print(f"{self.name} has placed the item of type {item_type} in {box_name}.")
        else:
            print(f"Error: No box found for item type {item_type}.")    
        self.is_busy = False
    # else:
    #     print(f"{self.name} is currently busy picking up items.")


# Defining a Class called ConveyorTrackingSystem 
class ConveyorTrackingSystem:
    def __init__(self):
        self.camera = Camera()
        self.cobot1 = Cobot("Cobot 1 (Sorter)")
        self.cobot2 = Cobot("Cobot 2 (Picker)")
        self.sorted_items = []  # List to track sorted items ready for pickup
        self.boxes = {
            "Box-a": [1], 
            "Box-b": [1], 
            "Box-c": [1], 
            "Box-d": [1], 
            "Box-e": [1]
        }                    # Dictionary to hold boxes for different item types

    def run(self):
        iteration = 0
        while iteration < 4:  # Add a condition to stop after 4 iterations
            print("Camera scanning for items on the conveyor belt")
            item_detected, position, item_type = self.camera.detect_item()
            print("##############################################################") 
            if item_detected:
                print(f"Item detected at position {position}, identified as {item_type}.")

                # Assign cobot1 to sort the item
                if not self.cobot1.is_busy:
                    sorting_done = self.cobot1.sort_item(position, item_type)
                    if sorting_done:
                        # Add the sorted item to the list of items to be picked
                        self.sorted_items.append(item_type)
                        # Cobot2 picks the item immediately after it's sorted
                        if not self.cobot2.is_busy and self.sorted_items:
                            # Cobot2 only picks after Cobot1 has sorted
                            self.cobot2.pick_sorted_item(self.sorted_items.pop(0), self.boxes)  # Pass the sorted item type for picking
                else:
                    print(f"{self.cobot1.name} is busy. Waiting for sorting to complete.")
            else:
                print("No item detected.")

            # Wait before the next camera scan
            time.sleep(2)
            iteration += 1  # Increment the iteration counter
        
        # Print the contents of the boxes at the end
        print("\nFinal Box Contents:")
        for item_type, box in self.boxes.items():
            print(f"{item_type.capitalize()} box contains: {len(box)} items.")

# Running the conveyor tracking system
if __name__ == "__main__":
    tracking_system = ConveyorTrackingSystem()
    tracking_system.run()

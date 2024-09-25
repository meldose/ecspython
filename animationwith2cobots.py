import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
conveyor_length = 30       # Conveyor length
conveyor_speed = 0.02     # Conveyor belt speed
cobot1_pos = [5, 3]        # Initial position of Cobot 1
cobot2_pos = [15, 3]       # Initial position of Cobot 2
work_area_width = 20       # Width of the work area
work_area_height = 10       # Height of the work area
bins = {"red": [5, 4], "blue": [5, 4], "green": [5, 2]}  # Sorting bins for Cobot 1
object_position = [0, 0]   # Position of object on the conveyor

# Different items (sorted by color)
items = [{"color": "red", "pos": [0, 1]}, {"color": "blue", "pos": [5, 1]}, {"color": "green", "pos": [10, 1]}]
item_speed = conveyor_speed

# Create figure
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, work_area_width)
ax.set_ylim(0, work_area_height)
ax.set_title("CONVEYOR TRACKING WITH 2 COBOTS FOR SORTING AND PICKING")

# Conveyor belt (horizontal line)
conveyor_belt, = ax.plot([], [], lw=25, color='black')

# Cobots (blue and red circles)
cobot1, = ax.plot([], [], 'yo', markersize=20, label="Cobot 1(sorter)")
cobot2, = ax.plot([], [], 'co', markersize=20, label="Cobot 2)(Picker)")

# Items (objects on the conveyor)
item_markers = []
for item in items:
    marker, = ax.plot([], [], 'o', color=item["color"], markersize=10)
    item_markers.append(marker)

# Work area outline
ax.add_patch(plt.Rectangle((0, 0), work_area_width, work_area_height, fill=False, edgecolor='blue', linewidth=2))

# Legend
ax.legend()

# Initialize function for animation
def init():
    conveyor_belt.set_data([], [])
    cobot1.set_data([], [])
    cobot2.set_data([], [])
    for marker in item_markers:
        marker.set_data([], [])
    return [conveyor_belt, cobot1, cobot2] + item_markers

# Function for sorting and picking logic
def update(frame):
    global object_position, items, cobot1_pos, cobot2_pos

    # Move items along the conveyor
    for i, item in enumerate(items):
        if item["pos"][0] < conveyor_length:
            item["pos"][0] += item_speed
        else:
            item["pos"][0] = 0  # Reset object when it reaches the end

    # Cobot 1: Sort items
    for item in items:
        if abs(cobot1_pos[0] - item["pos"][0]) < 1:  # Cobot 1 picks the item
            item["pos"] = bins[item["color"]]  # Move item to the correct bin
            break  # Only sort one item at a time

    # Cobot 2: Pick up sorted items from bins
    for color, bin_pos in bins.items():
        for item in items:
            if item["pos"] == bin_pos:  # If item is in the bin
                if abs(cobot2_pos[0] - bin_pos[0]) < 1:  # Cobot 2 picks the item
                    item["pos"] = [cobot2_pos[0], cobot2_pos[1] + 1]  # Pick the item
                break

    # Update conveyor belt line
    conveyor_belt.set_data([0, conveyor_length], [1, 1])

    # Update cobot 1 and 2 positions
    cobot1.set_data(cobot1_pos[0], cobot1_pos[1])
    cobot2.set_data(cobot2_pos[0], cobot2_pos[1])

    # Update positions of items
    for marker, item in zip(item_markers, items):
        marker.set_data(item["pos"][0], item["pos"][1])

    return [conveyor_belt, cobot1, cobot2] + item_markers

# Create animation
ani = animation.FuncAnimation(fig, update, frames=200, init_func=init, interval=50, blit=True)

# Show the animation
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
conveyor_length = 20       # Conveyor length
conveyor_speed = 0.05      # Conveyor belt speed
cobot1_pos = [5, 3]        # Initial position of Cobot 1
cobot2_pos = [15, 3]       # Initial position of Cobot 2
work_area_width = 20       # Width of the work area
work_area_height = 6       # Height of the work area
object_position = [0, 0]   # Position of object on the conveyor

# Create figure
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, work_area_width)
ax.set_ylim(0, work_area_height)
ax.set_title("Conveyor Tracking with Two Cobots")

# Conveyor belt (horizontal line)
conveyor_belt, = ax.plot([], [], lw=5, color='black')

# Cobots (blue and red circles)
cobot1, = ax.plot([], [], 'bo', markersize=15, label="Cobot 1")
cobot2, = ax.plot([], [], 'ro', markersize=15, label="Cobot 2")

# Object on the conveyor (green square)
object_marker, = ax.plot([], [], 'gs', markersize=10, label="Object")

# Work area outline
ax.add_patch(plt.Rectangle((0, 0), work_area_width, work_area_height, fill=False, edgecolor='blue', linewidth=2))

# Legend
ax.legend()

# Initialize function for animation
def init():
    conveyor_belt.set_data([], [])
    cobot1.set_data([], [])
    cobot2.set_data([], [])
    object_marker.set_data([], [])
    return conveyor_belt, cobot1, cobot2, object_marker

# Update function for animation
def update(frame):
    global object_position
    
    # Move object along the conveyor
    object_position[0] += conveyor_speed
    if object_position[0] > conveyor_length:
        object_position[0] = 0  # Reset object when it reaches the end

    # Cobot 1 moves towards the object if it is within range
    if abs(cobot1_pos[0] - object_position[0]) < 1:
        cobot1_pos[1] = object_position[1]  # Cobot 1 tracks object vertically
    else:
        cobot1_pos[1] = 3  # Rest position

    # Cobot 2 moves toward the right side of the conveyor
    if abs(cobot2_pos[0] - object_position[0]) < 1:
        cobot2_pos[1] = object_position[1]
    else:
        cobot2_pos[1] = 3

    # Update conveyor belt line
    conveyor_belt.set_data([0, conveyor_length], [1, 1])
    
    # Update positions of cobots
    cobot1.set_data(cobot1_pos[0], cobot1_pos[1])
    cobot2.set_data(cobot2_pos[0], cobot2_pos[1])
    
    # Update object position on the conveyor
    object_marker.set_data(object_position[0], 1)
    
    return conveyor_belt, cobot1, cobot2, object_marker

# Create animation
ani = animation.FuncAnimation(fig, update, frames=200, init_func=init, interval=50, blit=True)

# Show the animation
plt.show()

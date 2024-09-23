import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
conveyor_length = 10  # Length of the conveyor
cobot_positions = np.array([0, 0])  # Initial positions of the cobots
target_positions = np.array([8, 8])  # Target positions for the cobots
speed = 0.1  # Speed of the cobots

# Initialize the figure
fig, ax = plt.subplots()
ax.set_xlim(-1, conveyor_length + 1)
ax.set_ylim(-1, 1)
ax.set_xticks(np.arange(0, conveyor_length + 1, 1))
ax.set_yticks([])

# Draw conveyor
ax.hlines(0, 0, conveyor_length, colors='gray', linewidth=5)

# Draw cobots
cobot1, = ax.plot([], [], 'ro', markersize=10, label='Cobot 1')
cobot2, = ax.plot([], [], 'bo', markersize=10, label='Cobot 2')

# Initialize legend
ax.legend()

# Update function for animation
def update(frame):
    global cobot_positions

    # Update positions towards target
    for i in range(len(cobot_positions)):
        if cobot_positions[i] < target_positions[i]:
            cobot_positions[i] += speed
        elif cobot_positions[i] > target_positions[i]:
            cobot_positions[i] -= speed

    # Update cobot positions in the plot
    cobot1.set_data(cobot_positions[0], 0)
    cobot2.set_data(cobot_positions[1], 0)

    # Return the updated artists
    return cobot1, cobot2

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

# Show the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import time

# Conveyor parameters
conveyor_length = 100  # Length of conveyor in units (e.g., cm)
conveyor_speed = 10    # Speed of conveyor (cm/s)

# Cobot parameters
cobot_position = np.array([50, 10])  # Initial cobot position (x, y) (above conveyor)
cobot_speed = 5  # Cobot movement speed (cm/s)

# Object parameters
object_position = np.array([0, 0])  # Object starts at the beginning of the conveyor
object_speed = conveyor_speed       # Object moves at the speed of the conveyor

# Simulation parameters
simulation_time = 10  # Total simulation time in seconds
time_step = 0.1       # Time step for the simulation

# Proportional control gain for cobot tracking
kp = 0.5

# Lists to store data for plotting
object_positions = []
cobot_positions = []

def move_conveyor_object(obj_pos, speed, dt):
    """ Move the object along the conveyor at a given speed. """
    obj_pos[0] += speed * dt  # Move in the x direction
    if obj_pos[0] > conveyor_length:  # Wrap around if it goes past conveyor end
        obj_pos[0] = 0
    return obj_pos

def cobot_control(cobot_pos, target_pos, kp, max_speed, dt):
    """ Simple proportional control to move cobot toward the target position. """
    error = target_pos[0] - cobot_pos[0]  # Tracking error in x-axis
    control_signal = kp * error  # Proportional control signal
    control_signal = np.clip(control_signal, -max_speed, max_speed)  # Limit cobot speed
    cobot_pos[0] += control_signal * dt  # Update cobot position in x
    return cobot_pos

# Simulation loop
for t in np.arange(0, simulation_time, time_step):
    # Move the object on the conveyor
    object_position = move_conveyor_object(object_position, object_speed, time_step)
    
    # Move the cobot to track the object
    cobot_position = cobot_control(cobot_position, object_position, kp, cobot_speed, time_step)
    
    # Store positions for plotting
    object_positions.append(object_position[0])
    cobot_positions.append(cobot_position[0])
    
    # Print current positions (optional)
    print(f"Time: {t:.2f}s, Object Position: {object_position[0]:.2f}, Cobot Position: {cobot_position[0]:.2f}")
    
    # Sleep to simulate real-time
    time.sleep(time_step)

# Plot the results
plt.plot(np.arange(0, simulation_time, time_step), object_positions, label='Object Position')
plt.plot(np.arange(0, simulation_time, time_step), cobot_positions, label='Cobot Position')
plt.xlabel('Time (s)')
plt.ylabel('Position (cm)')
plt.legend()
plt.title('Cobot Tracking Object on Conveyor')
plt.show()

from neurapy.robot import Robot
import numpy as np
import matplotlib.pyplot as plt

# creatting an Conveyor class
class Conveyor:
    def __init__(self, speed=0.1):  # speed in meters per second
        self.speed = speed  # Conveyor speed
        
    def get_position(self, time):
        """Returns the conveyor position at a given time."""
        return self.speed * time
# Creating an Cobot class
class Cobot:
    def __init__(self, initial_position=0.0, kp=1.0, ki=0.1, kd=0.05):
        self.position = initial_position
        self.kp = kp  # Proportional gain
        self.ki = ki  # Integral gain
        self.kd = kd  # Derivative gain
        self.error_sum = 0.0
        self.previous_error = 0.0
    
    def pid_control(self, target_position, dt):
        """Adjust cobot movement using a PID controller."""
        error = target_position - self.position
        self.error_sum += error * dt
        d_error = (error - self.previous_error) / dt
        
        # PID control law
        control_signal = (self.kp * error) + (self.ki * self.error_sum) + (self.kd * d_error)
        
        self.previous_error = error
        return control_signal

    def move(self, control_signal, dt):
        """Updates cobot position based on control signal."""
        self.position += control_signal * dt

# Simulation parameters
total_time = 20  # seconds
dt = 0.1  # time step
time_steps = np.arange(0, total_time, dt)

# Initialize conveyor and cobot
conveyor = Conveyor(speed=0.05)
cobot = Cobot(initial_position=0.0)

# Store positions for plotting
cobot_positions = []
conveyor_positions = []

for t in time_steps:
    conveyor_position = conveyor.get_position(t)
    conveyor_positions.append(conveyor_position)
    
    control_signal = cobot.pid_control(conveyor_position, dt)
    cobot.move(control_signal, dt)
    cobot_positions.append(cobot.position)

# Plotting the results
plt.plot(time_steps, conveyor_positions, label='Conveyor Position')
plt.plot(time_steps, cobot_positions, label='Cobot Position', linestyle='--')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.legend()
plt.title('Conveyor Tracking by Cobot')
plt.grid(True)
plt.show()

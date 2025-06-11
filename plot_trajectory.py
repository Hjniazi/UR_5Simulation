import matplotlib.pyplot as plt
import numpy as np
from ur5_kinematics import end_effector_position

def plot_trajectory(joint_trajectories):
    """Plot the end-effector trajectory."""
    positions = []
    for joint_angles in joint_trajectories:
        positions.append(end_effector_position(joint_angles))
    
    positions = np.array(positions)
    
    # Plot the end-effector trajectory
    plt.plot(positions[:, 0], positions[:, 1], 'o-', label='End-effector path')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.title('End-effector Trajectory')
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_joint_movements(joint_trajectories):
    """Plot the joint movements over time."""
    steps = len(joint_trajectories)
    time = np.linspace(0, steps, steps)
    
    joint_trajectories = np.array(joint_trajectories)
    
    # Plot each joint's movement
    for i in range(joint_trajectories.shape[1]):
        plt.plot(time, joint_trajectories[:, i], label=f'Joint {i+1}')
    
    plt.xlabel('Time (steps)')
    plt.ylabel('Joint Angle (radians)')
    plt.title('Joint Movements Over Time')
    plt.grid(True)
    plt.legend()
    plt.show()

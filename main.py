import numpy as np
from optimization import optimize_joint_angles, simulate_joint_movements
from plot_trajectory import plot_trajectory, plot_joint_movements

# Initial guess for the joint angles (in radians)
initial_joint_angles = np.array([0, -np.pi/4, np.pi/4, 0, np.pi/2, 0])

# Desired end-effector force (in Newtons)
desired_force = np.array([0, 0, 10])  # Example force in the Z direction

def main():
    print("Starting optimization...")

    # Optimize and get the final joint angles
    optimized_angles = optimize_joint_angles(initial_joint_angles, desired_force)
    print(f"Optimized joint angles: {optimized_angles}")

    # Simulate joint movements over time
    joint_trajectories = simulate_joint_movements(initial_joint_angles, optimized_angles)
    
    # Plot the joint movements
    plot_joint_movements(joint_trajectories)

    # Plot the end-effector trajectory
    plot_trajectory(joint_trajectories)

if __name__ == "__main__":
    main()

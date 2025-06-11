import numpy as np
from scipy.optimize import minimize
from ur5_kinematics import end_effector_position, compute_end_effector_force

# Desired position for the end-effector
desired_position = np.array([0.3, 0.4, 0.2])

def cost_function(joint_angles, desired_force):
    """Cost function to minimize torque (approximated by joint angles squared) and match the desired force."""
    force_error = np.linalg.norm(compute_end_effector_force(joint_angles) - desired_force)
    torque_approximation = np.sum(np.square(joint_angles))
    return torque_approximation + force_error  # Combine both torque minimization and force control

def constraint_eq(joint_angles):
    """Constraint to ensure the end-effector reaches approximately the desired position."""
    tolerance = 0.01  # Allow 1 cm error in the position
    return np.linalg.norm(end_effector_position(joint_angles) - desired_position) - tolerance

def optimize_joint_angles(initial_guess, desired_force):
    """Optimization function to find the joint angles that minimize cost and match desired force."""
    joint_limits = [(-np.pi, np.pi)] * 6  # Joint limits for the UR5

    constraints = {'type': 'eq', 'fun': constraint_eq}

    # Run optimization
    result = minimize(cost_function, initial_guess, args=(desired_force,), bounds=joint_limits, constraints=constraints)
    
    if result.success:
        return result.x
    else:
        raise ValueError("Optimization failed! Reason: {}".format(result.message))

def simulate_joint_movements(initial_angles, final_angles, steps=100):
    """Simulate joint movements by linearly interpolating between initial and final angles."""
    joint_trajectories = np.linspace(initial_angles, final_angles, steps)
    return joint_trajectories

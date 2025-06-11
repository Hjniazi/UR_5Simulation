import numpy as np

# Define UR5 DH parameters (theta, d, a, alpha)
DH_params = np.array([
    [0, 0.089159, 0, np.pi/2],
    [0, 0, -0.425, 0],
    [0, 0, -0.39225, 0],
    [0, 0.10915, 0, np.pi/2],
    [0, 0.09465, 0, -np.pi/2],
    [0, 0.0823, 0, 0]
])

def dh_transform(theta, d, a, alpha):
    """Helper function to compute transformation matrix."""
    return np.array([
        [np.cos(theta), -np.sin(theta) * np.cos(alpha), np.sin(theta) * np.sin(alpha), a * np.cos(theta)],
        [np.sin(theta), np.cos(theta) * np.cos(alpha), -np.cos(theta) * np.sin(alpha), a * np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), d],
        [0, 0, 0, 1]
    ])

def forward_kinematics(joint_angles):
    """Calculate end-effector pose from joint angles."""
    T = np.eye(4)  # Identity matrix as starting point
    for i, params in enumerate(DH_params):
        theta = joint_angles[i] + params[0]
        d = params[1]
        a = params[2]
        alpha = params[3]
        T = np.dot(T, dh_transform(theta, d, a, alpha))
    return T

def end_effector_position(joint_angles):
    """Extracts the position (x, y, z) from the transformation matrix."""
    T = forward_kinematics(joint_angles)
    return T[:3, 3]  # Return only the position part

def compute_end_effector_force(joint_angles):
    """Compute the force exerted by the end-effector (simple example)."""
    # Assuming force in the Z direction only (placeholder calculation)
    return np.array([0, 0, 10])  # Example force output for demonstration

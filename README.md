# 🤖 UR5 Robot Arm Project (Python-Based 6DOF Manipulator)

## 📌 Overview

This project involves modeling, simulating, and visualizing the motion of a **6-DOF UR5 robotic arm** using Python. I implemented both **forward and inverse kinematics**, along with **trajectory planning** and **data visualization** for analyzing motion and control performance.

---

## 🧠 Key Objectives

- Model the **UR5 robot’s kinematics** using Python libraries.
- Simulate both **forward** and **inverse kinematics**.
- Generate and visualize joint trajectories and end-effector paths.
- Recreate and analyze **6 core plots**.
- Lay the groundwork for **advanced control strategies** like RNN or Kriging.

---

## ⚙️ Tools & Technologies

- **Python 3.11+**
- [`numpy`](https://numpy.org/), [`sympy`](https://www.sympy.org): For numerical & symbolic math.
- [`matplotlib`](https://matplotlib.org/): For plotting joint trajectories and 3D paths.
- [`spatialmath`](https://petercorke.com/toolboxes/spatial-math-toolbox/), [`roboticstoolbox-python`](https://github.com/petercorke/roboticstoolbox-python): For UR5 modeling (or custom DH parameter implementation).
- **VS Code**: My main IDE for development.

---

## 📈 Main Outputs

- 🧩 **Joint angle vs. time plots** for all 6 UR5 joints.
- 🌀 **End-effector trajectory in 3D Cartesian space**.
- 📉 **Velocity and error profiles** for control evaluation.
- 📊 Clean, labeled subplots resembling research publications like `xu2020`.

---

## 🧠 My Role

- Built the UR5 manipulator model using **Denavit–Hartenberg (DH) parameters**.
- Implemented **custom inverse kinematics** logic (or optionally used `roboticstoolbox`).
- Developed simulation and trajectory planning pipelines.
- Visualized outputs including:
  - Joint angle plots
  - End-effector paths in 3D
  - Comparative plots of desired vs. actual motion

---

## 🚀 Applications & Future Scope

- Extendable to **real-time robot control** via Python-ROS bridge.
- Foundation for:
  - 🤝 **Human-robot collaboration**
  - 🥽 **VR-based robot teleoperation**
  - 🧠 **AI-integrated motion-force control** (Kriging or RNN)

---

> 📬 Feel free to reach out or collaborate via [hjniazi2001@gmail.com](mailto:hjniazi2001@gmail.com)

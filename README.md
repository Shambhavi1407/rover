# Rover Simulation using URDF and PyBullet

This project presents a physics-based simulation of a four-wheeled robotic rover using URDF (Unified Robot Description Format) and PyBullet. The rover model is designed with realistic physical properties and is controlled interactively through keyboard inputs.

---

## Overview

The objective of this project is to model and simulate a mobile robot capable of basic locomotion in a dynamic environment. The system integrates robot modeling, physics simulation, and real-time control to demonstrate core robotics concepts.

---

## Features

* URDF-based rover model with chassis and four wheels
* Real-time simulation using PyBullet physics engine
* Keyboard-based control for forward, backward, and turning motion
* Differential drive mechanism using independent wheel velocities
* Procedurally generated obstacles (cubes and spheres)
* Collision-aware environment with gravity and friction

---

## Robot Model

The rover is designed as a four-wheel differential drive system consisting of:

* Chassis: Rectangular base with defined mass and inertia
* Wheels: Cylindrical links connected via continuous joints
* Joints: Enable continuous rotation for wheel movement
* Physical properties: Mass, inertia, and collision parameters for realistic behavior

---

## Simulation Environment

The simulation includes:

* Ground plane for surface interaction
* Gravity-enabled physics
* Randomly generated obstacles placed within the environment
* Safe spawn region near the origin

---

## Control System

The rover is controlled using keyboard inputs:

* Up Arrow: Move forward
* Down Arrow: Move backward
* Left Arrow: Turn left (by adjusting wheel velocities)
* Right Arrow: Turn right (by adjusting wheel velocities)

The control logic uses velocity control for joints, enabling differential steering.

---

## Project Structure

```plaintext
rover/
├── rover.urdf
├── control.py
├── spawn.py
├── forward.py
├── circle.py
├── square.py
├── button.py
└── README.md
```

---

## Installation

Install the required dependency:

```bash
pip install pybullet
```

---

## Usage

Run the simulation:

```bash
python control.py
```

Ensure that the URDF file path is correctly specified in the script.

---

## Implementation Details

* Simulation runs in real-time using PyBullet GUI
* Wheel joints are controlled using velocity control
* Turning is achieved by varying left and right wheel speeds
* Obstacles are generated randomly while maintaining a minimum distance from the spawn point

---

## Future Enhancements

* Integration of sensors such as cameras or LiDAR
* Autonomous navigation and obstacle avoidance
* Path planning algorithms
* Improved rover suspension and terrain interaction
* ROS or ROS2 integration

---

## License

This project is open-source and available under the MIT License.

---

## Author

Shambhavi1407

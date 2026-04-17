import pybullet as p
import pybullet_data
import time
import random
import math   # <-- added for distance check

# Connect to PyBullet
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Enable gravity
p.setGravity(0, 0, -10)

# Load ground plane
plane = p.loadURDF("plane.urdf")

# Load your car URDF (update path if needed)
car = p.loadURDF(r"C:\Users\Shambhavi\OneDrive\Desktop\md\rover.urdf", [0, 0, 0.2])

# Wheel mapping 
left_wheels = [1, 3]
right_wheels = [0, 2]

# Disable default joint motors
for joint in range(p.getNumJoints(car)):
    p.setJointMotorControl2(car, joint, controlMode=p.VELOCITY_CONTROL, force=0)

# Parameters
maxForce = 10000
forwardVel = 10
turnFactor = 20   # smaller → wider curves, bigger → sharper turns

# -------- Obstacles --------
obstacles = []
min_distance = 1.0   # safe zone radius around origin

# Cubes
for i in range(15):
    while True:
        x = random.uniform(-5, 5)
        y = random.uniform(-5, 5)
        if math.sqrt(x**2 + y**2) >= min_distance:
            break
    size = random.uniform(0.2, 0.5)
    cube = p.loadURDF("cube.urdf", [x, y, size/2], globalScaling=size)
    p.changeDynamics(cube, -1, mass=0)
    obstacles.append(cube)

# Spheres
for i in range(50):
    while True:
        x = random.uniform(-5, 5)
        y = random.uniform(-5, 5)
        if math.sqrt(x**2 + y**2) >= min_distance:
            break
    sphere = p.loadURDF("sphere_small.urdf", [x, y, 0.03], globalScaling=1)
    p.changeDynamics(sphere, -1, mass=0)
    obstacles.append(sphere)

# ----------------------------

while True:
    keys = p.getKeyboardEvents()

    vel_left = 0
    vel_right = 0

    # Forward
    if p.B3G_UP_ARROW in keys and keys[p.B3G_UP_ARROW] & p.KEY_IS_DOWN:
        vel_left = -forwardVel
        vel_right = -forwardVel

        # Curve forward left
        if p.B3G_LEFT_ARROW in keys and keys[p.B3G_LEFT_ARROW] & p.KEY_IS_DOWN:
            vel_left -= turnFactor

        # Curve forward right
        if p.B3G_RIGHT_ARROW in keys and keys[p.B3G_RIGHT_ARROW] & p.KEY_IS_DOWN:
            vel_right -= turnFactor

    # Backward (with curves)
    elif p.B3G_DOWN_ARROW in keys and keys[p.B3G_DOWN_ARROW] & p.KEY_IS_DOWN:
        vel_left = forwardVel
        vel_right = forwardVel

        # Curve backward left
        if p.B3G_LEFT_ARROW in keys and keys[p.B3G_LEFT_ARROW] & p.KEY_IS_DOWN:
            vel_left += turnFactor

        # Curve backward right
        if p.B3G_RIGHT_ARROW in keys and keys[p.B3G_RIGHT_ARROW] & p.KEY_IS_DOWN:
            vel_right += turnFactor

    # Apply wheel velocities
    for joint in left_wheels:
        p.setJointMotorControl2(car, joint, controlMode=p.VELOCITY_CONTROL, targetVelocity=vel_left, force=maxForce)
    for joint in right_wheels:
        p.setJointMotorControl2(car, joint, controlMode=p.VELOCITY_CONTROL, targetVelocity=vel_right, force=maxForce)

    p.stepSimulation()
    time.sleep(1. / 240)
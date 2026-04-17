import pybullet as p
import pybullet_data
import time
import math

# Setup
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)
planeid = p.loadURDF("plane.urdf")
carId = p.loadURDF(r"C:\Users\Shambhavi\OneDrive\Desktop\md\rover.urdf", [0, 0, 0.2]) # add your rover's path

# Get wheels
# Build joint name-to-index dictionary
joints = {}
for i in range(p.getNumJoints(carId)):
    joint_name = p.getJointInfo(carId, i)[1].decode('utf-8')
    joints[joint_name] = i

# Extract required wheel joints
wheel_names = ['wheel_front_left_joint', 'wheel_front_right_joint', 
               'wheel_back_left_joint', 'wheel_back_right_joint']

fl, fr, bl, br = [joints[name] for name in wheel_names]


def set_wheels(left_vel, right_vel):
    #left wheels get left wala velocity
    p.setJointMotorControl2(carId, fl, p.VELOCITY_CONTROL, targetVelocity=left_vel, force=100)
    p.setJointMotorControl2(carId, bl, p.VELOCITY_CONTROL, targetVelocity=left_vel, force=100)
    #right wheels get right wala velocity
    p.setJointMotorControl2(carId, fr, p.VELOCITY_CONTROL, targetVelocity=right_vel, force=100)
    p.setJointMotorControl2(carId, br, p.VELOCITY_CONTROL, targetVelocity=right_vel, force=100)

def stop():
    set_wheels(0, 0)
    for _ in range(30):
        p.stepSimulation()
        time.sleep(1./240.)

def move(direction, speed=5.0, duration=2.0):
    """Move with smooth acceleration"""
    velocities = {"forward": (speed, speed), "backward": (-speed, -speed), 
                  "rotate_left": (-speed, speed), "rotate_right": (speed, -speed)}
    left_vel, right_vel = velocities[direction]
    
    accel_steps = int(0.2 * 240)  # 0.2s acceleration
    start_time = time.time()
    step = 0
    
    while time.time() - start_time < duration:
        factor = min(1.0, step / accel_steps)
        set_wheels(left_vel * factor, right_vel * factor)
        p.stepSimulation()
        time.sleep(1./240.)
        step += 1
    stop()


move("forward",10,5)
move("backward",10,5)
move("rotate_left",10,5)
move("rotate_right",10,5)

while p.isConnected():
    p.stepSimulation()
    time.sleep(1./240.)
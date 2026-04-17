import pybullet as p
import pybullet_data
import time

# 1. Connect to physics server
physicsClient = p.connect(p.GUI)  # GUI mode
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # for plane.urdf

# 2. Load environment
planeId = p.loadURDF("C:\Users\Shambhavi\OneDrive\Desktop\md\rover.urdf")  # Ground
carId = p.loadURDF(
    r"C:/Users/Geetika Rupani/OneDrive/Desktop/ROS_urdf/robot.urdf",
    [0, 0, 0.1]  # Spawn slightly above ground
)
#change the path of geetika with the one on their system ( right click on urdf file and select “copy as path”

# 3. Set gravity
p.setGravity(0, 0, -9.8)

# Print joint info (debugging)
print("Joint information:")
for i in range(p.getNumJoints(carId)):
    print(i, p.getJointInfo(carId, i)[1])  # index and joint name

# 4. Run simulation (no movement, just spawn)
while p.isConnected():
    p.stepSimulation()
    time.sleep(1./240.)



import pybullet as p, pybullet_data, time 
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.81)
robotId = p.loadURDF(r"C:\Users\Shambhavi\OneDrive\Desktop\md\rover.urdf",[0,0,0.1])
p.loadURDF("plane.urdf")
wheels = []
for i in range(p.getNumJoints(robotId)):       
    joint_info = p.getJointInfo(robotId, i)    
    joint_type = joint_info[2]                
    if joint_type != p.JOINT_FIXED:            
        wheels.append(i)                       

print("Using wheel joints:", wheels)
forces, dt = 1000, 1/240
speeds = {0:5,2:5, 1:12, 3:12}
for j,v in speeds.items():
    p.setJointMotorControl2(
    bodyUniqueId = robotId,      # which robot
    jointIndex = j,              # which joint (wheel)
    controlMode = p.VELOCITY_CONTROL, # how we control it
    targetVelocity = v,          # desired wheel speed
    force = forces               # max motor torque which motor can use to reach that velocity
)
for x in range(5000):
    p.stepSimulation(); time.sleep(dt)
for j in wheels:
    p.setJointMotorControl2(robotId,j,p.VELOCITY_CONTROL,targetVelocity=0,force=forces)
print("Circle motion done!")
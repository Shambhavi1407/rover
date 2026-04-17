import pybullet as p, pybullet_data, time
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.81)

robotId = p.loadURDF(r"C:\Users\Shambhavi\OneDrive\Desktop\md\rover.urdf",[0,0,0.25])
p.loadURDF("plane.urdf")

wheels = [i for i in range(p.getNumJoints(robotId)) if p.getJointInfo(robotId,i)[2]!=p.JOINT_FIXED]
forces, dt = 1000, 1/240

def drive(speeds, steps):
    for j,v in speeds.items():
        p.setJointMotorControl2(robotId,j,p.VELOCITY_CONTROL,targetVelocity=v,force=forces)
    for x in range(steps):
        p.stepSimulation(); time.sleep(dt)

for x in range(16):
    drive({0:10,1:10,2:10,3:10}, 500)
    drive({0:-7 ,2:-7,1:7,3:7}, 400)

for j in wheels:
    p.setJointMotorControl2(robotId,j,p.VELOCITY_CONTROL,targetVelocity=0,force=forces)

print("Square motion done!")
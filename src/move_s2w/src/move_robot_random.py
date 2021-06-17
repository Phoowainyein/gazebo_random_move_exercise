#! /usr/bin/python3

import rospy
# Twist is linear and angular velocity
from geometry_msgs.msg import Point,Twist
# Position, orientation, linear velocity, angular velocity
from nav_msgs.msg import Odometry
from math import atan2
from tf.transformations import euler_from_quaternion
import random 


def callback(data):
    vel_msg = Twist()
    pose=data.pose.pose.position
    print(data)

    if pose.x > 19 or pose.y < 19:
        
        vel_msg.angular.z = -0.3
        vel_msg.linear.x = 1
    elif pose.x < 19 or pose.y > 19:
       
        vel_msg.angular.z = -0.3
        vel_msg.linear.x = 1
    else:
        vel_msg.angular.z=random.randint(-2,2)
        vel_msg.linear.x=random.randint(2,10)

    velocity_publisher.publish(vel_msg)

    
    
rospy.init_node('simple_controller')
 # Publisher to control the robot's speed
velocity_publisher =rospy.Publisher('/cmd_vel',Twist,queue_size=10)
pose_subscriber =rospy.Subscriber('/odom',Odometry,callback)

vel_msg = Twist()
r =rospy.Rate(4)




while not rospy.is_shutdown():
    rospy.spin()

# 1- using the cmd_vel topic you don't have to worry about moving the wheels individually, 
# that is done for you.

# 2 - in order to move any robot to a specific point you must first know
#  where it is and which way it is facing.
#   You'll then need to plan a path which the robot must follow to arrive at the final 
#   goal point. This is a more complex process than simply issuing a cmd_vel message.

# 3 - the cmd_vel topic controls the speed and direction a robot should move in at a
#  specific point in time by sending multiple varying cmd_vel messages over time you 
#  can make a robot follow a sinusoidal path or any other path for that matter.

"""Understanding Topics cmd_vel & odom
To recap the flow so far, first teleop_twist_keyboard publishes velocity commands on a topic
 called cmd_vel. This topic is subscribed by the differential drive Gazebo plugin.
  The plugin drives the robot model according to the received messages. As the robot moves, 
  the plugin publishes odometry information to odom topic.

But, what exactly constitues a velocity command or what is the format of published odometry 
message or what is odometry after all? These are the questions we try to answer in this section.
 Understanding these topics will help us implement custom velocity command and odometry 
 publishers in Part-2 of this book. Immediately, this knowledge will be useful to implement 
 a simple custom commands publisher (in the next section)."""

"""In a differential drive robot (and most wheeled robots), the wheel velocities determine
  the robot’s speed and orientation. However, robot’s (base) velocity is expressed as a single 
  entity called Twist. The differential drive controller (here a plugin) breaks the Twist 
  down to individual wheel velocities and the downstream hardware components actuate the
   wheels accordingly.

Twist has two components – linear velocity & angular velocity. Each of them is a velocity 
in the 3 dimension space (hence a vector). Unsurprisingly, the geometry_msgs/Twist message 
of cmd_vel topic is defined in the same way."""
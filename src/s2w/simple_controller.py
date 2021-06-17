#! /usr/bin/python3

import rospy
# Twist is linear and angular velocity
from geometry_msgs.msg import Point,Twist
# Position, orientation, linear velocity, angular velocity
from nav_msgs.msg import Odometry
from math import atan2
from tf.transformations import euler_from_quaternion
import random 

x=0.0
y=0.0
theta=0.0

def callback(data):
    global x
    global y
    global theta 
    pose=data


    if data.pose.pose.position.x > 9.5 or data.pose.pose.position.y < 1.5 :
        
        vel_msg.angular.z = 1
        vel_msg.linear.x = 0.2
    elif data.pose.pose.position.x or data.pose.pose.position.x > 9.5:
       
        vel_msg.angular.z = 1
        vel_msg.linear.x = 0.2
    else:
        vel_msg.angular.z=random.randint(-2,2)
        vel_msg.linear.x=random.randint(2,4)

    velocity_publisher.publish(vel_msg)
    rospy.init_node('simple_controller',anonymous=True)
    
 
 # Publisher to control the robot's speed
velocity_publisher =rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
pose_subscriber =rospy.Subscriber('/turtle1/cmd_vel',Odometry,callback)

vel_msg = Twist()
r =rospy.Rate(4)




while not rospy.is_shutdown():
    rospy.spin()
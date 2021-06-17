#! /usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import random 

def callback(data):
    vel_msg = Twist()
    pose=data
    print(data)

    if pose.x > 9.5 or pose.y < 1.5 :
        pose.theta = 4
        vel_msg.angular.z = 1
        vel_msg.linear.x = 0.2
    elif pose.x < 1.5 or pose.y > 9.5:
        pose.theta = 4
        vel_msg.angular.z = 1
        vel_msg.linear.x = 0.2
    # elif pose.y > 9:
    #     vel_msg.angular.z = -0.3
    #     vel_msg.linear.x = 0.2
    # elif pose.y < 2:
    #     vel_msg.angular.z = -0.3
    #     vel_msg.linear.x = 0.2
    else:
     
        vel_msg.angular.z=random.randint(-2,2)
        vel_msg.linear.x=random.randint(2,4)

    velocity_publisher.publish(vel_msg)

rospy.init_node('turtlebot_auto',anonymous=True)
velocity_publisher =rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
pose_subscriber =rospy.Subscriber('/turtle1/pose',Pose,callback)

while not rospy.is_shutdown():
   rospy.spin()
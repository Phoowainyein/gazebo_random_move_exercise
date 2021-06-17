#! /usr/bin/python3
from time import sleep
import rospy
from geometry_msgs.msg import Twist,Point
from turtlesim.msg import Pose

import random


rospy.init_node('kbot_simple_twist_pub')
vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)  # Velocity publisher




while not rospy.is_shutdown():
  msg = Twist()
  msg.angular.z=random.randint(-2,2)
  msg.linear.x=random.randint(2,5)
  vel_pub.publish(msg)
  sleep(10)

  

    
 

import math
from math import sin, cos, pi

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3

rospy.init_node('odometry_publisher')

odom_pub = rospy.Publisher("/cmd_vel",Twist, queue_size=50)


current_time = rospy.Time.now()
last_time = rospy.Time.now()

r = rospy.Rate(1.0)
while not rospy.is_shutdown():
    current_time = rospy.Time.now()
    move=Twist()
    move.linear.x = 0.1 
    move.angular.z = 0
    odom_pub.publish(move)

    rospy.spin()
    r.sleep()
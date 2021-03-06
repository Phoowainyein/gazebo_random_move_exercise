
import rospy

from geometry_msgs.msg import Twist
 
def publish_velocity_commands():
  # Velocity publisher
  vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
  rospy.init_node('kbot_simple_twist_pub', anonymous=True)
 
  msg = Twist()
  msg.linear.x = 5
  msg.linear.y = 0
  msg.linear.z = 0
  msg.angular.x = 0
  msg.angular.y = 0
  msg.angular.z = 0
 
  rate = rospy.Rate(10) # 10hz
  while not rospy.is_shutdown():
    vel_pub.publish(msg)
    rate.sleep()
 

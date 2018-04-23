import rospy
from geometry_msgs.msg import Twist


def main():
	pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
	rospy.init_node('talker', anonymous = True)
	rate = rospy.Rate(10)
	msg = Twist()

	msg.linear.x = 0.2
	msg.angular.z = 0.1
	while not rospy.is_shutdown():
		pub.publish(msg)
		rate.sleep()


if __name__ == '__main__':
	main()

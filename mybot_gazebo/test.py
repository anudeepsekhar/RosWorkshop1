import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
x =0

def getOdom(msg):
	global x
	x = msg.pose.pose.position.x
	y = msg.pose.pose.position.y
	z = msg.pose.pose.position.z
	#print(x)
	

def main():
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
	rospy.Subscriber('/odom',Odometry, getOdom)
	rospy.init_node('talker', anonymous = True)
	rate = rospy.Rate(10)
	msg = Twist()
	#print(x)


	#msg.linear.x = 0
	
	while not rospy.is_shutdown():
		print('x')
		print(x)
		if(x>=5):
			msg.linear.x = -0.2
		elif(x<=0.1):
			msg.linear.x = 0.2
			

		pub.publish(msg)
		rate.sleep()


if __name__ == '__main__':
	main()
	


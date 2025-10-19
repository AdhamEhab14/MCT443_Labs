#!/usr/bin/env python3
import rospy

from std_msgs.msg import String
def callback(data):
	print ("3lekom el slam " + data.data)
def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("chatter", String, callback)
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
if __name__ == '__main__':
	listener()

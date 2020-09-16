#!/usr/bin/env python3
""" Investigating receiving a message using a callback function """
from geometry_msgs.msg import PointStamped
import rospy

rospy.init_node('receive_message')

def process_point(msg):
    print(msg.header)

rospy.Subscriber("/my_point", PointStamped, process_point)

rospy.spin()

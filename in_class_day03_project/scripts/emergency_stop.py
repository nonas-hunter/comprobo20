#!/usr/bin/env python3
""" This script explores publishing ROS messages in ROS using Python """
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from std_msgs.msg import Int8MultiArray
import rospy

class EmergencyStop:
    def __init__(self):
        rospy.init_node('emergency_stop')
        self.subscriber = rospy.Subscriber('/bump', Int8MultiArray, self.callback)
    
    def callback(self, msg):
        print(msg.data)

if __name__ == "__main__":
    emergy_stop = EmergencyStop()
    rospy.spin()
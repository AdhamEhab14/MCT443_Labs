#!/usr/bin/env python3
import rospy
import actionlib
from lab3.msg import CounterAction, CounterFeedback, CounterResult # Corrected import

def callback(goal):
    feedback = CounterFeedback()
    result = CounterResult()
    rate = rospy.Rate(1)
    Final_Number = 0
    for i in range(0, goal.Limit):
        feedback.current = i + 1
        Action_Server.publish_feedback(feedback)
        Final_Number = Final_Number + 1
        rate.sleep()
    result.Limit_Reached = Final_Number
    Action_Server.set_succeeded(result)

rospy.init_node("action_server")
Action_Server = actionlib.SimpleActionServer("Counter", CounterAction, callback, auto_start=False)
Action_Server.start()
rospy.spin()

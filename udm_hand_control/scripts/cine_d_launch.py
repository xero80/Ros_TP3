#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

from udm_hand_control.srv import *

class move_finger:
    def __init__(self, group_name, l, m, n):
	self.group_name = group_name
	self.l = l
	self.m = m
	self.n = n
	rospy.init_node('move_cine_d', anonymous=True)
	moveit_commander.roscpp_initialize(sys.argv)

	group_name = group_name

	robot = moveit_commander.RobotCommander()

	scene = moveit_commander.PlanningSceneInterface()

	move_group = moveit_commander.MoveGroupCommander(group_name)
	display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory, queue_size=20)

	joint_goal = move_group.get_current_joint_values()
	joint_goal[0] = l
	joint_goal[1] = m
	joint_goal[2] = n
	move_group.go(joint_goal, wait=True)
	move_group.stop()
	current_joints = move_group.get_current_joint_values()

class move_thumb:
    def __init__(self, group_name, l, m):
	self.group_name = group_name
	self.l = l
	self.m = m
	rospy.init_node('move_cine_d', anonymous=True)
	moveit_commander.roscpp_initialize(sys.argv)

	group_name = group_name

	robot = moveit_commander.RobotCommander()

	scene = moveit_commander.PlanningSceneInterface()

	move_group = moveit_commander.MoveGroupCommander(group_name)
	display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory, queue_size=20)

	joint_goal = move_group.get_current_joint_values()
	joint_goal[0] = l
	joint_goal[1] = m
	move_group.go(joint_goal, wait=True)
	move_group.stop()
	current_joints = move_group.get_current_joint_values()

if __name__ == '__main__':
    move_finger('first_finger', 0.3, 0.2, 0.1)
    move_finger('second_finger', 0.5, 0.4, 0.2)
    move_finger('third_finger', 0.2, 0.5, 0.2)
    move_finger('fourth_finger', 0.5, 0.3, 0.2)
    move_thumb('thumb', 0.0, 0.0)







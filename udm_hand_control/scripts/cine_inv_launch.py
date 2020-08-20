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
    def __init__(self, group_name, l, m, n, o):
	self.group_name = group_name
	self.l = l
	self.m = m
	self.n = n
	self.o = o
	rospy.init_node('move_cine_inv', anonymous=True)
	moveit_commander.roscpp_initialize(sys.argv)

	group_name = group_name

	robot = moveit_commander.RobotCommander()

	scene = moveit_commander.PlanningSceneInterface()

        move_group = moveit_commander.MoveGroupCommander(group_name)
        display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)
        pose_goal = geometry_msgs.msg.Pose()
        pose_goal.orientation.w = l
        pose_goal.position.x = m
        pose_goal.position.y = n
        pose_goal.position.z = o

        move_group.set_pose_target(pose_goal)
        plan = move_group.go(wait=True)
        move_group.stop()
        move_group.clear_pose_targets()

if __name__ == '__main__':
    move_finger('first_finger', 1.0, 0.3, 0.2, 0.1)








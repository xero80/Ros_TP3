# Ros_TP3

# TP3_moveit

# Installation

For installation, clone the project in the src folder of your catkin workspace ( catkin_ws )
```
cd catkin_ws/src
git clone https://github.com/xero80/Ros_TP3.git
catkin build
cd ..
source devel/setup.bash
```

# udm_urdf

Contains the hand model 

# udm_hand_moveit_config

Makes use of the MoveIt Setup Assistant to configure the hand robot with MoveIt

# udm_hand_control

## (b) Cinematique directe

The robot hand moves its fingers according to the joint values assigned 

- Terminal #1 - launch the demo to display the hand robot in RViz

```
roslaunch udm_hand_moveit_config demo.launch
```

- Terminal #2 - Run the python file with rosrun

```
rosrun udm_hand_control cine_move_d.py  
```

- Terminal #3 - Call the service

```
rosservice call /udm_service "joint_goal1:
  data: 0.3
joint_goal2:
  data: 0.2
joint_goal3:
  data: 0.1
group:
  data: 'first_finger'"
```

change the group data to : second_finger, third_finger, fourth_finger to move the other fingers; then for thumb (has only 2 joints): 

```
rosservice call /udm_service "joint_goal1:
  data: 0.0
joint_goal2:
  data: 0.0
group:
  data: 'thumb'"
```

## (c) Cinematique inverse

The robot hands plans a path to the pose goal assigned 

- Terminal #1 - launch the demo to display the hand robot in RViz

```
roslaunch udm_hand_moveit_config demo.launch
```

- Terminal #2 - Run the python file with rosrun

```
rosrun udm_hand_control cine_move_inv.py  
```

- Terminal #3 - Call the service

```
rosservice call /cine_service "orientation:
  data: 1.0
posex:
  data: 0.1
posey:
  data: 0.4
posez:
  data: 0.2
group:
  data: 'first_finger'"
```

# Launch 

Launchfile for cinematique directe

- cine_direct.launch

## View in Rviz 

```
roslaunch udm_hand_control cine_direct.launch
```

# ROS_TP_Cours 2

# Dependencies

rospy, roscpp, urdf, std_msgs, geometry_msgs, sensor_msgs

# 1st part

Creation of xml file 
  - urdf_cylinder.urdf
  - box.urdf
  - sphere.urdf
  - mesh.urdf

The visual field define what we see on the simulator 
The geometry is the box, cylinder, mesh & sphere depending on the requirement


# 2nd part

Two principle fields that describe the geometry of a robot: links & joints

# 3rd part

The type for joint is revolute
The limits are fixed by using for eg
```
<limit effort ="1000.0" lower="-2.0" upper="0.05" velocity="0.5"/>
```
 Define in which axis it moves
```
<axis xyz="x y z>
```

# View in Rviz

 - visualize_urdf.launch
 
```
roslaunch udm_urdf visualize_urdf.launch
```

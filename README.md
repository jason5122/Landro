# Landro

## Building
To build a package:
```
colcon build --packages-select [package_name]
```
The packages are:
- spawner: Spawns a robot into the world.
- controller: Estimates the robot's location and handles the robot's movment.

## Running
First, source the setup script. This must also be done after building any changes. You'll get a "Package 'package_name' not found" error otherwise:
```
source install/setup.bash
```

To run the spawner (which launches the Gazebo world):
```
ros2 launch spawner gazebo_world.launch.py
```

To run the controller:
```
ros2 launch controller controller_estimator.launch.py
```

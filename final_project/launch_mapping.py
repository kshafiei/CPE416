# launch/launch_bump_and_go1.py

import launch
from launch import LaunchDescription
from launch.actions import LogInfo, DeclareLaunchArgument, IncludeLaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    return LaunchDescription([

        # Launch gobilda.launch.py
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                'install/gobilda_robot/share/gobilda_robot/launch/gobilda.launch.py'
            ),
            launch_arguments={'namespace': 'final_mapping'}.items()
        ),

        # Launch rplidar_a1_launch.py
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                'src/rplidar_ros/launch/rplidar_a1_launch.py'
            ),
            launch_arguments={'namespace': 'final_mapping'}.items()
        ),

        # Launch camera.launch.py
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                '/opt/ros/humble/share/depthai_ros_driver/launch/camera.launch.py'
            ),
            launch_arguments={'namespace': 'final_mapping'}.items()
        ),

        # Launch slam_toolbox_online_async_launch.py
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                '/opt/ros/humble/share/slam_toolbox/launch/online_async_launch.py'
            ),
            launch_arguments={'namespace': 'final_mapping'}.items()
        ),

        # Launch ekf.launch.py
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                '/opt/ros/humble/share/robot_localization/launch/ekf.launch.py'
            ),
            launch_arguments={'namespace': 'final_mapping'}.items()
        ),
    ])


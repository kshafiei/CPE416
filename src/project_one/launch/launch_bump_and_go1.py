# launch/launch_bump_and_go1.py

import launch
from launch import LaunchDescription
from launch.actions import LogInfo, DeclareLaunchArgument, IncludeLaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    return LaunchDescription([

        # Launch gobilda.launch.py with the specified namespace
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                # Specify the absolute or relative path to the gobilda.launch.py file
                '../../../install/gobilda_robot/share/gobilda_robot/launch/gobilda.launch.py'
            ),
            launch_arguments={'namespace': 'Bump_and_go1'}.items()
        ),

        # Launch rplidar_a1_launch.py with the specified namespace
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                # Specify the absolute or relative path to the gobilda.launch.py file
                '../../../src/rplidar_ros/launch/rplidar_a1_launch.py'
            ),
            launch_arguments={'namespace': 'Bump_and_go1'}.items()
        ),

        # Launch the Bump_and_go executable from the project_one package
        Node(
            package='project_one',
            executable='bump_and_go',
            name='Bump_and_go_node',
            namespace='',
        ),

    ])


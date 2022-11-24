# Copyright 2022 Ross Lunan (ARLunan/Rossbots)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# @author Ross Lunan (arlunan@ieee.org)

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
import launch_ros.actions

def generate_launch_description():

    pkg_depthai_viz=get_package_share_directory('depthai_viz')

    rviz2_config=PathJoinSubstitution(
        [pkg_depthai_viz,'rviz','default.rviz']
    )
    
    rviz2_node=launch_ros.actions.Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2_node',
            arguments=['-d',rviz2_config],
            output='screen')
        
    ld=LaunchDescription()    
    ld.add_action(rviz2_node)
    return ld

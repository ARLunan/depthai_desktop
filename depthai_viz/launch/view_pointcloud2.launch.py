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
from launch import LaunchDescription, launch_description_sources
from launch.actions import IncludeLaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition, LaunchConfigurationEquals, LaunchConfigurationNotEquals 
import launch_ros.actions
import launch_ros.descriptions

def generate_launch_description():
    depthai_examples_path = get_package_share_directory('depthai_examples')
    # add lines 13 - 283
    # Line 300-330
    stereo_node=launch=launch_ros.actions.Node(
        package='depthai_examples', executable='stereo_inertial_node',
        output='screen'
        parameters=[{},
     
        
    ])  
    
    # Line 341-464

    ld=LaunchDescription()    
    return ld
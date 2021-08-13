import os
from setuptools import setup
from glob import glob

package_name = 'controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jason',
    maintainer_email='jjhan@vassar.edu',
    description='Controls the motion of a robot.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'robot_controller = controller.robot_controller:main',
          'robot_estimator = controller.robot_estimator:main'
        ],
    },
)

#!/usr/bin/env python

from distutils.core import setup


setup(
    name='ms5837',
    version='1.0',
    description='Interfaces with MS5837-30BA and MS5837-02BA waterproof '
                'pressure and temperature sensors',
    author='Blue Robotics',
    url='https://github.com/bluerobotics/ms5837-python',
    packages=['ms5837'],
    install_requires=['smbus'],
)

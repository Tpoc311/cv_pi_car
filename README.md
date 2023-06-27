# CV pi car

<p align="center">
    <img src="Images/hardware/overview.jpg" width="50%" alt="Images/hardware/overview.jpg"/>
</p>

<p align="center">
    <img src="Images/hardware/demo.gif" width="50%" alt="Images/hardware/overview.jpg"/>
</p>

Here is project of my simple robocar presented. The main idea is to get images from Raspberry Pi camera, recognize
simulated road lane and make the wheeled base follow the lane.

## Structure of the robocar

Basically the project consists of two main parts - hardware and software. To learn more about each of them, check
following readmes:

* Hardware part - [README_hardware](README_hardware.md).
* Software part - [README_software](README_software.md).

## What I used to connect to robocar and start it

After installing Raspberry OS we need to enable ssh. Then configure VNC server to connect with monitor via your PC or
laptop [1].
After that all we need is to upload `drivingModule.ino` to Arduino and start `main.py`.

If you have any questions about the project you are always welcome to contact me via email:
vadim.kolesnikov.311@gmail.com.

## Sources

1. [Configure VNC server](https://www.tomshardware.com/how-to/install-vnc-raspberry-pi-os).

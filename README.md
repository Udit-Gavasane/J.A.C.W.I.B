# J.A.C.W.I.B
## Authors/Developers : Udit Gavasane, Rohan Tergaonkar, Amod Sahasrabudhe
J.A.C.W.I.B (Just Another Car With Intelligent Brain) is a lane keeping, self driving car built using Raspberry Pi and OpenCV.

![JACWIB](https://github.com/Udit-Gavasane/J.A.C.W.I.B/blob/master/IMG_20200408_124248.jpg)

This project builds a self driving car which is based on the technique of lane detection using OpenCV. The main processing unit of the car is Raspberry Pi. It makes use of camera module to capture video stream and send it wirelessly to the terminal of the computer executing the program. The computer carries out the task of lane detection and calculates the steering angle. This steering angle is again transferred back to the Raspberry Pi. A client model on the Raspberry Pi gives direction to the car based on the steering angle.




### About the files


#### Computer/
**_computer_server.py_** : 
1. Video streaming from raspi to computer
2. Calculating the steering angle
3. Transferring the steering angle using socket

#### Raspberry Pi/
**_raspi_client_1.py_**:
1. Receive steering angle from host computer
2. Give steering angle to Raspberry Pi to enable driving

**_raspi_client_2_**:
1. Send video stream in jpeg format to the host computer
 

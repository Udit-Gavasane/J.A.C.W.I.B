# J.A.C.W.I.B
## Authors/Developers : Amod Sahasrabudhe, Rohan Tergaonkar, Udit Gavasane
J.A.C.W.I.B (Just Another Car With Intelligent Brain) is a lane keeping, self driving car built using Raspberry Pi and OpenCV.

![JACWIB](https://github.com/Udit-Gavasane/J.A.C.W.I.B/blob/master/JACWIB.jpg)

This project builds a self driving car which is based on the technique of lane detection using OpenCV. The main processing unit of the car is Raspberry Pi. It makes use of camera module to capture video stream and send it wirelessly to the terminal of the computer executing the program. The computer carries out the task of lane detection and calculates the steering angle. This steering angle is again transferred back to the Raspberry Pi. A client model on the Raspberry Pi gives direction to the car based on the steering angle.




### About the files


#### Computer/
**_computer_server.py_** :<br />
&emsp; &emsp;  &emsp; &emsp;1. Video streaming from raspi to computer<br />
&emsp; &emsp;  &emsp; &emsp;2. Calculating the steering angle<br />
&emsp; &emsp;  &emsp; &emsp;3. Transferring the steering angle using socket<br />


#### Raspberry Pi/
**_raspi_client_1.py_**:<br />
&emsp; &emsp;  &emsp; &emsp;1. Receive steering angle from host computer<br />
&emsp; &emsp;  &emsp; &emsp;2. use steering angle to enable driving<br />

**_raspi_client_2.py_**:<br />
&emsp; &emsp;  &emsp; &emsp;1. Send video stream in jpeg format to the host computer<br />



### How to drive
1. **Connection:** Connect Raspberry Pi to Host Computer using Remote Desktop Connection to control the Raspberry Pi via Host Computer.
2. **Testing:** Execute the `test_drive.py` program on Raspberry Pi terminal to check the throttle and direction of the car.
3. **Initialise Server:** On the host computer, execute `computer_server.py`.
4. **Initialise Client:** On the Raspberry Pi simultaneously execute 2 client programs i.e. `raspi_client_1.py` and `raspi_client_2.py` respectively. At this point, the host computer will start calculating steering angle based on the video stream received by `raspi_client_2.py` from the Raspberry Pi and will send them back through socket which will be received by `raspi_client_1.py` client.
5. **Self-Driving in Action:** Based on the steering angle, the program `raspi_client_1.py` will give instructions to the GPIO pins of the Raspberry Pi for running the motors (motors are used to drive the wheels of the car). Thus the car will start driving autonomously in the designated lanes.

##### Check out our article for detailed information on this project.&emsp;[J.A.C.W.I.B](https://medium.com/@amod.jacwib/j-a-c-w-i-b-autonomous-car-9c42bc732279)

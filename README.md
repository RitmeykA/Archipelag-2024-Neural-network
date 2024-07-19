# Archipelag-2024-Neural-network
This project was created during a competition held July 13 - 17 called Archipelag 2024. The following tools were used to fulfill the terms of reference: Agisoft Metashape, Roboflow, Python and some of its libraries. The competition involved locating an object of interest on the range and sending a ground robot to it. Such technology can be applied in life, in case of emergencies.
In total, the test is divided into 4 phases:
1. Drone overflight and photographing the terrain. Execution time: 10 minutes. Site dimensions (8x8 + 3m, 3 + 2m).
2. After the drone flight, we get a photo of the terrain and a text file with coordinates where the photo was taken. The neural network should process the entire volume of images and use the trained model to detect the object of interest. In the output we should get approximate coordinates of the object of interest (+- 0.5m).
3. The obtained coordinates we put into the code of the ground robot, which builds the shortest route bypassing obstacles and follows the object of interest.
Geoscan drone, model Pioneer, is used as equipment. The ground robot is assembled from improvised means, using a Raspberry Pi microcomputer.
Let's go through the composition of the repository.
- The Libraries folder contains libraries that are used in the drone and ground robot (geobot) code. 
- The Neural networks folder contains drone photos, neural network code and neural network weights file (object of interest).
- The Orthophoto folder contains arena files without the object of interest. It is intended for determining the coordinates of obstacles. And because the files are too big, I decided to upload them to google drive via a link: https://drive.google.com/drive/folders/1v_tzjoFcnryCfZa7w8-7ODgaeeNum7K9?usp=sharing
- The file geobot-robot.py contains the code for the ground robot.

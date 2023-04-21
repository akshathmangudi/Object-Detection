# Repo Revision

This repo was previously in use for real-time drowsiness detection for truck drivers. 
The current purpose of this repo has been shifted to object detection using a webcam using OpenCV. 

The first half of the project deals with face detection using OpenCV. 
To run that code: Follow Steps 0, 1 and 2. 
Step 3: Run the following code. 


For taking a picture, press SPACE. 
For terminating the program, press ESC. 

This project deals with object detection using OpenCV and MobileNetSSD. 
The logic of the code is to loop over each frame on the webcam and detect common objects such as chair, person, etc. 

The output of the detection is shown on a box. For running the code: 

Step 0: Create a directory and clone it. 

Step 1: Install the necessary dependancies. For this program, it involves:
1. OpenCV
2. imutils
3. matplotlib
4. Numpy

Step 2: Check if your video devices are connected. 

Step 3: To run the model, run the following code. 

"--prototxt" is the prototxt file that has information related to the machine learning model trained
"--model" has the necessary information needed for detection. These two work hand in hand. 


For termination of the program, press W. 

Step 4: For anything else, type in the following code.

Project by Akshath Mangudi (2023)

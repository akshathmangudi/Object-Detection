# Object Detection

## Table of Contents
* <a href="">Initializing</a>
* <a href="">Dependencies</a>
* <a href="">Running the model </a>
* <a href="">Help</a>

NOTE: This repo was previously in use for real-time drowsiness detection for truck drivers. 
The current purpose of this repo has been shifted to object detection using a webcam using OpenCV. 

The first half of the project deals with face detection using OpenCV. 
To run that code: Follow Steps 0, 1 and 2. 
Step 3: Run the following code. 

```bash
python face_detect.py
```

For taking a picture, press SPACE. 
For terminating the program, press ESC. 

This project deals with object detection using OpenCV and MobileNetSSD. 
The logic of the code is to loop over each frame on the webcam and detect common objects such as chair, person, etc. 

Create a virtual environment in order to avoid conflict with global versions of packages.

## Initalizing
```shell
mkdir ~/Desktop/opencv_project
cd ~/Desktop/opencv_project
```

## Dependencies
1. OpenCV
2. imutils
3. matplotlib
4. Numpy

```shell
pip install opencv-python
pip install opencv-contrib
pip install imutils
pip install matplotlib
pip install numpy
```

## Checking video cameras (not necessary)
```shell
system_profiler SPCameraDataType
system_profiler SPCameraDataType | grep "^    [^ ]" | sed "s/    //" | sed "s/://"
```

## Running the model

```shell
python object_detection.py --prototxt deploy.prototxt.txt --model caffedep.caffemodel
```

Arguments: 
1. --prototxt: is the prototxt file that has information related to the machine learning model trained
2. --model: has the necessary information needed for detection. These two work hand in hand. 

For termination of the program, press W. 

## Help
```shell
python object_detection.py --help 
```

Project by Akshath Mangudi (2023)

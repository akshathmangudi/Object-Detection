# Repo Revision

This repo was previously in use for real-time drowsiness detection for truck drivers. 
The current purpose of this repo has been shifted to object detection using a webcam using OpenCV.

For taking a picture, press SPACE. 
For terminating the program, press ESC. 

This project deals with object detection using OpenCV and MobileNetSSD. 
The logic of the code is to loop over each frame on the webcam and detect common objects such as chair, person, etc. 

Create a virtual environment in order to avoid conflict with global versions of packages.

Step 0: Clone the repository. 
```bash
$ git clone https://github.com/akshathmangudi/Object-Detection.git
$ cd Object-Detection/ 
```

Step 1: Install the necessary dependencies. Dependencies can either be installed manually (list is in the requirements)
or the following command below can be used to install all the dependencies in one go. 
```bash
$ pip install -r requirements.txt
```

Step 2: Check if your video devices are connected and are working.
```bash
$ system_profiler SPCameraDataType
$ system_profiler SPCameraDataType | grep "^    [^ ]" | sed "s/    //" | sed "s/://"
```

Step 3a: For face detection, run this code.
```bash
$ python face_detect.py
````

Step 3b: For object detection, run this code with the arguments provided below.
```bash
$ python object_detection.py --prototxt deploy.prototxt.txt --model caffedep.caffemodel
```

"--prototxt" is the prototxt file that has information related to the machine learning model trained
"--model" has the necessary information needed for detection. These two work hand in hand. 

For termination of the program, press W. 

Step 4: For anything else, type in the following code.
```bash
$ python object_detection.py --help 
```

Project by Akshath Mangudi (2023)
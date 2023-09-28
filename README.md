# Repo Revision

This repo was previously in use for real-time drowsiness detection for truck drivers. 
The current purpose of this repo has been shifted to object detection using a webcam using OpenCV.

This project deals with object detection using OpenCV and MobileNetSSD. 
The logic of the code is to loop over each frame on the webcam and detect common objects such as chair, person, etc.

### Cloning the repo
```bash
$ git clone https://github.com/akshathmangudi/Object-Detection.git
$ cd Object-Detection/ 
```

## Table of Contents
* <a href=""> Creating a virtualvenv </a>
* <a href=""> Installing dependencies </a>
* <a href=""> Checking condition of webcam / video devices </a>
* <a href=""> Face detection </a>
* <a href=""> Object detection </a>
* <a href=""> Help </a>


### Creating a venv
For Python 3.6+ users: 
```shell
python -m venv /path/to/virtualenv
```
For activation of virtualenv:
bash/zsh: 
```bash 
$ source <venv>/bin/activate
```
fish: 
```shell
$ source <venv/bin/activate.fish
```
cmd.exe: 
```shell
C:\> <venv>\Scripts\activate.bat
```
```shell
PowerShell: 
PS C:\> <venv>\Scripts\activate.ps1
```
For conda users, the following commands are to be sequentially passed into your terminal: 

```bash
conda -V
conda update conda
conda create -n <envname> python=x.x anaconda
conda activate <envname>
```
For deactivation: 
```bash
conda deactivate
```

### Installing dependencies
```bash
$ pip install -r requirements.txt
```

### Check condition of video devices
```bash
$ system_profiler SPCameraDataType
$ system_profiler SPCameraDataType | grep "^    [^ ]" | sed "s/    //" | sed "s/://"
```

### Face detection
```bash
$ python face_detect.py
````

### Object detection
```bash
$ python object_detection.py --prototxt deploy.prototxt.txt --model caffedep.caffemodel
```

"--prototxt" is the prototxt file that has information related to the machine learning model trained
"--model" has the necessary information needed for detection. These two work hand in hand. 

For termination of the program, press W. 

### Help
```bash
$ python object_detection.py --help 
```

For taking a picture, press SPACE. 
For terminating the program, press ESC.

Project by Akshath Mangudi (2023)
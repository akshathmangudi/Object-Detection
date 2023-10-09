This folder inside Object-Detection utilizes Ultralytics' YOLOv8 model which can be used for object detection, 
image segmentation on versatile inputs like a webcam, video input or an image. 

Our first part of this repository will be to implement an object detection algortithm in real time while the second part
will be to implement a custom object detection algorithm using a video input. 

Second-Half:

To use the repository:
1. Install all the dependencies and download the dataset and store it under data/ 
    1. <a href="https://storage.googleapis.com/openimages/v6/oidv6-train-annotations-bbox.csv">Train</a>
    2. <a href="https://storage.googleapis.com/openimages/v5/validation-annotations-bbox.csv">Validation</a>
    3. <a href="https://storage.googleapis.com/openimages/v5/test-annotations-bbox.csv">Test</a>
2. run prepare_data/create_image_file.py. This will be used later on for our image/label split. 
3. run downloader.py with the following arguments: 
```shell
python downloader.py $IMAGE_LIST_FILE (path of image list file) --download_folder=$DOWNLOAD_FOLDER (where to download imgs)
```
4. run prepare_data/yolo_format.py. 
5. Now, our data will be split into train, validation and testing, with each folder split into two subfolders images
and labels. This will be very cruical as we will use our yolo model to train on these images and labels. 
6. Run the following command to train the model
```shell
yolo detect train data=config.yaml model='yolov8n.pt' epochs=100
```
7. After this, our model will create a runs folder with weights best.pt and last.pt. This will be used for our testing. 
We will use a video input for our testing (video/alpaca_cat.mp4). Run this specific command to test the model:
```shell
yolo task=detect mode=predict model=(relative path of weights\best.pt) show=True conf=0.5 source='video\alpaca_cat.mp4'
```

If you would like to save the segmented images to a folder, add a 'save_crop=True' argument to step 7. If you have any 
queries or if you would like to collaborate, please let me know at akshathmangudi@gmail.com
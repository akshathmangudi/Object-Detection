import cv2 # Importing the OpenCV module

# Importing the required cascade file for face detection
haar_cas = cv2.CascadeClassifier ('/Users/Aksha/PycharmProjects/drowsy-detect/haar cascade/haarcascade_frontalface_default.xml')

# Captures the webcam
video_capture = cv2.VideoCapture(0)

img_counter = 0

while True:
    # Capture each frame. As a webcam is used, the program will not run out of frames
    ret, frame = video_capture.read()
    # Converting to gray -> Almost all image manipulations are done using grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Keyboard input for either exiting the program or taking a photo.
    k = cv2.waitKey(1)
    # Detecting the faces using the cascade file
    face = haar_cas.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw the rectangle wherever the face is found.
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # The top caption of the program
    cv2.imshow("Akshath Mangudi", frame)

    if k % 256 == 27: # ESC button -> For exiting the program
        break
    elif k % 256 == 32: # ENTER button -> For taking a photo
        img_name = "facedetection-{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1


# Releasing all windows.
video_capture.release()
cv2.destroyAllWindows()
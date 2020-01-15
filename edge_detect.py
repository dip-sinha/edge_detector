# OpenCV program to perform Edge detection in real time
# import libraries of python OpenCV
# where its functionality resides
import cv2
import glob
import os
# np is an alias pointing to numpy library
import numpy as np
import File_name_gen as fng
# capture frames from a camera
cap = cv2.VideoCapture(0)

# loop runs if capturing has been initialized
while (1):

    # reads frames from a camera
    ret, frame = cap.read()

    # converting BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of red color in HSV
    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])

    # create a red HSV colour boundary and
    # threshold HSV image
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Display an original image
    cv2.imshow('Original', frame)
    # font
    font = cv2.FONT_HERSHEY_SIMPLEX

    # org
    org = (50, 50)

    # fontScale
    fontScale = 1

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 2
    # finds edges in the input image image and
    # marks them in the output map edges
    edges = cv2.Canny(frame, 100, 200)
    edges = cv2.putText(edges,'press spacebar to save image', org, font,fontScale, color, thickness, cv2.LINE_AA)
    # Display edges in a frame
    cv2.imshow('Edges', edges)
    # TO Find the last file name saved and continue from there!
    # fileName = Generate_filename()
    # Wait for Esc key to stop
    k = cv2.waitKey(1) & 0xFF
    if k == 32: # space bar to save image
        name = fng.Generate_filename()
        filename = str(name)
        cv2.imwrite("image/"+filename+".jpg", edges) # saving image
        break
    if k == 27:
        break

# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()

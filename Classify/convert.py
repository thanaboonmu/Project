import cv2
import numpy as np
import argparse
import cv2
import os, os.path
import scipy.misc
image_dir = "images"
image_path_list = []
valid_image_extensions = [".jpg", ".jpeg", ".png", ".tif", ".tiff",".JPG",".TIF"]
valid_image_extensions = [item.lower() for item in valid_image_extensions]
for file in os.listdir(image_dir):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_image_extensions:
        continue
    image_path_list.append(os.path.join(image_dir, file))

a = 0
for imagePath in image_path_list:
    img = cv2.imread(imagePath)
    if img is not None:
        sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
        # cv2.imshow(imagePath, sobelx)
        name = str(a) + ".png"
        # scipy.misc.toimage(sobelx,cmin=1.0,cmax=3.0).save(name)
        scipy.misc.toimage(sobelx,cmin=1.0,cmax=3.0).save(name)
        # cv2.imwrite(name,img)
        print (a)
        a += 1
        continue
    elif img is None:
        print ("Error loading: " + imagePath)
        #end this loop iteration and move on to next image
        continue
    key = cv2.waitKey(0)
    if key == 27: # escape
        break
cv2.destroyAllWindows()

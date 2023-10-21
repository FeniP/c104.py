import cv2
import numpy as np
black=np.ones([400,600])
black[200:400,200:400]=0
cv2.imshow("aabds",black)
cv2.waitKey(0)
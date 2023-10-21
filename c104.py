import cv2 
img= cv2.imread("C:/Users/mahif/Downloads/PRO-104-OpenCV-Image-Assets-main/PRO-104-OpenCV-Image-Assets-main/butterfly.jpg")
cv2.putText(img,"asddf",(220,20),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=2,color=(255,0,255))
cv2.imshow("abc",img)
greyimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("abbc",greyimg)
cv2.waitKey(0)
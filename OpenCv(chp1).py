import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# from 

'''CV_image = cv2.imread("coca.png",1);
print(CV_image)
print("Size: ",CV_image.shape)
print("Datatype: ",CV_image.dtype)
#plt.imshow(CV_image)
#plt.imshow(CV_image, cmap='gray')
reverse_img = CV_image[:,:,::-1]
plt.imshow(reverse_img)'''


'''
#Split image in B,G,R Components.
CV_image = cv2.imread("coca.png",1);
b,g,r=cv2.split(CV_image)

#Show the channels
plt.figure(figsize=[20,5])
plt.imshow(r, cmap='gray');plt.title("Red Channel");
plt.imshow(g, cmap='gray');plt.title("Green Channel");
plt.imshow(b, cmap='gray');plt.title("Blue Channel");


#Merging individual channels into BGR image.
image_merge = cv2.merge((b,g,r))
plt.imshow(image_merge[:,:,::-1]);plt.title("Merged Output");

cv2.imwrite("Rohit.png",CV_image)'''



#Displaying windows for 8sec 
CV_image = cv2.imread("coca.png",1);
window1=cv2.namedWindow("W1")
cv2.imshow(window1,CV_image)
cv2.waitKey(8000)
cv2.destroyWindow(window1)

#Displaying windows for 8sec 
CV_image = cv2.imread("check.jpg",1);
window2=cv2.namedWindow("W2")
cv2.imshow(window1,CV_image)
cv2.waitKey(8000)
cv2.destroyWindow(window2)

#Displaying windows until a key is pressed.
CV_image = cv2.imread("coca.png",1);
window3=cv2.namedWindow("W3")
cv2.imshow(window1,CV_image)
cv2.waitKey(0)
cv2.destroyWindow(window3)


#Displaying windows until a particular key is pressed.
CV_image = cv2.imread("check.jpg",1);
window4=cv2.namedWindow("W4")

Alive = True
while(Alive):
    cv2.imshow(window4,CV_image)
    keypress = cv2.waitKey(1)
    if(keypress == ord('r')):
        Alive = False
cv2.destroyWindow(window4)
cv2.destroyAllWindows()















 
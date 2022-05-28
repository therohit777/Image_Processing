# OpenCv(Chp1-ImProcessing Concepts:)

'''
   1. Some important modules:

        import cv2 (Computer Vision module)
        import matplotlib (Used for ploting graphs)
        import numpy as np (Used for making arrays)
        import matplotlib.pyplot as pit ()
        from Ipython.display import Image
        (used for importing images)
      
      


    2. Reading image as gray scales 
       (i.e.reading colors which are shades of gray.)

            i. Cv2.imread(path,flag): 
                    path is the path of image, 
                    Flag:
                        0 - specifies to load an image in 
                            grayscale mode.
                        1 - specifies to load a color image.
                       -1 - specifies to load an image as such 
                            including alpha channel.

        NOTE:
        Printing data in 2D numpy Array.
             CV_image = cv2.imread("check.jpg",0);
             print(CV_image)




    3.Printing the size and datatype 
      of Image.

        Snippets:
            print("Size: ",CV_image.shape)
            print("Datatype: ",CV_image.dtype)




    4. Display image using matplotlib 
       function:

        Snippets:
            plt.imshow(CV_image)
            plt.imshow(CV_image,cmap='gray')

            where,
            cmap: It is a color map, where we 
                  have assigned a gray to get 
                  output in gray scale color.





    5. To reverse COLOR channels in OpenCV.      
       Our normal color follows the convention of RGB
       whreas our OpenCV follows the reverse convention
       that is BGR.

       #So in order to reverse it:
                 Reverse = CV_image[:,:,::-1]




    6. Splitting and Merging Color Channels:
      
SNIPPETS:
#Split image in B,G,R Components.
CV_image = cv2.imread("coca.png",1);
b,g,r=cv2.split(CV_image)

#Show the channels
plt.figure(figsize=[20,5])
plt.Subplot(141);plt.imshow(r, cmap='gray');plt.title("Red Channel");
plt.Subplot(142);plt.imshow(g, cmap='gray');plt.title("Green Channel");
plt.Subplot(143);plt.imshow(b, cmap='gray');plt.title("Blue Channel");

#Merging individual channels into BGR image.
image_merge = cv2.merge((b,g,r))
plt.imshow(image_merge[:,:,::-1]);plt.title("Merged Output");


where,
     plt.title(""): provide titles to our plots.
     plt.subplot(): It helps in creating subplots.
     cv2.split(CV_image): splits image in B,G,R components.
     cv2.merge((b,g,r)): merges different components of image
                         to form the image.


    

     7.Conversion to different color spaces.
       
          convert = cv2.cvtColor(src , code)
        
          where,
               src = CV_image, the image we read.
               code = cv2.COLOR_BGR2RGB
                      cv2.COLOR_BGR2HSV


     8.Saving a Image.
       cv2.imwrite("Rohit.png",CV_image)
       where:
            first parameter: imagename 
            second parameter: image.


     9.Using ImShow() of OpenCV to display 
       a image.


        SNIPPETS:
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










      
'''
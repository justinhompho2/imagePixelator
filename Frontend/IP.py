# import cv2
# import numpy as np
# from PIL import Image

def testLink():
    print("Lorem ipsum...")


# def Pixelator2(img_doc, scale):
#     img = Image.open(img_doc)
#     imgSmall = img.resize((scale, scale))
#     result = imgSmall.resize(img.size,Image.NEAREST)
#     return result

# class ImagePixelator:
#     def _init_(self, image, client):
#         self.image = image
#         self.client = client
#         pass

#     ## Module to enable getting requests and handling requests between front and backend
#     def InteractiveModule():
#         ## Implement this later. Not sure how would the backend work with the frontend yet.
#         pass

#     ## ContourDetector for the image
#     def ContourDetector(self):
#         ## The following is a basic sample about how to do contour detecting in Opencv. 
#         ## Source: https://learnopencv.com/contour-detection-using-opencv-python-c/

#         # Convert the image to grayscale. Very important for contour detection to work.
#         img_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
#         ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
#         # visualize the binary image
#         cv2.imshow('Binary image', thresh)
#         cv2.waitKey(0)
#         cv2.imwrite('image_thres1.jpg', thresh)
#         cv2.destroyAllWindows()

#         # detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
#         contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
                                            
#         # draw contours on the original image
#         image_copy = self.image.copy()
#         cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
                        
#         # see the results
#         cv2.imshow('None approximation', image_copy)
#         cv2.waitKey(0)
#         cv2.imwrite('contours_none_image1.jpg', image_copy)
#         cv2.destroyAllWindows()
#         pass

#     ## The very basic image pixelator. Credit to https://www.youtube.com/watch?v=8g2Sgjtm4y4
#     ## image: the image to pixelate
#     ## pixelsize: the size of the pixels
#     def Pixelator(self, pixelsize: int) -> np.ndarray:

#         height, width = self.image.shape[0:2]
        
#         new_height, new_width = (height // pixelsize, width // pixelsize)
#         img_temp = cv2.resize(self.image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
#         img_out = cv2.resize(img_temp, (width, height), interpolation=cv2.INTER_NEAREST)
#         #cv2.imshow("pixelated_image", img_out)

#         return img_out
    
#     ## Rotate the image based on the user command
#     ## rotate_command: left or right
#     def Rotator(self, rotate_command: str):
#         img_out = self.image.copy()
#         if rotate_command == "right":
#             img_out = cv2.rotate(img_out, cv2.ROTATE_90_CLOCKWISE)
#         elif rotate_command == "left":
#             img_out = cv2.rotate(img_out, cv2.ROTATE_90_COUNTERCLOCKWISE)
#         return img_out
    
#     ## Resize the image based on the user input parameters
#     def Resizer(self):
#         ## todo: implement this based on user command
#         ## not sure how would the actual page be. Implement later.
#         pass

#     ## Crop the image based on the user input parameters
#     def Cropper():
#         pass

#     ## History tracker to enable undo the changes.
#     def HistoryTracker():
#         pass

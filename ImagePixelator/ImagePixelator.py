import cv2
import numpy as np
from PIL import Image

def Pixelator2(img_doc, pixel_size):
    img = Image.open(img_doc)
    width, height = img.size
    new_width, new_height = (width // pixel_size, height // pixel_size)
    imgSmall = img.resize((new_width, new_height))
    result = imgSmall.resize(img.size,Image.NEAREST)
    return result

class ImagePixelator:
    def _init_(self, image, client):
        self.image = image
        self.client = client
        pass

    ## Module to enable getting requests and handling requests between front and backend
    ## the request is supposed to be a simple command: Pixelate, Resize, Crop, 
    def InteractiveModule(request:str):
        ## Implement this later. Not sure how would the backend work with the frontend yet.
        ##pr
        pass

    ## ContourDetector for the image
    ## https://dontrepeatyourself.org/post/edge-and-contour-detection-with-opencv-and-python/
    def ContourDetector(self):
        # read the image
        image = cv2.imread('shape.jpg')
        
        # Convert the image to grayscale. Very important for contour detection to work.
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

        blurred = cv2.GaussianBlur(img_gray, (3, 3), 0)
        edged = cv2.Canny(blurred, 10, 100)

        # define a (3, 3) structuring element
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

        # apply the dilation operation to the edged image
        dilate = cv2.dilate(edged, kernel, iterations=1)

        # find the contours in the dilated image
        contours, _ = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        image_copy = image.copy()
        # draw the contours on a copy of the original image
        cv2.drawContours(image_copy, contours, -1, (0, 255, 0), 2)
        print(len(contours), "objects were found in this image.")

        return contours
    
    ## The very basic image pixelator. Credit to https://www.youtube.com/watch?v=8g2Sgjtm4y4
    ## image: the image to pixelate
    ## pixelsize: the size of the pixels
    def Pixelator(self, pixelsize: int, contourArea: np.array) -> np.ndarray:

        height, width = self.image.shape[0:2]
        
        new_height, new_width = (height // pixelsize, width // pixelsize)
        img_temp = cv2.resize(self.image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
        img_out = cv2.resize(img_temp, (width, height), interpolation=cv2.INTER_NEAREST)
        if len(contourArea) == 0:
            return img_out
        
        img_out_1 = self.image.copy()
        for i in range(new_width):
            for k in range(new_height):
                i_index = i*pixelsize
                k_index = k*pixelsize
                if cv2.pointPolygonTest(contourArea, (i_index, k_index), True) > 0 or \
                    cv2.pointPolygonTest(contourArea, (i_index+pixelsize-1, k_index), True) > 0 or \
                    cv2.pointPolygonTest(contourArea, (i_index, k_index+pixelsize-1), True) > 0 or \
                    cv2.pointPolygonTest(contourArea, (i_index+pixelsize-1, k_index+pixelsize-1), True) > 0:
                    img_out_1[k_index:k_index+pixelsize, i_index:i_index+pixelsize] = img_out[k_index:k_index+pixelsize, i_index:i_index+pixelsize]

        #cv2.imshow("pixelated_image", img_out)

        return img_out_1
    
    ## Rotate the image based on the user command
    ## rotate_command: left or right
    def Rotator(self, rotate_command: str):
        img_out = self.image.copy()
        if rotate_command == "right":
            img_out = cv2.rotate(img_out, cv2.ROTATE_90_CLOCKWISE)
        elif rotate_command == "left":
            img_out = cv2.rotate(img_out, cv2.ROTATE_90_COUNTERCLOCKWISE)
        return img_out
    
    ## Resize the image based on the user input parameters
    def Resizer(self, newSize: tuple):
        ## todo: implement this based on user command
        ## not sure how would the actual page be. Implement later.
        newimage = cv2.resize(self.image, newSize)
        return newimage
        

    ## Crop the image based on the user input parameters
    def Cropper(self, startindex, newsize):
        height, width = self.image.shape[0:2]
        x, y = startindex
        h, w = newsize
        crop_img = self.image[x:max(x+h, height), y:max(y+h, width)]
        return crop_img

    ## History tracker to enable undo the changes.
    def HistoryTracker():
        pass

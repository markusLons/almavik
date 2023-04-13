import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

class detectorDrop:

    center_mass = []
    img = []
    img_contour = []
    def shaded_contours(self, zeroes, min_area=0, max_area=10000):
        # Convert the input image to 8-bit grayscale
        gray = cv2.cvtColor(np.uint8(zeroes), cv2.COLOR_BGR2GRAY)
        # Apply Gaussian blurring to remove noise
        blur = cv2.GaussianBlur(gray, (7, 7), 0)

        # Apply Canny edge detection with the current parameters
        edges = cv2.Canny(blur, 100, 200)

        # Perform closing operation to close the contour
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

        # Dilate the contours
        kernel = np.ones((5, 5), np.uint8)
        dilated = cv2.dilate(closed, kernel, iterations=3)

        # Find the contours in the binary image
        contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Create a new black image with the same shape as the input
        shaded = np.zeros(zeroes.shape)

        # Loop through each contour and draw it filled in white on the shaded image
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > min_area and area < max_area:
                cv2.drawContours(shaded, [contour], 0, (255, 255, 255), -1)

        # Return the shaded image
        return shaded

    def __init__(self, img_path):
        MIN_AREA = 7000
        MAX_AREA = 25000
        list_photos = []

        for file_name in os.listdir(img_path):
            list_photos.append(cv2.imread(os.path.join(img_path, file_name), cv2.IMREAD_COLOR))
        number_photo = 0
        for img in list_photos:
            # Convert the image to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Apply Gaussian blurring to remove noise
            blur = cv2.GaussianBlur(gray, (7, 7), 0)

            # Apply Canny edge detection with the current parameters
            edges = cv2.Canny(blur, 100, 200)

            # Perform closing operation to close the contour
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
            closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

            # Dilate the contours
            kernel = np.ones((5, 5), np.uint8)
            dilated = cv2.dilate(closed, kernel, iterations=3)

            # Find the contours in the binary image
            contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Draw the contours on a copy of the original image
            contour_img = img.copy()
            zeroes = np.zeros(contour_img.shape)
            cv2.drawContours(zeroes, contours, -1, (0, 255, 0), 2)

            # Find shaded contours within the given area range
            new_img = self.shaded_contours(zeroes, MIN_AREA, MAX_AREA)

            # Apply Gaussian blurring to remove noise
            new_img = cv2.GaussianBlur(new_img, (7,7), 0)

            # Convert the image to grayscale
            gray_img = cv2.cvtColor(new_img.astype(np.uint8), cv2.COLOR_BGR2GRAY)

            # Convert the image to a single-channel 8-bit image
            gray_img = cv2.convertScaleAbs(gray_img)
            # Find the moments of the contour image
            M = cv2.moments(gray_img)

            # Calculate the center of mass
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
            else:
                cX, cY = 0, 0

            # Print the center of mass
            self.center_mass.append((number_photo,cX, cY))
            number_photo += 1
            self.img.append(img)
            self.img_contour.append(new_img)
            print("Center of mass: ({}, {})".format(cX, cY))

            #plt.imshow(new_img)
            #plt.show()

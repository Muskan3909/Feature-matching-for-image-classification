import cv2
import matplotlib.pyplot as plt
# reading the images
img1 = cv2.imread('/content/drive/MyDrive/Notebook/tom.png')
img2 = cv2.imread('/content/drive/MyDrive/Notebook/jerry.jpg')
#convert to greyscale using function
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#show greyscale images
plt.imshow(img1),plt.show()
plt.imshow(img2),plt.show()
#create shift object
sift = cv2.xfeatures2d.SIFT_create()
#extract keypoints and descriptors from both grayscale images
keypoints_1, descriptors_1 = sift.detectAndCompute(img1,None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2,None)
#feature matching
#create brute-force matcher with L1 distance to match pair of keypoints will be considered a match if bothkeypoints are each other's nearest neighbors
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
matches = bf.match(descriptors_1,descriptors_2)
matches = sorted(matches, key = lambda x:x.distance)
#draw the matches on a new image
img3 = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2, matches[:50], img2, flags=2)
#flags parameter is set to 2 to indicate only the matched key points and lines connecting them should be drawn.
plt.imshow(img3), plt.show()



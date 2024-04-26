import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors
import cv2

img= cv2.imread('bags.png')
plt.imshow(img)
plt.show()
img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

r,g,b= cv2.split(img)
fig= plt.figure()
axis = fig.add_subplot(1,1,1,projection="3d")
pixel_colors= img.reshape((np.shape(img)[0]*np.shape(img)[1],3))
norm= colors.Normalize(vmin=-1., vmax=1.)
norm.autoscale(pixel_colors)
pixel_colors= norm(pixel_colors).tolist()
axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors= pixel_colors, marker=".")
axis.set_xlabel("Red")
axis.set_ylabel("Green")
axis.set_zlabel("Blue")
plt.show()

hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
h,s,v = cv2.split(hsv_img)
fig = plt.figure()
axis= fig.add_subplot(1,1,1, projection= "3d")
axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors= pixel_colors, marker=".")
axis.set_xlabel("Hue")
axis.set_ylabel("Saturation")
axis.set_zlabel("Value")
plt.show()

#SILLON AMARILLO
light_yellow = (33,255,255)
dark_yellow= (14,155,90)
mask = cv2.inRange(hsv_img, dark_yellow, light_yellow)
amarillo= cv2.bitwise_and(img, img, mask=mask)
plt.subplot(1,2,1)
plt.imshow(mask, cmap= "gray")
plt.subplot(1,2,2)
plt.imshow(amarillo)
plt.show()

#SILLON NARANJA
light_orange = (13,255,255)
dark_orange= (0,127,23)
mask = cv2.inRange(hsv_img, dark_orange, light_orange)
naranja = cv2.bitwise_and(img, img, mask=mask)
plt.subplot(1,2,1)
plt.imshow(mask, cmap= "gray")
plt.subplot(1,2,2)
plt.imshow(naranja)
plt.show()

#SILLON VERDE
light_green = (100,250,200)
dark_green= (50,110,20)
mask = cv2.inRange(hsv_img, dark_green, light_green)
verde= cv2.bitwise_and(img, img, mask=mask)
plt.subplot(1,2,1)
plt.imshow(mask, cmap= "gray")
plt.subplot(1,2,2)
plt.imshow(verde)
plt.show()

#SILLON AZUL 
light_blue = (150,230,200)
dark_blue= (90,110,40)
mask = cv2.inRange(hsv_img, dark_blue, light_blue)
azul= cv2.bitwise_and(img, img, mask=mask)
plt.subplot(1,2,1)
plt.imshow(mask, cmap= "gray")
plt.subplot(1,2,2)
plt.imshow(azul)
plt.show()

#TODOS LOS COLORES 
light = (255,255,255)
dark= (0,110,60)
mask = cv2.inRange(hsv_img, dark, light)
todo= cv2.bitwise_and(img, img, mask=mask)
plt.subplot(1,2,1)
plt.imshow(mask, cmap= "gray")
plt.subplot(1,2,2)
plt.imshow(todo)
plt.show()


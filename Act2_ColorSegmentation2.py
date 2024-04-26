from skimage.io import imread, imshow
from skimage.color import rgb2hsv
import matplotlib.pyplot as plt
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm 
from matplotlib import colors
import cv2 

img = cv2.imread('bags.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

hsv_img = rgb2hsv(img)
fig, ax = plt.subplots(1,3, figsize=(15,5))
ax[0].imshow (hsv_img[:,:,0],cmap='hsv')
ax[0].set_title('hue')
ax[1].imshow(hsv_img[:,:,1], cmap = 'hsv')
ax[1].set_title('transparency')
ax[2].imshow(hsv_img[:,:,2], cmap='hsv')
ax[2].set_title('value')
fig.colorbar(imshow(hsv_img[:,:,2], cmap = 'hsv'))
#fig.tight_layout()
plt.show()

#TODOS LOS SILLONES SIN EL FONDO
hsv_img = rgb2hsv(img)
lower_mask = hsv_img[:,:,0] > 0.0
upper_mask = hsv_img[:,:,0] < 1
saturation_mask = hsv_img[:,:,1] > 0.5

mask2 = upper_mask*lower_mask*saturation_mask
red = img[:,:,0]*mask2
green = img[:,:,1]*mask2
blue = img[:,:,2]*mask2
todos2 = np.dstack((red, green, blue))
plt.imshow(todos2)
plt.show()

#SILLON AMARILLO 
hsv_img = rgb2hsv(img)
lower_mask = hsv_img[:,:,0] > 0.1
upper_mask = hsv_img[:,:,0] < 0.3
saturation_mask = hsv_img[:,:,1] > 0.755

mask2 = upper_mask*lower_mask*saturation_mask
red = img[:,:,0]*mask2
green = img[:,:,1]*mask2
blue = img[:,:,2]*mask2
amarillo2 = np.dstack((red, green, blue))
plt.imshow(amarillo2)
plt.show()

#SILLON AZUL 
hsv_img = rgb2hsv(img)
lower_mask = hsv_img[:,:,0] > 0.5
upper_mask = hsv_img[:,:,0] < 0.7
saturation_mask = hsv_img[:,:,1] > 0.4

mask2 = upper_mask*lower_mask*saturation_mask
red = img[:,:,0]*mask2
green = img[:,:,1]*mask2
blue = img[:,:,2]*mask2
azul2 = np.dstack((red, green, blue))
plt.imshow(azul2)

plt.show()

#SILLON VERDE 
hsv_img = rgb2hsv(img)
lower_mask = hsv_img[:,:,0] > 0.2
upper_mask = hsv_img[:,:,0] < 0.6
saturation_mask = hsv_img[:,:,1] > 0.4

mask2 = upper_mask*lower_mask*saturation_mask
red = img[:,:,0]*mask2
green = img[:,:,1]*mask2
blue = img[:,:,2]*mask2
verde2 = np.dstack((red, green, blue))
plt.imshow(verde2)
plt.show()

#SILLON NARANJA
hsv_img = rgb2hsv(img)
lower_mask = hsv_img[:,:,0] > 0.0
upper_mask = hsv_img[:,:,0] < 0.1
saturation_mask = hsv_img[:,:,1] > 0.56

mask2 = upper_mask*lower_mask*saturation_mask
red = img[:,:,0]*mask2
green = img[:,:,1]*mask2
blue = img[:,:,2]*mask2
naranja2 = np.dstack((red, green, blue))
plt.imshow(naranja2)
plt.show()


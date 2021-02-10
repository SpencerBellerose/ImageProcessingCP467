import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test1.png',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
fourier_t = 20*np.log(np.abs(fshift)) #Fourier Shift Using Numpy

#plots original image
plt.subplot(121),plt.imshow(img)
plt.title('Original'), plt.xticks([]), plt.yticks([])

#plots fourier transformed image
plt.subplot(122),plt.imshow(fourier_t, cmap = 'gray') #shown in greyscale
plt.title('Post Fourier Transform'), plt.xticks([]), plt.yticks([])
plt.show()

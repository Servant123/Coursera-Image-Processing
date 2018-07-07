import cv2
import numpy as np

img = cv2.imread('obama.jpg')


#neigbour hood length
nlen = 4
mysum=0

#to find dimensions of image
height, width, channels = img.shape


print(width)
print(height)

print(img[0,0])
print(img[0,1])
#+img[1,0]+img[1,1]+img[1,2]+img[2,0]+img[2,1]+img[2,2] wont work
print(np.add(img[0,0],img[0,1]))


# Outer 2 for loops are for running through each pixel of the image
# Inner 2 for loops are for traversing through neighbourhood pixels and adding the pixel values

#starting and ending pixels or region we want to blur can be specified in range
for i in np.arange(1 , height-nlen, int(nlen/2)):
    for j in np.arange(1, width-nlen, int(nlen/2)):
        rowind = i - int((nlen/2)) # index must be an integer
        colind = j - int((nlen/2))
        mysum=[0, 0,0] # rememer
        for k in range(0,nlen):
            for m in range(0, nlen):
                 mysum = np.add(mysum, img[rowind+k, colind+m])
        mysum= mysum/(nlen*nlen)
        #print(img[i,j],mysum)
        for k in range(0,nlen):
            for m in range(0, nlen):
                img[rowind+k, colind+m]= mysum

for i in range(0, height):
    for j in range(0, width):
        print(img[i][j])


path = 'F:/New Volume/Image Processing/week1/rsrobama.jpg'
cv2.imwrite(path,img)

import cv2
import numpy as np
from matplotlib import pyplot as plt



def connect(img,x,y):
    m=len(img)
    n=len(img[0])
    for i in range(m):
        a=-1
        for j in range(n):
            if img[i][j]==255:
                if a>=0 and j-a<y:
                    img[i][a:j]=255
                    
                a=j
    for j in range(n):
        a=-1
        for i in range(m):
            if img[i][j]==255:
                if a>=0 and i-a<x:
                    img[a:i][j:j+1]=255
                a=i

image = cv2.imread('4.jpg',0)
print(image.size,image.shape,len(image),len(image[0]))
im=cv2.resize(image,(500,687))
cv2.imshow('org',im)

blur = cv2.GaussianBlur(im, (5,5), 0)
ret, th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('th',th)

img=th

connect(img,3,30)
cv2.imshow('dilationConnect',img)
print(img.size,img.shape,len(img),len(img[0]))
_,cnts,_=cv2.findContours(img,1,2)
a=0
m=len(img)
n=len(img[0])
havg=0
wavg=0

print(cnts)

for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    havg+=h
    wavg+=w
havg/=len(cnts)
wavg/=len(cnts)
print(havg)
print(wavg)
attr=[]
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    if w/h > 5.0 or w<n/15.0 or h/w>5.0 or h<havg*2.0/3.0 or w>wavg*4.0/3.0:
        continue
    attr.append((x,y,w,h))

for x,y,w,h in attr:
    cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
    print(x,y,w,h,w/h,n/15)

cv2.imshow('f',im)

cv2.waitKey(0)
cv2.destroyAllWindows()

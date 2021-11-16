# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 01:10:50 2021

@author: Arafat Rohan
"""
#%%
import numpy
import cv2
import math
#%%

img = cv2.imread('E:/Downloads/lena.jpg',0)
#cv2.imshow("frame",img)

sobel_y = [[1,0,-1],[2,0,-2],[1,0,-1]]
sobel_x = [[1,2,1],[0,0,0],[-1,-2,-1]]

out = img.copy()
img_sobel = img.copy()

for i in range (1, img.shape[0]-1):
    for j in range(1,img.shape[1]-1):
        temp_x = 0
        temp_y = 0
        for s in range(-1,2):
            for t in range(-1,2):
                temp_x += sobel_x[s+1][t+1] * img.item(i-s,j-t)
                temp_y += sobel_y[s+1][t+1] * img.item(i-s,j-t)
        img_sobel.itemset((i,j), ((temp_x**2) + (temp_y**2))**(1/2))
cv2.imshow("Sobel",img_sobel)



imgb = img.copy()
out = img.copy()
for i in range (1, imgb.shape[0]-1):
    for j in range(1,imgb.shape[1]-1):
        if(imgb.item(i,j)>=128):
            imgb.itemset((i,j),255)
        else:
            imgb.itemset((i,j),0)
        
cv2.imshow("Binary",imgb)

ed = [[0,255,0],[255,255,255],[0,255,0]]
for i in range(1, imgb.shape[0]-1):
    for j in range(1, imgb.shape[1]-1):
        flag = False
        for s in range(-1,2):
            for t in range(-1,2):
                if ed[s+1][t+1]>0 and  ed[s+1][t+1] == imgb.item(i+s,j+t):
                  flag = True
        if flag == True:
          out.itemset((i,j),255)
        else:
          out.itemset((i,j),0)

for i in range(0, imgb.shape[0]):
    for j in range(0, imgb.shape[1]):
      w = out.item(i,j) - imgb.item(i,j)
      out.itemset((i,j), w)
cv2.imshow("Dilation",out)



for i in range(1, imgb.shape[0]-1):
    for j in range(1, imgb.shape[1]-1):
        flag = False
        match = 0
        for s in range(-1,2):
            for t in range(-1,2):
                if ed[s+1][t+1]>0 and  ed[s+1][t+1] == imgb.item(i+s,j+t):
                  flag = True
                  match += 1
        if flag == True and match != 5:
          out.itemset((i,j),0)
        elif flag == True and match == 5:
          out.itemset((i,j),255)
        elif flag == False:
          out.itemset((i,j),0)

for i in range(0, imgb.shape[0]):
    for j in range(0, imgb.shape[1]):
      w = imgb.item(i,j) - out.item(i,j)
      out.itemset((i,j), w)
cv2.imshow("Erosion",out)

cv2.waitKey(1000000)
cv2.destroyAllWindows()
#%%

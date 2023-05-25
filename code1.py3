import cv2
import math
import numpy as np

file_src = 'scream.jpg'
file_dst = 'scream_dst.jpg'

img_src = cv2.imread(file_src, 1)#カラー読み込み
#img_src = cv2.imread(file_src, 0)#グレースケール読み込み

cv2.namedWindow('src')
cv2.namedWindow('dst')

#処理
img_dst = cv2.flip(img_src, flipCode = 0)#垂直反転

cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)
cv2.imwrite(file_dst, img_dst)

cv2.waitKey(10000)
cv2.destroyAllWindows()
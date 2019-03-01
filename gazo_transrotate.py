from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageOps
import cv2

# 元となる画像の読み込み
filename='4378-2'
#img = Image.open(filename+'.jpg')
img = cv2.imread(filename+'.jpg',0)
#width, height=img.size
#img = ImageOps.grayscale(img)
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

plt.imshow(thresh)
plt.savefig('./rotate/OOTSUrotate_4378.jpg')
plt.pause(1)
plt.close()

imgEdge,contours,hierarchy = cv2.findContours(thresh, 1, 2)

#抽出された輪郭群をひとつひとつ処理
i = 0
radius0=0
for c in contours :
    cnt = c
    M = cv2.moments(cnt)
    #面積を求める
    area = cv2.contourArea(cnt)
    #ゴミを除外
    if area < 1000 : 
        continue
        
    # 円描画に必要な情報を計算
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)
    print(center,radius)
    img = cv2.circle(img,center,radius,(125,125,125),5)
    plt.imshow(img)
    plt.show()
    plt.close()
    if radius >= radius0:
        center_x=center[0]
        center_y=center[1]
        radius0=radius
    x,y,w,h = cv2.boundingRect(cnt)

img = Image.open(filename+'.jpg')
print(center_x,center_y)    
plt.imshow(img)
plt.show()
plt.close()

j=-1
for x in range(-20,20,10):
    for y in range(-20,20,10):
        img = Image.open(filename+'.jpg')
        img = img.rotate(0, translate=(x, y))
        #width, height=img.size
        #print(width, height)
        img = img.rotate(0,center=(center_x+x, center_y+y))
        plt.imshow(img)
        j += 1
        plt.savefig('./rotate/transrotate_4378/trans_rotate_4378_'+str(j)+'.jpg')
        plt.pause(0.01)
        plt.close()
        for i in range(10,361,10):
            j += 1
            img = img.rotate(10,center=(center_x+x, center_y+y))
            plt.imshow(img)
            plt.savefig('./rotate/transrotate_4378/trans_rotate_4378_'+str(j)+'.jpg')
            plt.pause(0.01)
            plt.close()


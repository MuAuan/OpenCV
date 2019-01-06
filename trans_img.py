#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# usage: ./increase_picture.py hogehoge.jpg
#

import cv2
import numpy as np
import sys
import os

# ヒストグラム均一化
def equalizeHistRGB(src):
    
    RGB = cv2.split(src)
    Blue   = RGB[0]
    Green = RGB[1]
    Red    = RGB[2]
    for i in range(3):
        cv2.equalizeHist(RGB[i])

    img_hist = cv2.merge([RGB[0],RGB[1], RGB[2]])
    return img_hist

# ガウシアンノイズ
def addGaussianNoise(src):
    row,col,ch= src.shape
    mean = 0
    var = 0.1
    sigma = 15
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = src + gauss
    
    return noisy

# salt&pepperノイズ
def addSaltPepperNoise(src):
    row,col,ch = src.shape
    s_vs_p = 0.5
    amount = 0.004
    out = src.copy()
    # Salt mode
    num_salt = np.ceil(amount * src.size * s_vs_p)
    coords = [np.random.randint(0, i-1 , int(num_salt))
                 for i in src.shape]
    out[coords[:-1]] = (255,255,255)

    # Pepper mode
    num_pepper = np.ceil(amount* src.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i-1 , int(num_pepper))
             for i in src.shape]
    out[coords[:-1]] = (0,0,0)
    return out

if __name__ == '__main__':
    # プログラムが存在するディレクトリの代入
    current_dir = os.getcwd()
    print(current_dir)
    # 画像が存在するディレクトリの代入

    image="hosi.jpg"    
        # 画像の読み込み
    img_src = cv2.imread(image)
    cv2.imshow('org1',img_src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    trans_img = []
    for i in range(10,100,5):
        for j in range(10,100,5):
            # 平滑化用
            average_square = (i,j)  #(10,10)
            # x軸方向の標準偏差
            sigma_x = 0
            sigma_y = 0
            # 平滑化      
            trans_img.append(cv2.blur(img_src, average_square,(sigma_x,sigma_y)))      

                
    # 反転
    flip_img = []
    for img in trans_img:
        flip_img.append(cv2.flip(img, 1))
    #trans_img.extend(flip_img)
    
    # ヒストグラム均一化
    hst_img = []
    for img in trans_img:
        hst_img.append(equalizeHistRGB(img))
    #trans_img.extend(hst_img)
    #trans_img.append(equalizeHistRGB(img_src))

    # ノイズ付加
    gaus_img = []
    for img in trans_img:
        gaus_img.append(addGaussianNoise(img))
    #trans_img.extend(gaus_img)    
    #trans_img.append(addGaussianNoise(img_src))
    spn_img = []
    for img in trans_img:
        gaus_img.append(addSaltPepperNoise(img))
    #trans_img.append(addSaltPepperNoise(img_src))    
    trans_img.extend(flip_img)    
    trans_img.extend(hst_img)
    trans_img.extend(gaus_img) 
    trans_img.extend(spn_img)       
        
    # 保存
    if not os.path.exists("trans_images2"):
        os.mkdir("trans_images2")
    
   # base =  os.path.splitext(os.path.basename(sys.argv[1]))[0] + "_"
    img_src.astype(np.float64)
    for i, img in enumerate(trans_img):
        # 比較用
        # cv2.imwrite("trans_images/" + base + str(i) + ".jpg" ,cv2.hconcat([img_src.astype(np.float64), img.astype(np.float64)]))
        cv2.imwrite("trans_images2/" + str(i) + ".jpg" ,img) 

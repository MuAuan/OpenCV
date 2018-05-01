import numpy as np
import cv2

# cv2.cv.CV_FOURCC
def cv_fourcc(c1, c2, c3, c4):
    return (ord(c1) & 255) + ((ord(c2) & 255) << 8) + \
        ((ord(c3) & 255) << 16) + ((ord(c4) & 255) << 24)

cap = cv2.VideoCapture('dougasozai_car.mp4')
GRAY_FILE_NAME='gray_dougasozai_car.avi'
FRAME_RATE=30
ret, frame = cap.read()

# Define the codec and create VideoWriter object
height, width, channels = frame.shape
out = cv2.VideoWriter(GRAY_FILE_NAME, \
                      cv_fourcc('X', 'V', 'I', 'D'), \
                      FRAME_RATE, \
                      (width, height), \
                      True)  #isColor=True for color
"""
out = cv2.VideoWriter(GRAY_FILE_NAME, \
                      cv2.VideoWriter_fourcc(*'XVID'), \
                      FRAME_RATE, \
                      (width, height), \
                      False)  ##isColor=False for gray
"""
# ウィンドウの準備（無くても余り変わらない）
cv2.namedWindow('frame')
cv2.namedWindow('gray')
cv2.namedWindow('hsv')
cv2.namedWindow('mask')
cv2.namedWindow('res')
cv2.namedWindow('gaussian')

while ret == True:
    #ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv =cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv =cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # ガウシアン平滑化
    # (5, 5)はｘ、ｙ方向の標準偏差で変えるとボケ度が変わる、最後の引数はint,ボーダータイプらしいが数字の意味不明    
    g_frame = cv2.GaussianBlur(frame, (15, 15), 0)
    gg_frame = cv2.cvtColor(g_frame, cv2.COLOR_BGR2GRAY)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND： mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    cv2.imshow('hsv',hsv)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('gaussian',g_frame)

    
    #書込みgrayならグレー画像、frameなら拡張子変更
    #カラーなら、out = cv2.VideoWriter()でisColor=True、グレーならFalse
    #out.write(gray)  #OK by cv2.VideoWriter_fourcc(*'XVID') #NG by cv_fourcc('X', 'V', 'I', 'D')
    #out.write(res)    #OK by cv_fourcc('X', 'V', 'I', 'D')
    #out.write(mask)  #OK by cv2.VideoWriter_fourcc(*'XVID') #NG by cv_fourcc('X', 'V', 'I', 'D')
    #out.write(hsv)    #OK by cv_fourcc('X', 'V', 'I', 'D')
    #out.write(frame)    #OK by cv_fourcc('X', 'V', 'I', 'D')
    out.write(g_frame)  #OK by cv_fourcc('X', 'V', 'I', 'D')
    #out.write(gg_frame)  #OK by cv2.VideoWriter_fourcc(*'XVID') #NG by cv_fourcc('X', 'V', 'I', 'D')
    
    #なんかKey押せば止まる
    if cv2.waitKey(25) >= 0:  
        break
        
    ret, frame = cap.read()

cap.release()
out.release()
cv2.destroyAllWindows()

from time import sleep
import cv2

def cv_fourcc(c1, c2, c3, c4):
        return (ord(c1) & 255) + ((ord(c2) & 255) << 8) + \
            ((ord(c3) & 255) << 16) + ((ord(c4) & 255) << 24)

def main():
    OUT_FILE_NAME = "combined_video"
    FRAME_RATE=30
    dst = cv2.imread('0.jpg')
    rows,cols,channels = dst.shape
    print(rows,cols,channels)

    timer = cv2.getTickCount()
    out = cv2.VideoWriter(OUT_FILE_NAME+str(int(timer))+".mp4", \
              cv_fourcc('M', 'P', '4', 'V'), \
              FRAME_RATE, \
              (cols, rows), \
              True)
    
    for i in range(1,1619):
        cv2.imshow('combined',dst)
        
        #cv2.waitKey(1)&0xff
        cv2.destroyAllWindows()
        # 読み込んだフレームを書き込み
        out.write(dst)

        # 次のフレームを読み込み
        dst = cv2.imread('{}.jpg'.format(i))

if __name__ == '__main__':
    main()

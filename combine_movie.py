#coding=utf-8

import cv2

def combine_movie():

    # 入力する動画と出力パスを指定。
    target1 = "kenbikyo_video_hatuga_60-3.mp4"
    target2 = "kenbikyo_video4450940952464.mp4"
    target3 = "kenbikyo_video4527173059250.mp4"
    result = "kenbikyo_combine_slow.m4v" 

    # 形式はMP4Vを指定
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    movie = cv2.VideoCapture(target1)    
    fps    = movie.get(cv2.CAP_PROP_FPS)
    height = movie.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width  = movie.get(cv2.CAP_PROP_FRAME_WIDTH)
    print(fps, int(width), int(height))
    
    # 出力先のファイルを開く(s=0.5;fast,s=2;slow)
    s=2
    out = cv2.VideoWriter(result, int(fourcc), int(fps*0.5), (int(width), int(height)))
    
    # 動画の読み込みと動画情報の取得
    for i in range(1,4):
        if i==1:
            movie = cv2.VideoCapture(target1)
            print(i)
        elif i==2:
            movie = cv2.VideoCapture(target2)
            print(i)
        elif i==3:
            movie = cv2.VideoCapture(target3)
            print(i)    

        # 最初の1フレームを読み込む
        if movie.isOpened() == True:
            ret,frame = movie.read()
        else:
            ret = False

        # フレームの読み込みに成功している間フレームを書き出し続ける
        while ret:
            cv2.putText(frame, 'comBined_movie', (400,400), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 2);
            
            # 読み込んだフレームを書き込み
            out.write(frame)

            # 次のフレームを読み込み
            ret,frame = movie.read()


if __name__ == '__main__':
    combine_movie()
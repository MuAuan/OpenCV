# -*- coding: utf-8 -*-
import cv2


# 定数定義
ESC_KEY = 27     # Escキー
INTERVAL= 33     # 待ち時間
FRAME_RATE = 30  # fps

ORG_WINDOW_NAME = "org"
GRAY_WINDOW_NAME = "gray"

ORG_FILE_NAME = "douga_car2.mp4"   #"org_768x576.avi"
GRAY_FILE_NAME = "gray_douga_car2.avi"   #"gray_768x576.avi"

# 元ビデオファイル読み込み
org = cv2.VideoCapture(ORG_FILE_NAME)

# 保存ビデオファイルの準備
end_flag, c_frame = org.read()
height, width, channels = c_frame.shape
rec = cv2.VideoWriter(GRAY_FILE_NAME, \
                      cv2.VideoWriter_fourcc(*'XVID'), \
                      FRAME_RATE, \
                      (width, height), \
                      False)
# ウィンドウの準備
cv2.namedWindow(ORG_WINDOW_NAME)
cv2.namedWindow(GRAY_WINDOW_NAME)

# 変換処理ループ
while end_flag == True:
    # グレースケール変換
    g_frame = cv2.cvtColor(c_frame, cv2.COLOR_BGR2GRAY)

    # フレーム表示
    cv2.imshow(ORG_WINDOW_NAME, c_frame)
    cv2.imshow(GRAY_WINDOW_NAME, g_frame)

    # フレーム書き込み
    rec.write(g_frame)

    # Escキーで終了
    key = cv2.waitKey(INTERVAL)
    if key == ESC_KEY:
        break

    # 次のフレーム読み込み
    end_flag, c_frame = org.read()

# 終了処理
cv2.destroyAllWindows()
org.release()
rec.release()


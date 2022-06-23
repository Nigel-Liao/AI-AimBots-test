import cv2
import mediapipe as mp
import mss
import pyautogui
import numpy as np
import time
import win32api
import win32con
import math

mp_drawing = mp.solutions.drawing_utils          # mediapipe 繪圖方法
mp_drawing_styles = mp.solutions.drawing_styles  # mediapipe 繪圖樣式
mp_pose = mp.solutions.pose                      # mediapipe 姿勢偵測

cap = cv2.VideoCapture(0)

WIDTH = 520
HEIGHT = 320
MOVEMENT = 2.5
HEADSHOT = 0.2
TARGET_SIZE = 100
MAX_TARGET_DISTANCE = math.sqrt(2 * pow(TARGET_SIZE, 2))
COLORS = np.random.uniform(0, 255, size=(1500, 3))

videoGameWindowTitle = "Overwatch"
# videoGameWindowTitle = str(input())

# 測試輸入遊戲標題
try:
    videoGameWindows = pyautogui.getWindowsWithTitle(videoGameWindowTitle)
    videoGameWindow = videoGameWindows[0]
except:
    print("此遊戲標題不存在")
    exit()

# 畫面資訊
monitor = {"mon": 1, "top": videoGameWindow.top + (videoGameWindow.height - HEIGHT) // 2,
           "left": ((videoGameWindow.left + videoGameWindow.right) // 2) - (WIDTH // 2),
           "width": WIDTH,
           "height": HEIGHT}


# center
cWidth = monitor["width"]/2
cHeight = monitor['height']/2

# 螢幕拍照
sct = mss.mss()

# 啟動骨架偵測
with mp_pose.Pose(min_detection_confidence=0.5, enable_segmentation=True, min_tracking_confidence=0.5) as pose:
    while True:
        # t = time.time()

        img = np.array(sct.grab(monitor))
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # 轉換成 RGB
        results = pose.process(imgRGB)                  # 取得姿勢偵測結果

        # 根據姿勢偵測結果，標記身體節點和骨架
        mp_drawing.draw_landmarks(imgRGB, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

        if not results.pose_landmarks:
            continue
        x = int(results.pose_landmarks.landmark[0].x * WIDTH)
        y = int(results.pose_landmarks.landmark[0].y * HEIGHT)
        mouseMove = [x - cWidth, y - HEADSHOT - cHeight]
        cv2.circle(imgRGB, (int(x),
                   int(y)), 8, (0, 0, 255))

        if win32api.GetAsyncKeyState(0x01):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,
                                 int(mouseMove[0]*MOVEMENT), int(mouseMove[1]*MOVEMENT), 0, 0)

        cv2.imshow('pose', imgRGB)
        cv2.waitKey(5)

        # fps
        # print('fps: {}'.format(1/(time.time()-t)))

        # nose
        print(x, y)

cap.release()
cv2.destroyAllWindows()

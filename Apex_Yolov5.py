from unittest import result
import torch
import pyautogui
import gc
import numpy as np
import cv2
import time
import mss
import win32api
import win32con

# 遊戲標題
videoGameWindowTitle = "Apex Legends"

# 偵測視窗大小
screenShotHeight = 320
screenShotWidth = 320

# 自動偵測大小
aaDetectionBox = 320

# 自動跟槍速度
aaMovementAmp = 3

# 篩選大小
confidence = 0.5

# 測試遊戲標題
try:
    videoGameWindows = pyautogui.getWindowsWithTitle(videoGameWindowTitle)
    videoGameWindow = videoGameWindows[0]
except:
    print("遊戲標題不存在")
    exit()

# Setting up the screen shots
monitor = {"mon": 1, "top": videoGameWindow.top + (videoGameWindow.height - screenShotHeight) // 2,
           "left":  ((videoGameWindow.left + videoGameWindow.right) // 2) - (screenShotWidth // 2),
           "width": screenShotWidth,
           "height": screenShotHeight}

# 自動偵測中央
cWidth = monitor["width"] / 2
cHeight = monitor["height"] / 2

# 截圖
sct = mss.mss()


# yolov5模組
model = torch.hub.load('ultralytics/yolov5', 'yolov5s',
                       pretrained=True, force_reload=True)
model.classes = [0]

COLORS = np.random.uniform(0, 255, size=(1500, 3))

while True:
    img = np.delete(np.array(sct.grab(monitor)), 3, axis=2)

    # 演算後影像
    results = model(img, size=320).pandas().xyxy[0]

    # 篩選
    filteredResults = results[(results['class'] == 0) & (
        results['confidence'] > confidence)]

    # 是否在偵測中心判斷
    cResults = ((filteredResults["xmin"] > cWidth - aaDetectionBox) & (filteredResults["xmax"] < cWidth + aaDetectionBox)) & \
        ((filteredResults["ymin"] > cHeight - aaDetectionBox) &
         (filteredResults["ymax"] < cHeight + aaDetectionBox))

    # 移除不在偵測中心項目
    targets = filteredResults[cResults]

    # 偵測中心有物
    if len(targets) != 0:
        targets['current_mid_x'] = (targets['xmax'] + targets['xmin']) // 2
        targets['current_mid_y'] = (targets['ymax'] + targets['ymin']) // 2

        # 被偵測物體中心
        xMid = round(
            (targets.iloc[0].xmax + targets.iloc[0].xmin) / 2)
        yMid = round((targets.iloc[0].ymax + targets.iloc[0].ymin) / 2)

        box_height = targets.iloc[0].ymax - targets.iloc[0].ymin

        headshot_offset = box_height * 0.3

        mouseMove = [xMid - cWidth, (yMid - headshot_offset) - cHeight]
        cv2.circle(img, (int(
            mouseMove[0] + xMid), int(mouseMove[1] + yMid - headshot_offset)), 3, (0, 0, 255))

        # 移動滑鼠
        if win32api.GetKeyState(0x01):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(
                mouseMove[0] * aaMovementAmp), int(mouseMove[1] * aaMovementAmp), 0, 0)
        last_mid_coord = [xMid, yMid]

    # 可視化ai判斷
    for i in range(0, len(results)):
        (startX, startY, endX, endY) = int(results["xmin"][i]), int(
            results["ymin"][i]), int(results["xmax"][i]), int(results["ymax"][i])

        confidence = results["confidence"][i]

        idx = int(results["class"][i])

        # 偵測物範圍
        label = "{}: {:.2f}%".format(
            results["name"][i], confidence * 100)
        cv2.rectangle(img, (startX, startY), (endX, endY),
                      COLORS[idx], 2)
        y = startY - 15 if startY - 15 > 15 else startY + 15
        cv2.putText(img, label, (startX, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
    cv2.imshow('s', img)
    cv2.waitKey(1)

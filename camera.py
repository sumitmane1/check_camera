from ast import excepthandler
from multiprocessing import connection
import pandas as pd
import cv2
df = pd.read_csv("test.csv")
Rtps_url = []
Store = int(input("Enter Store Number:"))
for i,row in df.iterrows():
    if row['store']==Store:
                video=cv2.VideoCapture(row['RTSP IP'])
                if video is None or not video.isOpened():
                     video1 = cv2.VideoCapture(row['RTSP URL'])
                     if video1 is None or not video1.isOpened():
                        print(video1)
                         video2 = cv2.VideoCapture(row['RTSP URL1'])
                         if video2 is None or not video2.isOpened():
                            print(video1)
                             video3 = cv2.VideoCapture(row['RTSP URL2'])
                             if video3 is None or not video3.isOpened():
                                print(video2)
                                Rtps_url.append([row['RTSP IP'],row['RTSP URL'],row['store'],"Not working"])
    df2 = pd.DataFrame(Rtps_url)
    # print("DF2")
    # print(df2)
    df2.to_csv("Output.csv")

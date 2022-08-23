from ast import excepthandler
from multiprocessing import connection
import pandas as pd
import cv2
df = pd.read_csv("test.csv")
Rtps_url = []
Store = int(input("Enter Store Number:"))
for i,row in df.iterrows():
    if row['store']==Store:
            print(row['RTSP IP'],row['store'])
            try:
                video=cv2.VideoCapture(row['RTSP IP'])
                    # print("tryyyyyyyyyyyyyy")
                # if video is None or not video.isOpened():
            except:
            #    cv2.VideoCapture(row['RTSP URL'])
                try:
                    video1=cv2.VideoCapture(row['RTSP URL'])
                
                    # if video1 is None or not video1.isOpened():
                except:
                    Rtps_url.append([row['RTSP IP'],row['store'],"Not working"])
    df2 = pd.DataFrame(Rtps_url)
    # print("DF2")
    # print(df2)
    df2.to_csv("Output.csv")

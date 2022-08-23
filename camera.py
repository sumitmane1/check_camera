from multiprocessing import connection
import pandas as pd
import cv2
df = pd.read_csv(r"C:\Users\Sumit\Desktop\CV RTSP Task\test.csv")
Rtps_url = []
Store = int(input("Enter Store Number:"))
for i,row in df.iterrows():
    if row['store']==Store:
            print(row['RTSP IP'],row['store'])
            video=cv2.VideoCapture(row['RTSP IP'])
                # print("tryyyyyyyyyyyyyy")
            if video is None or not video.isOpened():
                
            #    cv2.VideoCapture(row['RTSP URL'])
                video1=cv2.VideoCapture(row['RTSP URL'])
                if video1 is None or not video1.isOpened():
                    Rtps_url.append([row['RTSP IP'],row['store'],"Not working"])
                         
    df2 = pd.DataFrame(Rtps_url)
    # print("DF2")
    # print(df2)
    df2.to_csv("Output.csv")

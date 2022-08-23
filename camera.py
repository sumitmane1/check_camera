from multiprocessing import connection
import pandas as pd
import cv2
df = pd.read_csv(r"C:\Users\Sumit\Desktop\CV RTSP Task\test.csv")
Rtps_url = []
Store = int(input("Enter Store Number:"))
for i,row in df.iterrows():
    if row['store']==Store:
        print(row['RTSP IP'],row['store'])
        try:
            try:
                video=cv2.VideoCapture(row['RTSP IP'])
                # print("tryyyyyyyyyyyyyy")
                if video is None or not video.isOpened():
                    raise ConnectionError

            # try:
            #     cv2.VideoCapture(row['RTSP IP'])
            #     print("tryyyyyyyyyyyyyy")
                # Rtps_url.append([row['RTSP IP'],row['store']])
            except ConnectionError:
                # print("start")
                cv2.VideoCapture(row['RTSP URL'])
                # print("exceptttttttttttttttt")
                if video is None or not video.isOpened():
                    raise ConnectionError
                # Rtps_url.append([row['RTSP IP'],row['store']])
        except ConnectionError :
            # print("ERRORr")
            # print(e)
            # print(Rtps_url)
            Rtps_url.append([row['RTSP IP'],row['store'],str(ConnectionError)])            
    df2 = pd.DataFrame(Rtps_url,cloumns=["RTSP URL","Store No."],index=True)
    # print("DF2")
    # print(df2)
    df2.to_csv("Output.csv")

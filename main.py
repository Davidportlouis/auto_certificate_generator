# author: @art3mis

import cv2
import pandas as pd
import matplotlib.pyplot as plt

user_data = pd.read_csv("./data/test.csv",header=None).values

certi_path = "./template/test.jpg"

font_size = 2
font_color = (51,51,51)

y_adjustment = -730
x_adjustment = 350

font = cv2.FONT_HERSHEY_COMPLEX_SMALL

for name in user_data:
    img = cv2.imread(certi_path)
    name = name.item()
    text_size =  cv2.getTextSize(name,font,font_size,4)[0]
    text_x = (img.shape[1] - text_size[0])/2 + x_adjustment
    text_y = (img.shape[0] + text_size[1]/2) + y_adjustment
    text_x = int(text_x)
    text_y = int(text_y)

    cv2.putText(img,name,(text_x,text_y),font,font_size,font_color,4)
    cv2.imwrite(f"./out/{name}.png",img)
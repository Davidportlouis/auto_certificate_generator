# author: @art3mis

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("test.jpg")
font_size = 2
font_color = (51,51,51)

y_adjustment = -730
x_adjustment = 350

font = cv2.FONT_HERSHEY_COMPLEX_SMALL
test = "A. David Port Louis"
event = "lorem Ipsum"

text_size =  cv2.getTextSize(test,font,font_size,4)[0]
text_x = (image.shape[1] - text_size[0])/2 + x_adjustment
text_y = (image.shape[0] + text_size[1]/2) + y_adjustment
text_x = int(text_x)
text_y = int(text_y)

cv2.putText(image,test,(text_x,text_y),font,font_size,font_color,4)
cv2.imwrite("./test.png",image)

# cv2.destroyAllWindows()
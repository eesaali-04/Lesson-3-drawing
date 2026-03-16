import cv2

img = cv2.imread('pikachu.png')

start_point = (200,200)
end_point = (350,450)
color = (200,100,0)
thickness = 3
image = cv2.rectangle(img,start_point,end_point,color,thickness)
cv2.imshow('pikachu with rectangle',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
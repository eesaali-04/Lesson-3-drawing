import cv2

img = cv2.imread('pikachu.png')
start_point = (500,0)
end_point = (500,800)
color = (200,200,200)
thickness = 6
image = cv2.line(img,start_point,end_point,color,thickness)
cv2.imshow('pikachu with line', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
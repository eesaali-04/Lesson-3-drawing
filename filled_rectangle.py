import cv2

img = cv2.imread('pikachu.png', 0)
start_point = (400,425)
end_point = (700,750)
color = (0,0,200)
thickness = -1
image = cv2.rectangle(img,start_point,end_point,color,thickness)
cv2.imshow('pikachu with filled rectangle', image)
cv2.waitKey()
cv2.destroyAllWindows()
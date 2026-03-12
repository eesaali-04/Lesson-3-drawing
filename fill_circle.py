# Create circle same but fill with the colour 
import cv2

image = cv2.imread('pikachu.png')
centre_cor = (300,350)
radius = 80
color = (100,0,0)
thickness = -1
image = cv2.circle(image,centre_cor,radius,color,thickness)
cv2.imshow('pika with full circle',image)
cv2.waitKey()
cv2.destroyAllWindows()
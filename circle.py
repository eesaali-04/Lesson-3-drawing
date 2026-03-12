import cv2

image = cv2.imread('pikachu.png')
centre_cor = (250,300)
radius = 125
color = (200,50,25)
thickness = 5
image = cv2.circle(image,centre_cor,radius,color,thickness)
cv2.imshow('circle pika',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
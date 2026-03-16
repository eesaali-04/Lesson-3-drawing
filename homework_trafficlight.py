import cv2

image = cv2.imread('black_bg.png')
centre_cor = (250,150)
radius = 40
color = (0,0,255)
thickness = -1
image = cv2.circle(image,centre_cor,radius,color,thickness)
centre_cor = (250,250)
radius = 40
color = (0,255,255)
thickness = -1
image2 = cv2.circle(image,centre_cor,radius,color,thickness)
centre_cor = (250,350)
radius = 40
color = (0,255,0)
thickness = -1
image3 = cv2.circle(image,centre_cor,radius,color,thickness)
start_point = (185,80)
end_point = (315,420)
color = (255,255,255)
thickness = 3
image4 = cv2.rectangle(image,start_point,end_point,color,thickness)
cv2.imshow('Traffic light',image)
cv2.waitKey()
cv2.destroyAllWindows()
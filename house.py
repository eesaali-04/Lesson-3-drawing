import cv2

image = cv2.imread('black.png')
start_point = (200,200)
end_point = (600,200)
color = (31, 249, 198)
thickness = 3
image = cv2.line(image,start_point,end_point,color,thickness)

start_point = (200,200)
end_point = (400,25)
color = (31, 249, 198)
thickness = 3
image = cv2.line(image,start_point,end_point,color,thickness)

start_point = (400,25)
end_point = (600,200)
color = (31, 249, 198)
thickness = 3
image = cv2.line(image,start_point,end_point,color,thickness)

start_point = (200,200)
end_point = (600,450)
color = (54,69,100)
thickness = 3
image = cv2.rectangle(image,start_point,end_point,color,thickness)

start_point = (450,225)
end_point = (550,450)
color = (184,252,170)
thickness = 3
image = cv2.rectangle(image,start_point,end_point,color,thickness)

center_cor = (325,300)
radius = 45
color =(230,145,60)
thickness = 2
image = cv2.circle(image,center_cor,radius,color,thickness)
cv2.imshow('house on image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
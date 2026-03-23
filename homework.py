import cv2

image = cv2.imread('white.jpg')
start_point = (300,10)
end_point = (700,575)
color = (231, 76, 56)
thickness = 3
image = cv2.rectangle(image,start_point,end_point,color,thickness)

start_point = (330,25)
end_point = (425,230)
color = (31, 249, 198)
thickness = 3
image = cv2.rectangle(image,start_point,end_point,color,thickness)

start_point = (440,25)
end_point = (535,230)
color = (31, 249, 198)
thickness = 3
image = cv2.rectangle(image,start_point,end_point,color,thickness)

start_point = (545,25)
end_point = (660,230)
color = (31,249,198)
thickness = 3
image = cv2.rectangle(image,start_point,end_point,color,thickness)


start_point = (330,240)
end_point = (425,400)
color = (31, 249, 198)
thickness = 3
image = cv2.rectangle(image,start_point,end_point,color,thickness)

start_point = (440,240)
end_point = (535,400)
color = (31, 249, 198)
thickness = 3
image = cv2.rectangle(image,start_point,end_point,color,thickness)

start_point = (545,240)
end_point = (660,400)
color = (31,249,198)
thickness = 3
image = cv2.rectangle(image,start_point,end_point,color,thickness)


start_point = (330,410)
end_point = (425,570)
color = (31, 249, 198)
thickness = 3
image = cv2.rectangle(image,start_point,end_point,color,thickness)

start_point = (440,410)
end_point = (535,570)
color = (31, 249, 198)
thickness = 3
image = cv2.rectangle(image,start_point,end_point,color,thickness)

start_point = (625,470)
end_point = (685,570)
color = (200,34,12)
thickness = 3
image = cv2.rectangle(image,start_point,end_point,color,thickness)

centre_cor = (635,540)
radius = 5
color = (0,0,255)
thickness = -1
image = cv2.circle(image,centre_cor,radius,color,thickness)
cv2.imshow('apartment',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
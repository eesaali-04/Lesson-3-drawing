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


cv2.imshow('house on image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
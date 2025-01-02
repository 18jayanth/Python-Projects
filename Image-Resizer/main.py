import cv2
src = cv2.imread("sachin.jpg ",cv2.IMREAD_UNCHANGED)
cv2.imshow("title",src)
scale_percent=25
new_width=int(src.shape[0]*scale_percent/100)
new_height=int(src.shape[1]*scale_percent/100)
newsize=(new_width,new_height)
output=cv2.resize(src,newsize)
cv2.imwrite('newimage.png',output)
cv2.waitKey(0)
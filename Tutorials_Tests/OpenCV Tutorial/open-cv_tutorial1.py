import cv2

img = cv2.imread('assets/rocket.png', 1)
img = cv2.resize(img, (0,0), fx=2, fy=2)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('assets/new_img.png', img)

cv2.imshow('rocket', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
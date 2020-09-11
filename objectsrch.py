import cv2

image = cv2.imread('12.jpg')
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_lov = (97, 50, 50)
image_high = (115, 255, 255)
image_hsv = cv2.inRange(image_hsv, image_lov, image_high)
cntr, hr = cv2.findContours(image_hsv.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, cntr, -1, (0, 255, 0), 2, cv2.LINE_AA, hr, 2)
cv2.imshow('12.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

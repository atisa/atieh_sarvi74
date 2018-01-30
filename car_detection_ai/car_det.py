import cv2
#uncomment next line if you want to examine LBPcascade features

#car_cascade = cv2.CascadeClassifier('LBPcascade.xml')
car_cascade = cv2.CascadeClassifier('cars.xml')

#u can rename the image name to use a different image
img = cv2.imread('1.jpg', 1)
#uncomment the below line if you want to resize photo (not required)
#img = cv2.resize(img, None, fx =3 ,fy = 3, interpolation = cv2.INTER_CUBIC)

#tp get the gray image to start proccesing...
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect cars using gray photo (change 1.2 to 1.1 or 1.3 if needed
cars = car_cascade.detectMultiScale(gray, 1.2, 1)

# draws a rectange around the car
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)


# Shows image
cv2.imshow("cars found", img)
cv2.waitKey(0)


#https://pysource.com/2021/10/29/kalman-filter-predict-the-trajectory-of-an-object/
from kalmanfilter import KalmanFilter
import cv2
import json

l1 = json.load(open('cent_hist.json', 'r'))
# Kalman Filter
kf = KalmanFilter()

img = cv2.imread("blue_background.webp")



for pt in l1:
    cv2.circle(img, pt, 7, (0, 20, 220), -1)
    predicted = kf.predict(pt[0], pt[1])

    cv2.circle(img, predicted, 8, (20, 220, 0), 3)

for i in range(1):
    predicted = kf.predict(predicted[0], predicted[1])
    cv2.circle(img, predicted, 8, (20, 220, 0), 3)

    


cv2.imshow("Img", img)
cv2.waitKey(0)

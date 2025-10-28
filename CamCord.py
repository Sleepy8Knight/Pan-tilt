import cv2
import numpy as np

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX


while True:
    check, frame = cam.read()

    img = cv2.resize(frame,(320, 240))

    img_empty = np.zeros((img.shape[0], img.shape[1]))
    gray = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)


    img_empty = np.zeros((img.shape[0], img.shape[1]))

    img2 = cv2.normalize(img, img_empty, 0, 255, cv2.NORM_MINMAX)

    _, threshold = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #img4 = cv2.GaussianBlur(threshold, (3, 3), 0)

    cv2.imshow("Original", img)

    cv2.imshow("Normalized", img2)

    cv2.imshow("Threshold", threshold)

    #cv2.imshow("Blurred", img4)
  

    for cnt in contours:
        # Approximate and draw contour
        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
        cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5)

        # Flatten points
        n = approx.ravel()
        i = 0
        for j in n:
            if i % 2 == 0:  # x, y coords
                x, y = n[i], n[i + 1]
                coord = f"{x} {y}"
                if i == 0:  # first point
                    cv2.putText(img2, "Arrow tip", (x, y), font, 0.5, (255, 0, 0))
                else:
                    cv2.putText(img2, coord, (x, y), font, 0.5, (0, 255, 0))
            i += 1



    key = cv2.waitKey(1)
    if key == 27:
        break
cam.release()
cv2.destroyALLwindows()


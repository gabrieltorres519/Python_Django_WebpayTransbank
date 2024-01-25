import cv2

img = cv2.imread("logo.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

cv2.waitKey(0) # Para poder cerrar la ventana con la imagen
cv2.destroyAllWindows()

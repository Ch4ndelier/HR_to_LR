import cv2

# TODO: add edge blur

img = cv2.imread("/Users/liujunyuan/HR_to_LR/data/1k2kminus/0001.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edge_output = cv2.Canny(gray, 50, 150)
cv2.imshow("edge_output", edge_output)
cv2.waitKey(0)
cv2.destroyAllWindows()

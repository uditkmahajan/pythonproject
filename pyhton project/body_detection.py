import cv2

body_cascade=cv2.CascadeClassifier("haarcascade_fullbody.xml")

cap=cv2.VideoCapture(0)
print("cap")
while True :
    res, img= cap.read()

    if not res :
        break

    grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    body=body_cascade.detectMultiScale(grey_img,1.6,3)
    print("body")
    for (x,y,w,h) in body :
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow("img",img)
    print("rec") 
    if cv2.waitKey(1) & 0xFF == ord("q") :
        break
cap.release()
cv2.destroyAllWindows()
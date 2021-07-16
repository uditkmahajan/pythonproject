import cv2

# load the classifier

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap=cv2.VideoCapture(0)

while True :

    response, img= cap.read()

    if not response : 
        break
    
    grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(grey_img,1.6,7)
    print("sfsfs")
    for (x,y,w,h) in faces :
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow("img",img)

    if cv2.waitKey(1) & 0xFF == ord("q") :
        break

cap.release()
cv2.destroyAllWindows()
import cv2

#load the classifiet
car_cascade=cv2.CascadeClassifier("haarcascade_car.xml")

# load the video
cap=cv2.VideoCapture("Sequence_03.mp4")

while True :
    response, img=cap.read()

    if response==False:
        break

    #convert to grey scale image
    grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    #detect car
    cars=car_cascade.detectMultiScale(grey_img,1.6,2)
    for (x,y,w,h) in cars :
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        # show image
        cv2.imshow("img",img)
    
    if cv2.waitKey(1) & 0xFF == ord("q") :
        break

cap.release()
cv2.destroyAllWindows()
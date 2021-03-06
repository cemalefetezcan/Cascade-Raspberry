import cv2

objectName = "Raspberry"
frameWidth = 280
frameHeight = 360
color=(255,0,0)

cap=cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

def empty(a):pass

#trackbar

cv2.namedWindow("Sonuc")
cv2.resizeWindow("Sonuc", frameWidth,frameHeight + 100)


#cascade classifier
cascade=cv2.CascadeClassifier("raspberry_object.xml")

while True:
    success,img=cap.read()
    if success:
        gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        rects=cascade.detectMultiScale(gray,1.1,9)
        
        for(x,y,w,h) in rects:
            cv2.rectangle(img,(x,y),(x+w,y+h),color,3)
            cv2.putText(img, objectName, (x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            
        cv2.imshow("Sonuc",img)
        
    if cv2.waitKey(1) & 0xFF == ord("q"): break
    
import cv2
cap=cv2.VideoCapture(0)
face_xml=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
isOpened=cap.isOpened
i=0
while(isOpened):
    if i>10:
        break
    else:
        i+=1
    (flag,frame)=cap.read()
    filename="image"+str(i)+".jpg"
    #print(filename)
    if flag==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face_xml.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imwrite(filename,frame,[cv2.IMWRITE_JPEG_QUALITY,100])
        
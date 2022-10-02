from typing import final
import cv2
import jwt

SECRET_KEY = 'key.env'

for i in range(9):
    
    try:
        i = str(i)
        img = cv2.imread('images/'+i+'.png')

        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)


        decoded = jwt.decode(value, SECRET_KEY, algorithms=["HS256"])
        print(decoded)
        
        
        
        
    except(jwt.InvalidSignatureError,jwt.DecodeError):
        # print("jwt.InvalidSignatureError")
        print(i)
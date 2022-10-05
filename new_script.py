import pyqrcode
import jwt
num = 102
serial = []

SECRET_KEY = "nuvkhelaiyaftw"


for i in range(1, num+1):
    if(i<10):
        y = ("OFSQR-2022-0" + str(i))
        serial.append(y)
    elif(i>=10):
        y = ("OFSQR-2022-" + str(i))
        serial.append(y)
print(serial[101])

def making_qr():
    for i in range(num):
        encoded_jwt = jwt.encode(
            {
                "serial":serial[i],
                "name": "NuvKhelaiyaplayer"
            },
               SECRET_KEY,
               algorithm="HS256"
            )
        print(encoded_jwt)

        qr = pyqrcode.create(encoded_jwt)
        qr.png("offline/" + str(i+1) + ".png", scale=8)
        decoded = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=["HS256"])
        print(decoded)

making_qr()
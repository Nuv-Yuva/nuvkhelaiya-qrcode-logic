import random
import jwt 
import string
from oauth2client.service_account import ServiceAccountCredentials
import pyqrcode
import gspread
import pprint
import png

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("nuvkhelaiyaeb").sheet1

data = sheet.get_all_records()
uid = sheet.col_values(1)
name = sheet.col_values(2)
email = sheet.col_values(6)
enrollmentid = sheet.col_values(4)

num = 5
serial = []

for i in range(num):
    if(i<10):
        y = ("00000000-0000-EBQR-2022-00000000000" + str(i))
        serial.append(y)
    elif(i>=10 and i<100):
        y = ("00000000-0000-EBQR-2022-0000000000"+ str(i))
        serial.append(y)
    else:
        y = ("00000000-0000-EBQR-2022-000000000" + str(i))
        serial.append(y)


# # def making_listToJson():
# #     res = []
# #     for i in range(1, len(data) + 1):
# #         temp = {"serial": serial[i],
# #                   "name": name[i],
# #                   "enrollment": enrollmentid[i]}
# #         res.append(temp)

# #     jsonFile = open("reciepents.json", "w")
# #     jsonFile.write(json.dumps(res))
# #     jsonFile.close()



# # randlen = 64
# # num = 1

# # for i in range(num):
# #         res = ''.join(random.choices(string.ascii_uppercase , k=randlen))

# #         g = open(r'key.env', 'a')
# # generate a 64 byte random key
# #         g.write(res)
# #         g.write("\n")

SECRET_KEY = 'key.env'


def making_qr():
    for i in range(num):
        encoded_jwt = jwt.encode(
               {"Name": data[i]["name"], "serial": serial[i], "enrollment id": data[i]["enrollmentid"]},
               SECRET_KEY,
               algorithm="HS256")
        print(encoded_jwt)
        g = open(r'encodedjwt.txt', 'a')

        g.write(encoded_jwt)
        g.write("\n")
        qr = pyqrcode.create(encoded_jwt)
        qr.png("images/" + str(i+1) + ".png", scale=8)
        decoded = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=["HS256"])
        print(decoded)

making_qr()
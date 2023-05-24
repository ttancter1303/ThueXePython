import json
import random
import re 
import bcrypt
import os
import Client as Client
import Admin as Admin
import Vehical as Vehical
data = {}
data['client'] = []
adminCheck = False
UserID = 0.00
def check_specical_charecter(username):
    pattern = r'[^\w\s]'
    if re.search(pattern,username):
        return True
    else:
        return False


# mã hóa mật khẩu sử dụng hàm thư viện đẻ băm mật khẩu ngẫu nhiên và được mã hóa bởi utf-8
#
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'),salt)
    return hashed_password

ClientObj = Client()
def login(adminCheck):
    print("Đăng nhập")
    Username = input("Username : ")
    Password = input("Password : ")
    if(Username[0:5] == "admin"):
        print(Username[0:5])
        with open("data/admin.txt") as json_file:
            data = json.load(json_file)
            for p in data['admin']:
                if p['username'] == Username and bcrypt.checkpw(Password.encode('utf-8'),p['password'].encode('utf-8')): # sau khi mã hóa ở phần đăng kí sau khi đăng nhập cũng màx hóa lại
                    print("Admin login succesfully !")
                    adminCheck = True
                    return adminCheck
    else:
        with open('data/client.txt') as json_file:
            data = json.load(json_file)
            for p in data['client']:
                if p['username'] == Username and bcrypt.checkpw(Password.encode('utf-8'),p['password'].encode('utf-8')):
                    print("Login succesfully !")
                    p['id'] == UserID
                    ClientObj.id = p['id']
                    ClientObj.name = p['name']
                    return adminCheck

def register():
    print("Đăng ký")
    while True:    
        Name = input("Name : ")
        Username = input("Username : ")
        Password = input("Password : ")
        PasswordAgain = input("Password Again : ")
        if (Password == PasswordAgain):
            if check_specical_charecter(Username):
                print('nhập lại đi có ký tự đặc biệt kìa !  ')
                
                
            hashed_password = hash_password(Password)  
            hashed_password_str = hashed_password.decode('utf-8') #chuyền đổi từ bytes sang chuỗi thì lưu được vào file json      
            
            id = random.random()
            # tạo id random để đảm bảo các client ko bị trùng lặp
            NewUser = Client(id, Name, Username, hashed_password_str)
            
            # data["client"].append({
            #     "id": NewUser.id,
            #     "name": NewUser.name,
            #     "username": NewUser.username,
            #     "password": NewUser.password})
            # print(data)
            # obj = open("data/client.txt", "r")
            # txt1 = obj.read()
            # check file client nếu rỗng thì push data vào luôn
            # nhưng vì 1 lỗi nào đó mà nó đang lỗi ở đây :))))
            
            
            # lấy thông tin về tệp và lấy kích thước tệp đó
            if os.stat("data/client.txt").st_size == 0:
                with open("data/client.txt", 'w') as outfile:
                    json.dump(data, outfile)
            else:
                # nếu ko rỗng thì cắt chuỗi và thêm chuỗi mới vào
                # cách làm là lấy chuỗi json cũ về + chuỗi mới convert nó về lại dạng json
                # ko push dạng string vào đc nó sẽ lỗi nên phải chuyển sang json
                # tất nhiên là vẫn đang thiếu phần check ký tự đặc biệt ở username và mã hóa password
                
                # tempString = obj.read()[0:-2]+","+ str(data)[12:-2]+"]}"
                # jsonObj = json.loads(tempString)
                # with open("data/client.txt", 'w') as outfile:
                #     json.dump(jsonObj, outfile)
                # print(jsonObj)
                # obj.close()
                
                #  sử dụng try except để bắt lỗi và sử lý ngoại lệ 
               try:
                    with open('data/client.txt') as json_file:
                        txt1 = json_file.read() # lấy dữ liệu trong file
                        jsonObj = json.loads(txt1) # chuyển đổi nôi dụng sang từ chuỗi json sang đối tượng
                        jsonObj['client'].append({
                            "id": NewUser.id,
                            "name": NewUser.name,
                            "username": NewUser.username,
                            "password": NewUser.password})
                    with open('data/client.txt', 'w') as outfile:
                        json.dump(jsonObj, outfile)
               except json.decoder.JSONDecodeError:
                #    nếu có lỗi xảy ra khi chuyển đổi nọi dụng của file sang đối tượng json
                #    tạo luôn đối tượng json mới lưu vào file
                   with open('data/client.txt','w') as outfile:
                       json.dump(data,outfile)
            break           

        else:
            print("Wrong password")

def showAllCilent():
    # đây là hàm để test xem là đã đẩy được lên thành công chưa và hiển thị lên màn hình
    with open('data/client.txt') as json_file:
        data = json.load(json_file)
        for p in data['client']:
            print('Name: ' + p['name'])
            print('password: ' + p['password'])
            print('username: ' + p['username'])
            print('')

    # app chia làm 3 màn hình chính là login admin và client

def menuLogin():
    # thêm switch case vào
    register()
    login(adminCheck)
def mainMenuClient():
    pass    # thêm switch case và các hàm vào

def mainMenuAdmin():
    pass    # thêm switch case và các hàm vào

def addMoreMoney():
    money = int(input("Nhập số tiền muốn thêm: "))
    ClientObj.money = money
    print("Thêm thành công")
#     update vào trong file client thay thế vị trí client cũ( ghi đè sao cho đúng vị trí)
def addNewVihical():
    pass
def editVehical():
    pass
def deleteVehical():
    pass

def showAllClient():
    pass

def Main(adminCheck):
    menuLogin()
    if(adminCheck == True):
        print("Đăng nhập admin thành công")
        mainMenuAdmin()
    elif(adminCheck == False):
        print("Đăng nhập user thành công")
        mainMenuClient()
    # showAllCilent()

Main(adminCheck)
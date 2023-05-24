import json
import random
import re 
import bcrypt
import os


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

data = {}
data['client'] = []
adminCheck = False
class Admin:
    def __init__(self, id, name, username, password):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
#NTUYNJQXMQ

class Client:
    def __init__(self,id,name,username,password,money,ListVehical):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.money = money
        self.ListVehical = ListVehical
    def __init__(self, id, name, username, password):
        self.id = id
        self.name = name
        self.username = username
        self.password = password

class Vehical:
    def __init__(self, id, name, status, listClient, cost, quantity, time):
        self.id = id
        self.name = name
        self.status = status
        self.listClient = listClient
        self.cost = cost
        self.quantity = quantity
        self.time = time

    def __init__(self, id, name, status,  cost, quantity):
        self.id = id
        self.name = name
        self.status = status
        self.cost = cost
        self.quantity = quantity


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
                    return adminCheck
# phần login đã làm xong 90% chưa có check kí tự đặc biệt và giải mã password

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
            # lấy thông tin về tệp và lấy kích thước tệp đó
            open("data/client/" + NewUser.name + ".txt")
            if os.stat("data/client/"+NewUser.name+".txt").st_size == 0:
                with open("data/client/"+NewUser.name+".txt", 'w') as outfile:
                    json.dump(data, outfile)
            else:
                #  sử dụng try except để bắt lỗi và sử lý ngoại lệ 
               try:
                    with open("data/client/"+NewUser.name+".txt") as json_file:
                        txt1 = json_file.read() # lấy dữ liệu trong file
                        jsonObj = json.loads(txt1) # chuyển đổi nôi dụng sang từ chuỗi json sang đối tượng
                        jsonObj['client'].append({
                            "id": NewUser.id,
                            "name": NewUser.name,
                            "username": NewUser.username,
                            "password": NewUser.password})
                    with open("data/client/"+NewUser.name+".txt", 'w') as outfile:
                        json.dump(jsonObj, outfile)
               except json.decoder.JSONDecodeError:
                #    nếu có lỗi xảy ra khi chuyển đổi nọi dụng của file sang đối tượng json
                #    tạo luôn đối tượng json mới lưu vào file
                   with open("data/client/"+NewUser.name+".txt",'w') as outfile:
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

def Main(adminCheck):
    menuLogin()
    if(adminCheck == True):
        print("Dang nhap admin thanh cong")
        mainMenuAdmin()
    elif(adminCheck == False):
        print("dang nhap user thanh cong")
        mainMenuClient()
    # showAllCilent()

Main(adminCheck)
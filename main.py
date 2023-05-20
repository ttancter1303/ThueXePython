import json
import random

data = {}
data['client'] = []
adminCheck = False
class Admin:
    def __init__(self, id, name, username, password):
        self.id = id
        self.name = name
        self.username = username
        self.password = password


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
                if(p['username'] == Username and p['password'] == Password):
                    print("Admin login succesfully !")
                    adminCheck = True
                    return adminCheck

    else:
        with open('data/client.txt') as json_file:
            data = json.load(json_file)
            for p in data['client']:
                if (p['username'] == Username and p['password'] == Password):
                    print("Login succesfully !")
                    return adminCheck
# phần login đã làm xong 90% chưa có check kí tự đặc biệt và giải mã password

def register():
    print("Đăng ký")
    Name = input("Name : ")
    Username = input("Username : ")
    Password = input("Password : ")
    PasswordAgain = input("Password Again : ")
    if (Password == PasswordAgain):
        id = random.random()
        # tạo id random để đảm bảo các client ko bị trùng lặp
        NewUser = Client(id, Name, Username, Password)
        data["client"].append({
            "id": NewUser.id,
            "name": NewUser.name,
            "username": NewUser.username,
            "password": NewUser.password})
        print(data)
        obj = open("data/client.txt", "r")
        txt1 = obj.read()
        # check file client nếu rỗng thì push data vào luôn
        # nhưng vì 1 lỗi nào đó mà nó đang lỗi ở đây :))))
        if txt1 == None:
            with open("data/client.txt", 'w') as outfile:
                json.dump(data, outfile)
        else:
            # nếu ko rỗng thì cắt chuỗi và thêm chuỗi mới vào
            # cách làm là lấy chuỗi json cũ về + chuỗi mới convert nó về lại dạng json
            # ko push dạng string vào đc nó sẽ lỗi nên phải chuyển sang json
            # tất nhiên là vẫn đang thiếu phần check ký tự đặc biệt ở username và mã hóa password
            tempString = obj.read()[0:-2]+","+ str(data)[12:-2]+"]}"
            jsonObj = json.loads(tempString)
            with open("data/client.txt", 'w') as outfile:
                json.dump(jsonObj, outfile)
            print(jsonObj)
            obj.close()

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

        # thêm switch case và các hàm vào

def mainMenuAdmin():

        # thêm switch case và các hàm vào

def Main(adminCheck):
    menuLogin()
    if(adminCheck == True):
        print("Dang nhap admin thanh cong")
        mainMenuAdmin()
    elif(adminCheck == False):
        print("dang nhap user thanh cong")
        mainMenuClient()
    # showAllCilent()



Main()


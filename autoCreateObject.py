import datetime
import json
import random
import re
import bcrypt
import os
import matplotlib.pyplot as plt


data = {}
data['client'] = []
tg = datetime.datetime.now()
time = tg.strftime("%d/%m/%Y")
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
    def __init__(self):
        pass
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
    def __init__(self):
        pass
userObj = Client()
def check_specical_charecter(username):
    pattern = r'[^\w\s]'
    if re.search(pattern,username):
        return True
    else:
        return False
def check_number(num):
    pattern = r'[^\d+]'
    if re.search(pattern, num):
        return True
    else:
        return False

# mã hóa mật khẩu sử dụng hàm thư viện đẻ băm mật khẩu ngẫu nhiên và được mã hóa bởi utf-8
#
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'),salt)
    return hashed_password
def autoCreateClient():
    print("Đăng ký")
    for i in range(0,30):
        Name = "tuan" + str(i)
        Username = "tuan"+ str(i)
        Password = "tuan"+ str(i)
        hashed_password = hash_password(Password)
        hashed_password_str = hashed_password.decode('utf-8')
        id = random.random()
        userObj.id = id
        userObj.name = Name
        userObj.username = Username
        userObj.password = hashed_password_str
        open("data/client/" + userObj.username + ".txt",'w')
        with open("data/client/" + userObj.username + ".txt") as json_file:
            data['client'].append({
                "id": userObj.id,
                "name": userObj.name,
                "username": userObj.username,
                "password": userObj.password})
        with open("data/client/" + userObj.username + ".txt", 'w') as outfile:
            json.dump(data, outfile)
        print("đang khởi tạo client....")
    print("hoàn tất")

autoCreateClient()
def autoCreateVehical():
    for i in range(0,30):
        data = {}
        data['vehical'] = []
        # tạo 1 id ngẫu nhiên trong khoảng 1 - 1000
        id = random.randint(1, 1000)
        # Nhập tên xe
        name = "toyota" + str(i)
        status = 1
        cost = 300
        quantity = 90
        # thời gian nhập xe tự động hiện theo ngày sẵn có
        tg = datetime.datetime.now()
        time = tg.strftime("%d/%m/%Y")
        # lưu vào file
        data['vehical'].append({
            'id': id,
            'name': name,
            'status': status,
            'cost': cost,
            'quantity': quantity,
            'time': time
        })
        with open('data/vehical/' + name + '.txt', 'w') as f:
            json.dump(data, f)
            print("đang khởi tạo xe")
    print("-> Bạn đã thêm xe thành công!")
# autoCreateVehical()
def autoRentVehical():
    for i in range(2,10):
        vehical = Vehical()
        folder_path = "data/vehical"
        # Lấy danh sách tên file trong thư mục
        file_names = os.listdir(folder_path)
        # lấy ra tên các file và chạy for để lấy giá trị và gán vào đối tượng vehical
        selectName = "toyota" + str(i)
        selectQuantity = 2
        with open('data/vehical/' + selectName + ".txt", 'r') as f:
            data = json.load(f)
        for p in data['vehical']:
            vehical.id = p['id']
            vehical.name = p['name']
            vehical.cost = p['cost']
            vehical.status = p['status']
            vehical.time = p['time']
            vehical.quantity = p['quantity']
        for filename in os.listdir('data/vehical/'):
            if filename.endswith('.txt'):
                with open('data/vehical/' + filename ) as f:
                    try:
                        dataVehical = json.load(f)
                    except json.decoder.JSONDecodeError:
                        continue
                    if dataVehical['vehical'][0]['name'] == selectName:
                        found = True
                        if(dataVehical['vehical'][0]['status'] == 0):
                            print("Xe đã hết vui lòng chọn xe khác")
                        else:
                            with open('data/client/' + "tuan"+str(i)+ '.txt', 'r') as userfile:
                                dataClient = json.load(userfile)
                                newDataVehical = {
                                    "id": dataVehical["vehical"][0]["id"],
                                    "name": dataVehical["vehical"][0]["name"],
                                    "cost": dataVehical["vehical"][0]["cost"],
                                    "quantity": selectQuantity,
                                    "time": time
                                }
                            dataClient["ListVehical"] = newDataVehical
                            with open('data/client/' +"tuan"+str(i)+ '.txt', 'w') as f:
                                json.dump(dataClient, f)
                                print("Thuê xe thành công")
                            break
        if not found:
            print('không tìm thấy xe có tên ',selectName)
# autoRentVehical()
from tkinter import ALL
import datetime
import json
import random
import re
import bcrypt
import os
import matplotlib.pyplot as plt
from prettytable import PrettyTable, ALL
from operator import itemgetter
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

def login():
    adminCheck = False
    print("Đăng nhập")
    Username = input("Username : ")
    Password = input("Password : ")
    if(Username[0:5] == "admin"):
        print(Username[0:5])
        with open("data/admin.json") as json_file:
            data = json.load(json_file)
            for p in data['admin']:
                if p['username'] == Username and p['password'] == Password: # sau khi mã hóa ở phần đăng kí sau khi đăng nhập cũng màx hóa lại
                    print("Admin login succesfully !")
                    adminCheck = True
                    return adminCheck

    else:
        if os.path.exists('data/client/'+Username+'.json'):
            with open('data/client/'+Username+'.json') as json_file:
                data = json.load(json_file)
                for p in data['client']:
                    if p['username'] == Username and bcrypt.checkpw(Password.encode('utf-8'),p['password'].encode('utf-8')):
                        print("Đăng nhập thành công !")
                        userObj.id = p['id']
                        userObj.name = p['name']
                        userObj.username = p['username']
                        userObj.password = p['password']
                        return adminCheck
        else: print("Nguời dùng không tồn tại")
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
            userObj.id = id
            userObj.name = Name
            userObj.username = Username
            userObj.password = hashed_password_str
            # lấy thông tin về tệp và lấy kích thước tệp đó
            if os.path.exists("data/client/"+userObj.username+".json"):
                print("Tài khoản này đã được đăng ký xin vui lòng đăng ký tài khoản khác")
                break
            else:
                open("data/client/" + userObj.username + ".json",'w')
                #  sử dụng try except để bắt lỗi và sử lý ngoại lệ 
                try:
                    with open("data/client/"+userObj.username+".json") as json_file:
                        data['client'].append({
                            "id": userObj.id,
                            "name": userObj.name,
                            "username": userObj.username,
                            "password": userObj.password})
                    with open("data/client/"+userObj.username+".json", 'w') as outfile:
                        json.dump(data, outfile)
                        print("Đăng ký thành công")
                        return userObj
                except json.decoder.JSONDecodeError:
                #    nếu có lỗi xảy ra khi chuyển đổi nọi dụng của file sang đối tượng json
                #    tạo luôn đối tượng json mới lưu vào file
                    with open("data/client/"+userObj.username+".json",'w') as outfile:
                       json.dump(data,outfile)
            break
        else:
            print("Wrong password")
        
def addVehical():
    data = {}
    data['vehical'] = []
    # tạo 1 id ngẫu nhiên trong khoảng 1 - 1000
    id = random.randint(1, 10000000000)
    found = 0
    for filename in os.listdir('data/vehical/'):
        with open('data/vehical/' + filename) as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                continue
            if data['vehical'][0]['id'] == id:
                found = True
                break
    if found:
        print("ID đang trùng lặp......")
    else:
        print("- Nhập thông tin xe: ")
        # Nhập tên xe
        while True:
            name = input("  + Nhập tên xe : ")
            if check_specical_charecter(name):
                print("-> Nhập sai định dạng! Vui lòng nhập lại.")
            else:
                break

        # tình trạng xe
        while True:
            # nếu nhập 1 còn hàng, 0 hết hàng
            status = input("  + Nhập tình trạng(1/0): ")
            if status == "0" or status == "1":
                break
            else:
                print("-> Định dạng sai! Xin vui lòng nhập lại")
        # giá tiền của 1
        while True:
            cost = input("  + Nhập giá tiền($): ")
            if check_number(cost):
                print("-> Nhập sai định dạng! Vui lòng nhập lại.")
            else:
                break
        # số lượng
        if status == "0":
            quantity = "0"
        else:
            while True:
                quantity = input("  + Nhập số lượng: ")
                if check_number(quantity):
                    print("-> Nhập sai định dạng! Vui lòng nhập lại.")
                else:
                    break
        # thời gian nhập xe tự động hiện theo ngày sẵn có
        times = datetime.datetime.now()
        time = times.strftime("%d/%m/%Y")
        # lưu vào file
        data['vehical'].append({
            'id': id,
            'name': name,
            'status': status,
            'cost': cost,
            'quantity': quantity,
            'time': time
        })
        with open('data/vehical/' + name + '.json', 'w') as f:
                json.dump(data, f)
        print("-> Bạn đã thêm xe thành công!")
    
# Sửa dữ liệu xe
def editVehical():
    names = input("Nhập tên xe cần sửa: ")
    found = False
    for filename in os.listdir('data/vehical/'):
        with open('data/vehical/' + filename) as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                continue
            if data['vehical'][0]['name'] == names:
                found = True
                name = data['vehical'][0]['name']
                break
    if found:
        with open('data/vehical/' + name + '.json', 'r') as f:
            data = json.load(f)
        print("- Thông tin xe ban đầu:")
        print(" + Tên xe:", data['vehical'][0]['name'])
        if data['vehical'][0]['status'] == "1":
            print(" + Tình trạng: Còn hàng")
        else:
            print(" + Tình trạng: Hết hàng")
        print(" + Giá tiền:", data['vehical'][0]['cost'])
        print(" + Số lượng:", data['vehical'][0]['quantity'])
        print(" + Thời gian nhập: ", data['vehical'][0]['time'])

        print("- Nhập lại thông tin xe:")
        while True:
            new_name = input("  + Nhập tên xe : ")
            if check_specical_charecter(new_name):
                print("Nhập sai định dạng! Vui lòng nhập lại.")
            else:
                break

        while True:
            # nếu nhập 1 còn hàng, 0 hết hàng
            new_status = input("  + Nhập tình trạng(1/0): ")
            if new_status == "0" or new_status == "1":
                break
            else:
                print("-> Định dạng sai! Xin vui lòng nhập lại")

        while True:
            new_cost = input("  + Nhập giá tiền($): ")
            if check_number(new_cost):
                print("-> Nhập sai định dạng! Vui lòng nhập lại.")
            else:
                break

            # Số lượng xe
        if new_status == "0":
            new_quantity = "0"
        else:
            while True:
                new_quantity = input("  + Nhập số lượng: ")
                if check_number(new_quantity):
                    print("-> Nhập sai định dạng! Vui lòng nhập lại.")
                else:
                    break
        times = datetime.datetime.now()
        new_time = times.strftime("%d/%m/%Y")
        data['vehical'][0]['name'] = new_name
        data['vehical'][0]['status'] = new_status
        data['vehical'][0]['cost'] = new_cost
        data['vehical'][0]['quantity'] = new_quantity
        data['vehical'][0]['time'] = new_time
        with open('data/vehical/' + name + '.json', 'w') as f:
            json.dump(data, f)
        print("-> Đã cập nhật thông tin xe!")
    else:
        print("-> Không tìm thấy xe !")
def deleteVehical():
    names = input("Nhập tên xe cần xóa: ")
    found = False
    for filename in os.listdir('data/vehical'):
        with open('data/vehical/' + filename) as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                continue
            if data['vehical'][0]['name'] == names:
                found = True
                name = data['vehical'][0]['name']
                break
    if found:
        filename = 'data/vehical/' + name + '.json'
        os.remove(filename)
        print("-> Xóa xe thành công!")


def bubble_sort(arr):
    n = len(arr)
    # Lặp qua từng phần tử của danh sách
    for i in range(n):
        # Lặp qua các phần tử khác của danh sách
        for j in range(0, n - i - 1):
            # So sánh hai phần tử
            if float(arr[j]['vehical'][0]['cost']) > float(arr[j + 1]['vehical'][0]['cost']):
                # Nếu phần tử hiện tại lớn hơn phần tử tiếp theo, hoán đổi chúng
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



def sort_vehical():
    folder_path = "data/vehical"
    file_names = os.listdir(folder_path)
    file_names = os.listdir(folder_path)
    table = PrettyTable()
    table.hrules = ALL  # thêm đường gạch dưới mỗi đối tượng
    table.field_names = ["id", 'name', 'cost', 'status', 'time', 'quantity']
    data = []
    for filename in file_names:
        if filename.endswith('.json'):
            with open('data/vehical/' + filename, 'r') as f:
                data.append(json.load(f))
    bubble_sort(data)
    print("xe sau khi sắp xếp theo giá tiền ")
    for p in data:
        for vehicle in p['vehical']:
            if vehicle['status'] == 1:
                status = "còn xe"
            else:
                status = "hết xe"
            table.add_row(
                [vehicle['id'], vehicle['name'], vehicle['cost'], status, vehicle['time'], vehicle['quantity']])

    print(table)


def search():
    print('tìm kiếm xe')
    name = input('nhập tên xe cần tìm kiếm: ')
    found = False
    for filename in os.listdir('data/vehical'):
        if filename.endswith('.json'):
            with open('data/vehical/' + filename) as f:
                try:
                    data = json.load(f)
                except json.decoder.JSONDecodeError:
                    continue
                if data['vehical'][0]['name'] == name:
                    found = True
                    print("thông tin xe sau khi tìm là : ")
                    print('ID : ',data['vehical'][0]['id'])
                    print('Tên xe : ',data['vehical'][0]['name'])
                    print('Tình trạng : ',data['vehical'][0]['status'])
                    print('giá tiền : ',data['vehical'][0]['cost'])
                    print('số lượng : ',data['vehical'][0]['quantity'])
                    print('thời gian nhập : ',data['vehical'][0]['time'])
                    break
    if not found:
        print('không tìm thấy xe có tên ',name)
        
def thongke():
    # Tạo dictionary để lưu trữ số lượng của từng xe
    vehicleCount = {}
    # Lấy đường dẫn tuyệt đối của thư mục data/vehical
    folder_path = os.path.abspath('data/vehical')
    # Lấy danh sách tên file trong thư mục
    file_names = os.listdir(folder_path)
    
    # Lặp qua từng file và thêm số lượng của xe vào dictionary
   
    for file_name in file_names:
        with open(os.path.join(folder_path, file_name), 'r') as f:
            data = json.load(f)
            for p in data['vehical']:
                car_type = p['name']
                quantity = p['quantity']
                if car_type in vehicleCount:
                    vehicleCount[car_type] += int(p['quantity'])
                  
                else:
                    vehicleCount[car_type] = int(p['quantity'])

    print("Số lượng mỗi loại xe:")
    for car_type, count in vehicleCount.items():
        print(f"{car_type}: {count}")       
    # Tạo biểu đồ
    plt.bar(range(len(vehicleCount)), list(vehicleCount.values()), align='center', width=0.5)
    plt.xticks(range(len(vehicleCount)), list(vehicleCount.keys()))
    plt.xlabel('Xe')
    plt.ylabel('Số lượng')
    plt.title('Số lượng của từng xe')
    # Vẽ các chữ số trên biểu đồ
    for i, count in enumerate(list(vehicleCount.values())):
        plt.text(i, count + 0.1, str(count), ha='center', va='bottom')
    plt.show()
# xem chi tiết
def get_vehicle_data():
    names = input("Nhập tên xe cần xem thông tin: ")
    found = False
    for filename in os.listdir('data/vehical/'):
        with open('data/vehical/' + filename) as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                continue
            if data['vehical'][0]['name'] == names:
                found = True
                print("- Thông tin xe :")
                print(" + Tên xe:", data['vehical'][0]['name'])
                if data['vehical'][0]['status'] == "1":
                    print(" + Tình trạng: Còn hàng")
                else:
                    print(" + Tình trạng: Hết hàng")
                print(" + Giá tiền:", data['vehical'][0]['cost'])
                print(" + Số lượng:", data['vehical'][0]['quantity'])
                print(" + Thời gian nhập: ", data['vehical'][0]['time'])
                break

    if not found:
        print("-> Không tìm thấy xe có tên!", names)
#  danh sách xe
def listVehical():
    folder_path = "data/vehical/"
    file_names = os.listdir(folder_path)
    table = PrettyTable()
    table.field_names = ["id", 'name', 'cost', 'status', 'time', 'quantity']
    table.hrules = ALL  # thêm đường gạch dưới mỗi đối tượng
    for file_name in file_names:
        with open('data/vehical/' + file_name, 'r') as f:
            data = json.load(f)
        for p in data['vehical']:

            if p['status'] == 1:
                status = "còn xe"
            else:
                status = "hết xe"
            table.add_row([p['id'], p['name'], p['cost'], status, p['time'], p['quantity']])
    print(table)
def menuChoiceForAdmin():
    while True:
        print("-----------------------")
        print("1. Thêm xe mới")
        print("2. Sửa xe")
        print("3. Xóa xe")
        print("4. Sắp xếp")
        print("5. Tìm kiếm xe ")
        print("6. Thống kê")
        print("7. Danh sách xe ")
        print("8. Chi tiết xe")
        print("0. Thoát chương trình")
        print("-----------------------")
        choice = input("Nhập lựa chọn: ")
        if choice == "1":
            addVehical()
        elif choice == "2":
            editVehical()
        elif choice == "3":
            deleteVehical()
        elif choice == "4":
            sort_vehical()
        elif choice == "5":
            search()
        elif choice == "6":
            thongke()
        elif choice == "7":
            listVehical()
        elif choice == "8":
            get_vehicle_data()
        elif choice == "0":
            print("Thoát chương trình.....")
            break
        else:
            print("Lựa chọn không hợp lệ!")
def check_list_existence(file_name):
    with open(file_name, "r") as file:
        try:
            data = json.load(file)
            if isinstance(data, dict) and "ListVehical" in data:
                if isinstance(data["ListVehical"], list):
                    return True
            return False
        except json.JSONDecodeError:
            return False
def rentVehical():
    print("Rent Vehical")
    vehical = Vehical()
    clientObj = Client()
    folder_path = "data/vehical"
    # Lấy danh sách tên file trong thư mục
    file_names = os.listdir(folder_path)
    # lấy ra tên các file và chạy for để lấy giá trị và gán vào đối tượng vehical
    selectName = input("Nhập tên xe cần thuê: ")
    selectQuantity = int(input("Nhập số lượng xe cần thuê: "))
    if(os.path.exists('data/vehical/' + selectName + '.json')):
        # kiểm tra xem file có tồn tại hay ko
        with open('data/vehical/' + selectName + ".json", 'r') as f:
            data = json.load(f)
        for p in data['vehical']:
            vehical.id = p['id']
            vehical.name = p['name']
            vehical.cost = p['cost']
            vehical.status = p['status']
            vehical.time = p['time']
            vehical.quantity = p['quantity']
        #     đẩy data vào đối tượng vehical
        with open('data/vehical/' + selectName +".json" ) as f:
            dataVehical = json.load(f)
            if dataVehical['vehical'][0]['name'] == selectName:
                if(dataVehical['vehical'][0]['status'] == 0 or dataVehical['vehical'][0]['quantity'] == 0):
                    # kiểm tra xem trạng thái và số lượng xe nếu mà hết thì ko cho thuê
                    print("Xe đã hết vui lòng chọn xe khác")
                else:
                    with open('data/client/' + userObj.username + '.json', 'r') as userfile:
                        # lấy data xe với những dữ liệu cần thiết để đẩy vào file client thuê xe
                        newVehical = {
                            "id": dataVehical["vehical"][0]["id"],
                            "name": dataVehical["vehical"][0]["name"],
                            "cost": dataVehical["vehical"][0]["cost"],
                            "quantity": int(selectQuantity),
                            "time": time
                        }
                        # khởi tạo dic mới từ những data này
                        new_dict = newVehical
                        dataClient = json.load(userfile)

                        # khởi tạo dic mới chứa thông tin của người dùng
                        clientObj.name = dataClient["client"][0]["name"]
                        clientObj.id = dataClient["client"][0]["id"]
                        clientObj.username = dataClient["client"][0]["username"]
                        newClientDataForRentVehical = {
                            "id":clientObj.id,
                            "name":clientObj.name,
                            "username":clientObj.username,
                            "quantity": selectQuantity,
                            "time": time
                        }
                    if "ListVehical" in dataClient:
                        # nếu đã tồn tại key "ListVehical thì lấy list đó ra và append dic mới vào"
                        dataClient["ListVehical"].append(new_dict)
                        with open('data/client/' + userObj.username + '.json', "w") as file:
                            json.dump(dataClient, file)
                            print("Thêm xe thành công")
                    else:
                        # nếu chưa tồn tại "ListVehical" thì tạo mới và push data vào
                        with open('data/client/' + userObj.username + '.json', 'r') as userfile:
                            dataClient = json.load(userfile)
                            newDataVehical = [{
                                "id": dataVehical["vehical"][0]["id"],
                                "name": dataVehical["vehical"][0]["name"],
                                "cost": dataVehical["vehical"][0]["cost"],
                                "quantity": selectQuantity,
                                "time": time
                            }]
                        dataClient["ListVehical"] = newDataVehical
                        with open('data/client/' + userObj.username + '.json', 'w') as f:
                            json.dump(dataClient, f)
                            print("Thuê xe thành công")
                    # đoạn này là cập nhập thêm ListClient cho vehical được thuê
                    with open('data/vehical/' + selectName + ".json") as f:
                        newDataVehicalLoad = json.load(f)
                        if "ListClient" in newDataVehicalLoad:
                            # nếu đã tồn tại key "ListClient" thì lấy list đó ra và append dic mới vào"
                            newDataVehicalLoad["ListClient"].append(newClientDataForRentVehical)
                            with open('data/vehical/' + selectName +".json", "w") as file:
                                json.dump(newDataVehicalLoad, file)
                        else:
                            # nếu chưa tồn tại "ListClient" thì tạo mới và push data vào
                            with open('data/vehical/' + selectName +".json", 'r') as userfile:
                                newDataVehicalLoad = json.load(userfile)
                                newClientDataForRentVehical = [{
                                    "id": clientObj.id,
                                    "name": clientObj.name,
                                    "username": clientObj.username,
                                    "quantity": selectQuantity,
                                    "time": time
                                }]
                            newDataVehicalLoad["ListClient"] = newClientDataForRentVehical
                            # print(newDataVehicalLoad)
                            with open('data/vehical/' + selectName +".json", 'w') as f:
                                json.dump(newDataVehicalLoad, f)
                                # print("cập nhập lại số xe thành công")
            # Trừ số lượng xe đi
            dataVehical['vehical'][0]['quantity'] = dataVehical['vehical'][0]['quantity'] - selectQuantity
            with open('data/vehical/' + selectName +".json", 'w') as f:
                json.dump(dataVehical, f)
    else:
        print(selectName + "Không tồn tại vui lòng nhập xe khác")
def menuLogin():
    # thêm switch case vào
    print("-----------------------")
    print("1. Đăng nhập")
    print("2. Đăng ký")
    print("0. Thoát chương trình")
    print("-----------------------")
    choice = input("Nhập lựa chọn: ")
    while True:
        if choice == "1":
            check = login()
            return check
        elif choice == "2":
            register()
            break
        elif choice == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ vui lòng nhập lại.")
            menuLogin()
            break
def mainMenuClient():
    rentVehical()

def mainMenuAdmin():
    print("main menu admin")
    menuChoiceForAdmin()
def Main():
    adminCheck = menuLogin()
    if(adminCheck == True):
        # đăng nhập admin
        mainMenuAdmin()
    elif(adminCheck == False):
        # đăng nhập user
        mainMenuClient()
Main()

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


def register():
    print("Đăng ký")
    Name = input("Name : ")
    Username = input("Username : ")
    Password = input("Password : ")
    PasswordAgain = input("Password Again : ")
    if (Password == PasswordAgain):
        random.seed(12523463486237968729836523238)
        id = random.random()
        NewUser = Client(id, Name, Username, Password)
        data['client'].append({
            'id': NewUser.id,
            'name': NewUser.name,
            'username': NewUser.username,
            'password': NewUser.password
        })
        with open("data/client.txt", 'w') as outfile:
            json.dump(data, outfile)
    else:
        print("Wrong password")


def menuLogin():
    # register()
    login(adminCheck)
def mainMenuClient(adminCheck):
    if(adminCheck == True):
        print("Dang nhap admin thanh cong")

def mainMenuAdmin(adminCheck):
    if(adminCheck == False):
        print("dang nhap user thanh cong")
def Main():
    menuLogin()



Main()
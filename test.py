import json
data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
print(data)
with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
# tạo 1 file mới
new = "ttan"
with open('data/client/'+new+'.txt', 'w') as f:
    f.write('Create a new text file!')


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
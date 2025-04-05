import json
import random

class account:
    def __init__(self,idUser,nameUser, passwordUser, roleUser):
        self.idUser = idUser
        self.nameUser = nameUser
        self.passwordUser = passwordUser
        self.roleUser = roleUser

    def __str__(self):
        return f"idUser: {self.idUser}\nnameUser: {self.nameUser}\npasswordUser: {self.passwordUser}\nroleUser: {self.passwordUser}"
class ManagerAccount:
    def __init__(self, filename ="account.json"):
        self.accountList = []
        self.filename = filename
        
    def loadData(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
            if not data:
                raise ValueError("Không có dữ liệu trong file")
            for ac in data:
                idUser = ac.get("idUser", "N/A")
                nameUser = ac.get("nameUser", "N/A")
                passwordUser = ac.get("passwordUser", "N/A")
                roleUser = ac.get("roleUser", "N/A")
                self.accountList.append(account(idUser, nameUser, passwordUser, roleUser))
            print("Load dữ liệu thành công!")
        except ValueError as ve:
            print(f"Lỗi: {ve}")
        except FileNotFoundError:
            print(f"Lỗi: Không tìm thấy file")
        except Exception as e:
            print(f"Lỗi không xác định: {e}")

    def saveAccount(self):
        dataNew = []
        for us in self.accountList:
            us_data = {
                "idUser": us.idUser,
                "nameUser": us.nameUser,
                "passwordUser": us.passwordUser,
                "roleUser": us.roleUser
            } 
            dataNew.append(us_data)
        with open(self.filename, "w", encoding='utf-8') as file:
            json.dump(dataNew, file)
            print("Thêm thanh công!")

    def createAc(self):
        idUser = random.random()
        nameUser = input("Tên tài khoản: ")
        passwordUser = input("Mật khẩu: ")
            
        roleUser = input("Chức vụ (Manager/General): ")
        if roleUser != "Manager":
            roleUser = "General"
        self.accountList.append(account(idUser, nameUser, passwordUser, roleUser))
        self.saveAccount()

    def readAc(self):
        if not self.accountList:
            print("Không có dữ liệu")
        else:
            for ac in self.accountList:
                print(ac)

def menu():
    qla = ManagerAccount()
    qla.loadData()
    while True:
        print("____MENU_____")
        print("1. Thêm người dùng")
        print("2. Xuất danh sách người dùng")
        print("0. THOÁT")

        choice = int(input("Mời chọn chức năng: "))
        if choice == 0:
            break
        if choice == 1:
            qla.createAc()
        elif choice == 2:
            qla.readAc()
        else:
            print(f"Không có chức năng {choice}")
    
def main():
    menu()

if __name__=="__main__":
    main()



        


import tkinter as tk
#from home import HomeScreen  # Import giao diện trang chủ
from PIL import Image, ImageTk
import customtkinter as ctk
import json

class LoginApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Đăng Nhập")
        
        self.setup_ui()  # Gọi hàm thiết lập giao diện
        self.root.mainloop()

    def setup_ui(self):
        """Thiết lập giao diện đăng nhập"""
        # Kích thước cửa sổ
        window_width, window_height = 500, 400

        # Lấy kích thước màn hình
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Tính toán vị trí để canh giữa
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        # Thiết lập kích thước & vị trí cửa sổ
        self.root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
        #Ảnh icon login
        image_path = "Images/login.png"
        img = Image.open(image_path)
        img = img.resize((90,90))
        self.photo = ImageTk.PhotoImage(img)

        #title Đăng nhập
        self.title_dangnhap = tk.Label(self.root ,text="ĐĂNG NHẬP",font=("Arial", 20, "bold"))
        self.title_dangnhap.pack(pady = 10)

        # Hiển thị ảnh
        self.image_label = tk.Label(self.root, image=self.photo)
        self.image_label.pack(pady=10)

        
        # Nhãn và ô nhập tên đăng nhập
        self.entry_username = tk.Entry(self.root,width=30, font=("Arial", 12))
        self.entry_username.pack(pady=5, ipady=5)

        # Nhãn và ô nhập mật khẩu
        self.entry_password = tk.Entry(self.root,width=30,font=("Arial", 12), show="*")
        self.entry_password.pack(pady=5,ipady=5)

        # Nhãn hiển thị thông báo
        self.label_message = tk.Label(self.root, text="", fg="red")
        self.label_message.pack(pady=5)

        # Tạo frame chứa nút bấm để căn chỉnh
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # Nút đăng nhập
        self.btn_login = tk.Button(button_frame, text="Đăng Nhập", command=self.check_login, width=15,font=("SF Pro Display", 12))
        self.btn_login.grid(row=0, column=0, padx=10, pady=10)

        # Nút thoát
        self.btn_exit = tk.Button(button_frame, text="Thoát", command=self.thoat_chuong_trinh, width=5,font=("Arial", 12))
        self.btn_exit.grid(row=0, column=1, padx=10, pady=10)

    def check_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        try:
            with open("account.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            for user in data:
                if user["nameUser"] == username and user["passwordUser"] == password:
                    self.root.destroy()
                    HomeScreen()
                    return
            # Nếu không khớp ai cả
            self.label_message.config(text="Sai tài khoản hoặc mật khẩu!")

        except FileNotFoundError:
            self.label_message.config(text="Không tìm thấy file tài khoản!")
        except json.JSONDecodeError:
            self.label_message.config(text="Lỗi định dạng JSON!")
        except Exception as e:
            self.label_message.config(text=f"Lỗi: {e}")


    def thoat_chuong_trinh(self):
        """Đóng chương trình"""
        self.root.destroy()

#Trang chủ 
class HomeScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MyHealthLog")

        self.root.geometry("900x600")
        self.root.resizable(False, False)

        # ===== Frame menu trái =====
        self.menu_frame = tk.Frame(self.root, bg="#2c3e50", width=200)
        self.menu_frame.pack(side="left", fill="y")

        # ===== Nội dung chính (bên phải) =====
        self.content_frame = tk.Frame(self.root, bg="#ecf0f1")
        self.content_frame.pack(side="right", fill="both", expand=True)

        # ===== Nút trong menu =====
        self.add_menu_button("Tài khoản", self.show_account)
        self.add_menu_button("Chỉ số BMI", self.show_bmi)
        self.add_menu_button("Tính Calo", self.show_calo)
        self.add_menu_button("Đăng Xuất", self.logout)

        # ===== Nội dung mặc định =====
        self.label_content = tk.Label(self.content_frame, text="Chào mừng!", font=("Arial", 20), bg="#ecf0f1")
        self.label_content.pack(pady=30)

        self.root.mainloop()

    def add_menu_button(self, text, command):
        button = tk.Button(self.menu_frame, text=text, command=command,
                           bg="#34495e", fg="black", font=("Arial", 12),
                           relief="flat", activebackground="#16a085", activeforeground="black")
        button.pack(fill="x", pady=5, padx=10, ipady=8)

    # ===== Các chức năng tương ứng với nút menu =====
    def show_account(self):
        self.update_content("Thông tin tài khoản")

    def show_bmi(self):
        self.update_content("Tính chỉ số BMI")

    def show_calo(self):
        self.update_content("Tính lượng calo cần thiết")

    def logout(self):
        from main import LoginApp
        self.root.destroy()
        LoginApp()

    def update_content(self, text):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        label = tk.Label(self.content_frame, text=text, font=("Arial", 18), bg="#ecf0f1")
        label.pack(pady=30)


if __name__ == "__main__":
    LoginApp()

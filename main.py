import tkinter as tk
from home import HomeScreen  # Import giao diện trang chủ

class LoginApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Đăng Nhập")
        

        # Kích thước cửa sổ
        window_width = 300
        window_height = 250
        
        # Lấy kích thước màn hình
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Tính toán vị trí để canh giữa
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)
        
        # Thiết lập kích thước & vị trí
        self.root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        tk.Label(self.root, text="Tên tài khoản:").pack(pady=5)
        self.entry_username = tk.Entry(self.root)
        self.entry_username.pack(pady=5)

        tk.Label(self.root, text="Mật khẩu:").pack(pady=5)
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack(pady=5)

        self.label_message = tk.Label(self.root, text="")
        self.label_message.pack()

        tk.Button(self.root, text="Đăng Nhập", command=self.check_login).pack(pady=10)

        self.root.mainloop()

    def check_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "admin" and password == "123":  
            self.root.destroy()  # Đóng đăng nhập
            HomeScreen()  # Mở trang chủ
        else:
            self.label_message.config(text="Sai tài khoản hoặc mật khẩu!", fg="red")

if __name__ == "__main__":
    LoginApp()  # Chạy chương trình

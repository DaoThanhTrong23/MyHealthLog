import tkinter as tk
from home import HomeScreen  # Import giao diện trang chủ
from PIL import Image, ImageTk
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

        # Hiển thị ảnh
        self.image_label = tk.Label(self.root, image=self.photo)
        self.image_label.pack(pady=10)

        # Nhãn và ô nhập tên đăng nhập
        tk.Label(self.root, text="Tên tài khoản:").pack(pady=5)
        self.entry_username = tk.Entry(self.root,width=30, font=("Arial", 12))
        self.entry_username.pack(pady=5, ipady=5)

        # Nhãn và ô nhập mật khẩu
        tk.Label(self.root, text="Mật khẩu:").pack(pady=5)
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
        """Kiểm tra thông tin đăng nhập"""
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "admin" and password == "123":  
            self.root.destroy()  # Đóng cửa sổ đăng nhập
            HomeScreen()  # Mở giao diện trang chủ
        else:
            self.label_message.config(text="Sai tài khoản hoặc mật khẩu!")

    def thoat_chuong_trinh(self):
        """Đóng chương trình"""
        self.root.destroy()

if __name__ == "__main__":
    LoginApp()

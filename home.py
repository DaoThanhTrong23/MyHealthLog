import tkinter as tk

class HomeScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Trang Chủ")
        
        # Kích thước cửa sổ
        window_width = 900
        window_height = 600
        
        # Lấy kích thước màn hình
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Tính toán vị trí để canh giữa
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)
        
        # Thiết lập kích thước & vị trí
        self.root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        label_welcome = tk.Label(self.root, text="Chào mừng bạn đến với Trang Chủ!", font=("Arial", 14))
        label_welcome.pack(pady=0)

        btn_logout = tk.Button(self.root, text="Đăng Xuất", command=self.root.destroy)
        btn_logout.pack(pady="10",side="top", anchor="e")

		#vòng kiểm tra sức khoẻ
        
        self.root.mainloop()
# HomeScreen()
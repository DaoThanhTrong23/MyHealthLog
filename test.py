import customtkinter as ctk
from tkinter import messagebox

# Khởi tạo theme
ctk.set_appearance_mode("System")      # Có thể dùng: "Light", "Dark", "System"
ctk.set_default_color_theme("blue")    # Có thể thử: "dark-blue", "green", "blue"

class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Đăng nhập hiện đại")
        self.geometry("400x350")
        self.resizable(False, False)

        # Tiêu đề
        self.label_title = ctk.CTkLabel(self, text="Chào mừng bạn", font=("Arial", 24, "bold"))
        self.label_title.pack(pady=30)

        # Entry tài khoản
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Tài khoản", width=250, font=("Arial", 14))
        self.username_entry.pack(pady=10)

        # Entry mật khẩu
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Mật khẩu", show="*", width=250, font=("Arial", 14))
        self.password_entry.pack(pady=10)

        # Nút đăng nhập
        self.login_button = ctk.CTkButton(self, text="Đăng nhập", width=150, command=self.login)
        self.login_button.pack(pady=20)

        # Nút huỷ
        self.cancel_button = ctk.CTkButton(self, text="Huỷ", width=150, fg_color="gray", hover_color="darkgray", command=self.quit)
        self.cancel_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "123456":
            messagebox.showinfo("Thành công", "Đăng nhập thành công!")
        else:
            messagebox.showerror("Thất bại", "Sai tài khoản hoặc mật khẩu.")

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()

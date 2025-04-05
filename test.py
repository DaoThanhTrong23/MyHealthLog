import tkinter as tk
from tkinter import ttk, messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Đăng nhập")
        self.root.geometry("400x300")
        self.root.configure(bg="#f4f4f4")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        # Tiêu đề
        ttk.Label(self.root, text="Đăng nhập", font=("Arial", 18, "bold")).pack(pady=20)

        # Frame chứa input
        frame = ttk.Frame(self.root)
        frame.pack(pady=10)

        # Tên đăng nhập
        ttk.Label(frame, text="Tài khoản:", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.username_entry = ttk.Entry(frame, font=("Arial", 12))
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        # Mật khẩu
        ttk.Label(frame, text="Mật khẩu:", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.password_entry = ttk.Entry(frame, font=("Arial", 12), show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Nút Đăng nhập và Hủy
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=20)

        self.login_btn = ttk.Button(btn_frame, text="Đăng nhập", command=self.login)
        self.login_btn.grid(row=0, column=0, padx=10)

        self.cancel_btn = ttk.Button(btn_frame, text="Hủy", command=self.root.quit)
        self.cancel_btn.grid(row=0, column=1, padx=10)

        # Thêm hiệu ứng hover
        self.login_btn.bind("<Enter>", lambda e: self.login_btn.configure(style="Hover.TButton"))
        self.login_btn.bind("<Leave>", lambda e: self.login_btn.configure(style="TButton"))

        self.cancel_btn.bind("<Enter>", lambda e: self.cancel_btn.configure(style="Hover.TButton"))
        self.cancel_btn.bind("<Leave>", lambda e: self.cancel_btn.configure(style="TButton"))

        # Tạo style cho nút
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12), padding=5)
        self.style.configure("Hover.TButton", background="#d6d6d6")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "123456":
            messagebox.showinfo("Thành công", "Đăng nhập thành công!")
        else:
            messagebox.showerror("Lỗi", "Sai tài khoản hoặc mật khẩu!")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()

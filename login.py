import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk 
import json
from tkinter import messagebox
from home import HomeScreen

class LoginApp:
	def __init__(self):
		self.root = tk.Tk()
		self.root.title("Đăng Nhập")
		self.icon()
		self.setup_ui()
		self.root.bind('<Return>', self.enter_login)
		self.root.mainloop()
		
	def icon(self):
		ico = Image.open('Images/logo1.png')
		photo = ImageTk.PhotoImage(ico)
		self.root.wm_iconphoto(False, photo)
		
	def setup_ui(self):
		self.login_frame = tk.Frame(self.root, width=200, height=200)
		self.login_frame.pack(pady=20)
		# Kích thước cửa sổ
		window_width, window_height = 500, 600

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
		img = img.resize((95,95))
		self.photo = ImageTk.PhotoImage(img)

		#title Đăng nhập
		self.title_dangnhap = tk.Label(self.login_frame ,text="Đăng nhập",font=("Arial", 20))
		self.title_dangnhap.pack(pady = 10)

		# Hiển thị ảnh
		self.image_label = tk.Label(self.login_frame, image=self.photo)
		self.image_label.pack(pady=10)

		
		# Nhãn và ô nhập tên đăng nhập
		self.label_username = tk.Label(self.login_frame, text="Tên đăng nhập:", font=("Arial", 12))
		self.label_username.pack(padx=0, anchor='w')
		self.entry_username = tk.Entry(self.login_frame,width=30, font=("Arial", 12))
		self.entry_username.pack(pady=5, ipady=5)
		

		# Nhãn và ô nhập mật khẩu
		self.label_password = tk.Label(self.login_frame, text="Mật khẩu:", font=("Arial", 12))
		self.label_password.pack(padx=0, anchor='w')
		self.entry_password = tk.Entry(self.login_frame,width=30,font=("Arial", 12), show="*")
		self.entry_password.pack(pady=5,ipady=5)

		# Nhãn hiển thị thông báo
		self.label_message = tk.Label(self.login_frame, text="", fg="red")
		self.label_message.pack(pady=5)

		# Tạo frame chứa nút bấm để căn chỉnh
		button_frame = tk.Frame(self.root)
		button_frame.pack(pady=10)

		# Nút đăng nhập
		self.btn_login = tk.Button(button_frame, text="Đăng Nhập", command=self.check_login, width=15,font=("Arial", 12))
		self.btn_login.grid(row=0, column=0, padx=10, pady=10)

		# Nút thoát
		self.btn_exit = tk.Button(button_frame, text="Thoát", command=self.thoat_chuong_trinh, width=5,font=("Arial", 12))
		self.btn_exit.grid(row=0, column=1, padx=10, pady=10)
	def enter_login(self, event= None):
		self.check_login()

	def check_login(self):
		username = self.entry_username.get()
		password = self.entry_password.get()

		try:
			with open("data/account.json", "r", encoding="utf-8") as f:
				data = json.load(f)

			for user in data:
				if user["username"] == username and user["password"] == password:

					nameUser = user.get("username", "N/A")
					passwordUser = user.get("password", "N/A")
					fullname = user.get("fullname", "N/A")
					age = user.get("age", 0)
					gender = user.get("gender", "Nam")
					height = user.get("height", 0)
					weight = user.get("weight", 0)
					illness = user.get("illness", "Không")
					roleUser = user.get("role", "General")

					self.root.destroy()
					HomeScreen(name = nameUser, password = passwordUser,fullname = fullname, age = age, gender = gender, height = height, weight = weight, illness = illness ,  role = roleUser)
					return

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
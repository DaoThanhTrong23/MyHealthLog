import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk 
import json
from tkinter import messagebox
from home import HomeScreen
import hashlib
from dangky import DangKy
class LoginApp:
	def __init__(self):
		self.root = tk.Tk()
		self.root.title("Đăng Nhập")
		self.icon()
		self.setup_ui()
		self.root.bind('<Return>', self.event_enter_login)
		self.root.mainloop()
		
	def icon(self):
		ico = Image.open('Images/logo1.png')
		photo = ImageTk.PhotoImage(ico)
		self.root.wm_iconphoto(False, photo)
		
	def setup_ui(self):
		#Ảnh icon login
		image_path = "Images/login.png"
		img = Image.open(image_path)
		img = img.resize((95,95))
		self.photo = ImageTk.PhotoImage(img)

		#title Đăng nhập
		self.title_dangnhap = tk.Label(self.root ,text="Đăng nhập",font=("Segoe UI", 20,"bold"))
		self.title_dangnhap.grid(column=0, row=0, columnspan=2, pady = 10)

		# Hiển thị ảnh
		self.image_label = tk.Label(self.root, image=self.photo)
		self.image_label.grid(column=0, row=1, columnspan=2, pady=10)

		
		# Nhãn và ô nhập tên đăng nhập
		self.label_username = tk.Label(self.root, text="Tên đăng nhập:", font=("Segoe UI",12))
		self.label_username.grid(column=0, row=2, columnspan=2, padx=30, sticky='w')
		self.entry_username = tk.Entry(self.root,width=30, font=("Segoe UI", 12), bd=2, relief="groove", highlightthickness=1, highlightcolor="#4a90e2")
		self.entry_username.grid(column=0, row=3, columnspan=2, pady=(0, 10), ipady=5, padx=30)
		

		# Nhãn và ô nhập mật khẩu
		self.label_password = tk.Label(self.root, text="Mật khẩu:", font=("Segoe UI", 12))
		self.label_password.grid(column=0, row=4, columnspan=2, padx=30, sticky='w')
		self.entry_password = tk.Entry(self.root,width=30,font=("Segoe UI", 12), show="*", bd=2, relief="groove", highlightthickness=1, highlightcolor="#4a90e2")
		self.entry_password.grid(column=0, row=5, columnspan=2, pady=(0, 5),ipady=5, padx=30)

		# Nhãn hiển thị thông báo
		self.label_message = tk.Label(self.root, text="", fg="red")
		self.label_message.grid(column=0, row=6, columnspan=2, pady=5)

		# Nút đăng nhập
		self.btn_login = tk.Button(self.root, text="Đăng Nhập", command=self.on_click_check_login, width=15,font=("Segoe UI", 12, "bold"),fg="white",bg="#4CAF50", activebackground="#45a049", activeforeground="white", relief="flat")
		self.btn_login.grid(row=7, column=0, padx=5, pady=8)

		# Nút thoát
		self.btn_exit = tk.Button(self.root, text="Thoát", command=self.on_click_thoat_chuong_trinh, width=5,font=("Segoe UI", 12, "bold"),fg="white",bg="#f44336", activebackground="red", activeforeground="white", relief="flat")
		self.btn_exit.grid(row=7, column=1, padx=5, pady=8)

		#Nút đăng ký
		self.btn_dangky = tk.Button(self.root, text="Đăng ký mới", font=("Segoe UI", 12), fg="red", bd=0, command=self.on_click_dang_ki)
		self.btn_dangky.grid(column=0, row=8, columnspan=2, pady=(5, 25))
	def event_enter_login(self, event= None):
		self.on_click_check_login()

	def on_click_check_login(self):
		username = self.entry_username.get()
		password = self.entry_password.get()

		password_has = 	hashlib.sha256(password.encode()).hexdigest()
		try:
			with open("data/account.json", "r", encoding="utf-8") as f:
				data = json.load(f)

			for user in data:
				if user["username"] == username and user["password"] == password_has:

					nameUser = user.get("username", "N/A")
					passwordUser = user.get("password", "N/A")
					# fullname = user.get("fullname", "N/A")
					# age = user.get("age", 0)
					# gender = user.get("gender", "Nam")
					# height = user.get("height", 0)
					# weight = user.get("weight", 0)
					# illness = user.get("illness", "Không")
					roleUser = user.get("role", "General")

					self.root.destroy()
					HomeScreen(name = nameUser,  role = roleUser)
					return

			self.label_message.config(text="Sai tài khoản hoặc mật khẩu!")

		except FileNotFoundError:
			self.label_message.config(text="Không tìm thấy file tài khoản!")
		except json.JSONDecodeError:
			self.label_message.config(text="Lỗi định dạng JSON!")
		except Exception as e:
			self.label_message.config(text=f"Lỗi: {e}")
	def on_click_dang_ki(self):
		self.root.destroy()
		DangKy()

	def on_click_thoat_chuong_trinh(self):
		"""Đóng chương trình"""
		self.root.destroy()
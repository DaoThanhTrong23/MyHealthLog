import tkinter as tk
from PIL import Image, ImageTk
import json
from tkinter import messagebox
import hashlib
from tkinter import PhotoImage

class DangKy:
	def __init__(self):
		self.root = tk.Tk()
		self.root.title("Đăng Ký")
		self.icon()
		self.setup_ui()
		self.root.mainloop()
		
	def icon(self):
		ico = Image.open('Images/logo1.png')
		photo = ImageTk.PhotoImage(ico)
		self.root.wm_iconphoto(False, photo)
		
	def setup_ui(self):
		image_path = "Images/login.png"
		img = Image.open(image_path)
		img = img.resize((95,95))
		self.photo = ImageTk.PhotoImage(img)

		#title Đăng nhập
		self.title_dangki= tk.Label(self.root ,text="Đăng ký",font=("Segoe UI", 20, "bold"))
		self.title_dangki.grid(column=0, row=0, columnspan=2)

		# Hiển thị ảnh
		self.image_label = tk.Label(self.root, image=self.photo)
		self.image_label.grid(column=0, row=1, columnspan=2)

		# Nhãn và ô nhập tên đăng nhập
		label_username = tk.Label(self.root, text="Tên đăng nhập:", font=("Segoe UI", 12))
		label_username.grid(column=0, row=2, columnspan=2, sticky="w", padx=30)
		self.entry_username = tk.Entry(self.root,width=30, font=("Segoe UI", 12), bd=2, relief="groove", highlightthickness=1, highlightcolor="#4a90e2")
		self.entry_username.grid(column=0, row=3, columnspan=2, padx=30 ,ipady=3)

		self.entry_username.bind("<KeyRelease>", self.event_check_username)

		self.label_message = tk.Label(self.root, text="", fg="red")
		self.label_message.grid(column=0, row=4, columnspan=2)

		# Nhãn và ô nhập mật khẩu
		label_password = tk.Label(self.root, text="Mật khẩu:", font=("Segoe UI", 12))
		label_password.grid(column=0, row=5, columnspan=2, padx=30, sticky="w")
		self.entry_password = tk.Entry(self.root,width=30,font=("Segoe UI", 12), show="*",bd=2, relief="groove", highlightthickness=1, highlightcolor="#4a90e2")
		self.entry_password.grid(column=0, row=6, columnspan=2, padx=30, ipady=2)
		
        # Nhãn và ô nhập lại mật khẩu
		label_password_ = tk.Label(self.root, text="Nhập lại mật khẩu:", font=("Segoe UI", 12))
		label_password_.grid(column=0, row=7, columnspan=2, sticky="w",padx =30)
		self.entry_password_re = tk.Entry(self.root,width=30,font=("Segoe UI", 12), show="*",bd=2, relief="groove", highlightthickness=1, highlightcolor="#4a90e2")
		self.entry_password_re.grid(column=0, row=8, columnspan=2, padx=30, ipady=2)
		
        #Button đăng kí
		self.danngky_btn = tk.Button(self.root, text="Đăng ký", font=("Segoe UI", 12, "bold"),fg="white",bg="#4CAF50", activebackground="#45a049", activeforeground="white", relief="flat", command=self.on_click_dang_ky)
		self.danngky_btn.grid(column=0, row=9, pady=20, ipadx=20)

		#Button hủy
		self.huy_btn = tk.Button(self.root, text="Hủy", font=("Segoe UI", 12, "bold"),fg="white",bg="#f44336", activebackground="red", activeforeground="white", relief="flat", command=self.on_click_huy)
		self.huy_btn.grid(column=1, row=9,pady=20, ipadx=20)
		#Button hủy trở lại đăng nhập
		self.huy_btn = tk.Button(self.root, text="Trở lại đăng nhập",font=("Segoe UI", 12), fg="red", bd=0, command=self.on_click_dang_nhap)
		self.huy_btn.grid(column=0, row=10, columnspan=2, pady=(10, 25))
	def event_check_username(self, event=None):
		username = self.entry_username.get()
		try:
			with open("data/account.json", "r") as file:
				data = json.load(file)
		except FileNotFoundError:
			data = []
		
		for user in data:
			if user["username"] == username:
				self.label_message.config(text="Tên đăng nhập đã được sử dụng")
				self.entry_username.config(bg="red")
				return
		self.label_message.config(text="")
		self.entry_username.config(bg="white")
	def on_click_dang_ky(self):
		name = self.entry_username.get()
		password = self.entry_password.get()
		password_re = self.entry_password_re.get()
		if not name  or not password or not password_re:
			messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")
			return
		else:
			if len(password) <6:
				messagebox.showerror("Lỗi", "Mật khẩu phải từ 6 kí tự")
				self.entry_password.delete(0 , tk.END)
				self.entry_password_re.delete(0, tk.END)
				return
			elif password != password_re:
				messagebox.showerror("Lỗi", "Vui lòng nhập lại password")
				self.entry_password_re.delete(0, tk.END)
				return
			else:
				self.save_data()
				self.entry_username.delete(0, tk.END)
				self.entry_password.delete(0,tk.END)
				self.entry_password_re.delete(0, tk.END)
				messagebox.showinfo("Thông báo", "Đăng kí tài khoản thành công!")

	def save_data(self):
		try:
			with open("data/account.json", "r", encoding="utf-8") as file1:
				data_ac = json.load(file1)
		except FileNotFoundError:
			print("Lỗi: Không tìm thấy file")
			data_ac = []

		try:
			with open("data/health.json", "r", encoding="utf-8") as file2:
				data_health = json.load(file2)
		except FileNotFoundError:
			print("Không tìm thấy file")
			data_health = []

		try:
			with open("data/exercise.json", "r", encoding="utf-8") as file3:
				data_ex = json.load(file3)
		except FileNotFoundError:
			print("Không tìm thấy file")
			data_ex = []
		
		try:
			with open("data/meal.json", "r", encoding="utf-8") as file4:
				data_meal = json.load(file4)
		except FileNotFoundError:
			print("Không tìm thấy file")
			data_meal = []

		name = self.entry_username.get()
		pas = self.entry_password.get()
		pas_has = hashlib.sha256(pas.encode()).hexdigest()

		user_ac = {
			"username": name,
        	"password": pas_has,
        	"role": "General"
		}
		user_health = {
			"username": name,
        	"fullname": "",
        	"age": "0",
        	"gender": "Nam",
        	"height": "0",
        	"weight": "0",
        	"illness": "",
			"activitylevel":"1.2",
			"goal": "Giữ cân",
		}
		user_ex = {
			"username": name,
			"exercises":[]
		}
		user_meal ={
			"username": name,
			"meals":[]
		}
		data_ac.append(user_ac)
		data_health.append(user_health)
		data_ex.append(user_ex)
		data_meal.append(user_meal)
		with open("data/account.json", "w", encoding="utf-8") as file1:
			json.dump(data_ac, file1, indent=4, ensure_ascii=False)

		with open("data/health.json", "w", encoding="utf-8") as file2:
			json.dump(data_health, file2, indent=4, ensure_ascii=False)

		with open("data/exercise.json", "w", encoding="utf-8") as file3:
			json.dump(data_ex, file3, indent=4, ensure_ascii=False)

		with open("data/meal.json", "w", encoding="utf-8") as file4:
			json.dump(data_meal, file4, indent=4, ensure_ascii=False)

	def on_click_dang_nhap(self):
		self.root.destroy()
		from login import LoginApp
		LoginApp()

	def on_click_huy(self):
		self.entry_username.delete(0, tk.END)
		self.entry_password.delete(0, tk.END)
		self.entry_password_re.delete(0, tk.END)
		
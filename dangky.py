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
		self.root.bind('<Return>')
		self.root.mainloop()
		
	def icon(self):
		ico = Image.open('Images/logo1.png')
		photo = ImageTk.PhotoImage(ico)
		self.root.wm_iconphoto(False, photo)
		
	def setup_ui(self):
		self.dangki = tk.Frame(self.root, width=200, height=200)
		self.dangki.pack(pady=20)
		
		image_path = "Images/login.png"
		img = Image.open(image_path)
		img = img.resize((95,95))
		self.photo = ImageTk.PhotoImage(img)

		#title Đăng nhập
		self.title_dangki= tk.Label(self.dangki ,text="Đăng ký",font=("Arial", 20))
		self.title_dangki.pack()

		# Hiển thị ảnh
		self.image_label = tk.Label(self.dangki, image=self.photo)
		self.image_label.pack()

		# Nhãn và ô nhập tên đăng nhập
		label_username = tk.Label(self.dangki, text="Tên đăng nhập:", font=("Arial", 12))
		label_username.pack(sticky="w", padx=20)
		self.entry_username = tk.Entry(self.dangki,width=30, font=("Arial", 12),bg="white")
		self.entry_username.pack(padx=20, ipadx=2, ipady=2)
		self.entry_username.bind("<KeyRelease>", self.check_username)

		self.label_message = tk.Label(self.dangki, text="", fg="red")
		self.label_message.pack()

		# Nhãn và ô nhập mật khẩu
		label_password = tk.Label(self.dangki, text="Mật khẩu:", font=("Arial", 12))
		label_password.pack(sticky="w", padx=20)
		self.entry_password = tk.Entry(self.dangki,width=30,font=("Arial", 12), show="*")
		self.entry_password.pack(padx=20,ipadx=2, ipady=2)
		
        # Nhãn và ô nhập lại mật khẩu
		label_password_ = tk.Label(self.dangki, text="Nhập lại mật khẩu:", font=("Arial", 12))
		label_password_.pack(sticky="w", padx =20)
		
		self.entry_password_re = tk.Entry(self.dangki,width=30,font=("Arial", 12), show="*")
		self.entry_password_re.pack(padx=20,ipadx=2, ipady=2)
		
        #Button đăng kí
		self.danngky_btn = tk.Button(self.dangki, text="Đăng ký", font=("Arial", 12), command=self.on_click_dang_ky)
		self.danngky_btn.pack(pady=20)

		#Button hủy đăng kí 
		self.huy_btn = tk.Button(self.dangki, text="Trở lại đăng nhập",font=("Arial", 12), fg="red", bd=0, command=self.on_click_dang_nhap)
		self.huy_btn.pack(pady= 20)
	def check_username(self, event=None):
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
			if password != password_re:
				messagebox.showerror("Lỗi", "Vui lòng nhập lại password")
				self.entry_password_re.delete(0, tk.END)
				return
			else:
				self.save_data()
				self.entry_username.delete(0, tk.END)
				self.entry_password.delete(0,tk.END)
				self.entry_password_re.delete(0, tk.END)

	def save_data(self, filename="data/account.json"):
		try:
			with open(filename, "r", encoding="utf-8") as f:
				data = json.load(f)
		except FileNotFoundError:
			print("Lỗi: Không tìm thấy file")
			data = []
		name = self.entry_username.get()
		pas = self.entry_password.get()
		pas_has = hashlib.sha256(pas.encode()).hexdigest()

		user = {
			"username": name,
        	"password": pas_has,
        	"fullname": " ",
        	"age": "0",
        	"gender": "nam",
        	"height": "0",
        	"weight": "0",
        	"illness": " ",
        	"role": "General"
		}
		data.append(user)
		with open(filename, "w", encoding="utf-8") as file:
			json.dump(data, file, indent=4, ensure_ascii=False)

	def on_click_dang_nhap(self):
		self.root.destroy()
		

	def thoat_chuong_trinh(self):
		self.root.destroy()
		
# if __name__=="__main__":
# 	root = tk.Tk()
# 	app = DangKy(root)
# 	root.mainloop()
import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk 
import json
from tkinter import messagebox

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
		self.btn_login = tk.Button(button_frame, text="Đăng Nhập", command=self.check_login, width=15,font=("SF Pro Display", 12))
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
				if user["nameUser"] == username and user["passwordUser"] == password:

					idUser = user.get("idUser", "N/A")
					nameUser = user.get("nameUser", "N/A")
					passwordUser = user.get("passwordUser", "N/A")
					roleUser = user.get("roleUser", "General")

					self.root.destroy()
					HomeScreen(id = idUser,name = nameUser, password = passwordUser, role = roleUser)
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

#Trang chủ 
class HomeScreen:
	def __init__(self, id, name, password, role):
		self.root = tk.Tk()
		self.id = id
		self.name = name
		self.password = password
		self.role = role

		self.root.title("MyHealthLog")
		self.root.geometry("1000x600")
		self.root.config(bg="#ecf0f1")

		# ===== Frame menu trái =====
		self.menu_frame = tk.Frame(self.root, bg="#2c3e50", width=180)
		self.menu_frame.pack(side="left", fill="y")

		# ===== Nội dung chính (bên phải) =====
		self.content_frame = tk.Frame(self.root, bg="#ecf0f1")
		self.content_frame.pack(side="right", fill="both", expand=True)

		# ===== Tiêu đề menu =====
		self.title_menu()

		# ===== Nút trong menu =====
		self.add_menu_button("Tài khoản", self.show_account)
		self.add_menu_button("Chỉ số BMI", self.show_bmi)
		self.add_menu_button("Tính Calo", self.show_calo)
		if self.role == "Manager":
			self.add_menu_button("Danh sách User", self.show_listUser)
		self.add_menu_button("Đăng Xuất", self.logout)

		# ===== Nội dung mặc định =====
		self.label_content = tk.Label(
			self.content_frame,
			text="Chào mừng đến với MyHealthLog!",
			font=("Arial", 22, "bold"),
			bg="#ecf0f1",
			fg="#2c3e50"
		)
		self.label_content.pack(pady=30)
		self.root.mainloop()

	def title_menu(self):
		title = tk.Label(
			self.menu_frame,
			text="Menu",
			font=("Arial", 16, "bold"),
			bg="#2c3e50",
			fg="white"
		)
		title.pack(pady=20)

	def add_menu_button(self, text, command):
		button = tk.Button(
			self.menu_frame,
			text=text,
			command=command,
			bg="#34495e",
			fg="white",
			font=("Arial", 12),
			relief="flat",
			activebackground="#1abc9c",
			activeforeground="white",
			#cursor="hand2"
		)
		button.pack(fill="x", pady=8, padx=10, ipady=8)


	def show_account(self):
		# Xóa nội dung cũ
		for widget in self.content_frame.winfo_children():
			widget.destroy()

		# Card chứa toàn bộ info
		card_frame = tk.Frame(self.content_frame,bg='white', height=60)
		card_frame.pack(side='top', fill='x')
		# Đảm bảo frame không co lại theo nội dung
		card_frame.pack_propagate(False)

		# Frame chính chứa avatar + info
		info_frame = tk.Frame(card_frame, bg="white")
		info_frame.pack(side='top', fill="both", expand=True)

		image_path = "Images/icon_user.png"
		img = Image.open(image_path)
		img = img.resize((40, 40))
		self.photo = ImageTk.PhotoImage(img)
		self.image_label = tk.Label(info_frame, image=self.photo, bg="white")
		self.image_label.grid(column=0, row=0, sticky='w')

		# Thông tin: Tên
		label1 = tk.Label(info_frame, text="Tên đăng nhập:", font=("Arial", 11, "bold"),bg='white', fg='black')
		label1.grid(row=0, column=1, sticky='w',padx=5)
		value1 = tk.Label(info_frame, text=self.name, font=("Arial", 11), bg="white", fg="#2c3e50")
		value1.grid(row=0, column=2, sticky='w', padx=0)

		# Thông tin: Quyền
		label2 = tk.Label(info_frame, text="Chức vụ:", font=("Arial", 11, "bold"),bg='white', fg='black')
		label2.grid(row=0, column=3, sticky='w', padx=10)
		value2 = tk.Label(info_frame, text=self.role, font=("Arial", 11), bg="white", fg="#2c3e50")
		value2.grid(row=0, column=4, sticky='w', padx=0)

		#Frame Thông tin cá nhân
		thongtincanhan_frame = tk.Frame(self.content_frame,bg='white', height=300, width=400)
		thongtincanhan_frame.pack(side='top', fill='both', expand=True)

		title_thongtincaaanhan = tk.Label(thongtincanhan_frame, text="Thông tin thể trạng cá nhân", font=("Arial", 12, "bold"),bg='white', fg='black')
		title_thongtincaaanhan.pack()

		

	def show_bmi(self):
		self.update_content("Tính chỉ số BMI")

	def show_calo(self):
		self.update_content("Tính lượng calo cần thiết")

	def show_listUser(self):
		self.update_content("Danh sách các User (Tên, Tuổi, Giới tính, Cân nặng, Chiều cao, BMI)")

	def logout(self):
		from main import LoginApp
		check = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn đăng xuất?")
		if check:
			self.root.destroy()
			LoginApp()

	def update_content(self, text):
		# Xóa nội dung cũ
		for widget in self.content_frame.winfo_children():
			widget.destroy()

		# Tạo nội dung mới (card trắng)
		card = tk.Frame(self.content_frame, bg="white", bd=2, relief="groove")
		card.pack(pady=30, padx=30, fill="both", expand=True)

		label = tk.Label(card, text=text, font=("Arial", 18), bg="white", fg="#2c3e50")
		label.pack(pady=30)


if __name__ == "__main__":
	LoginApp()

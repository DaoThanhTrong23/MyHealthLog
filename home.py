import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk 
import json
from tkinter import messagebox


class HomeScreen:
    def __init__(self,name, password,fullname, age , gender, height, weight , illness,  role):
        self.root = tk.Tk()

        self.name = name
        self.password = password
        self.fullname = fullname
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.illness = illness
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
        card_frame = tk.Frame(self.content_frame, bg='white', height=80, relief="groove", bd=2)
        card_frame.pack(side='top', fill='x', pady=10, padx=10)
        card_frame.pack_propagate(False)

    # Frame chính chứa avatar + info
        info_frame = tk.Frame(card_frame, bg="white")
        info_frame.pack(side='top', fill="both", expand=True)

    # Avatar
        image_path = "Images/icon_user.png"
        img = Image.open(image_path)
        img = img.resize((50, 50))
        self.photo = ImageTk.PhotoImage(img)
        self.image_label = tk.Label(info_frame, image=self.photo, bg="white")
        self.image_label.grid(column=0, row=0, rowspan=2, padx=5, pady=5)

    # Thông tin: Tên
        label1 = tk.Label(info_frame, text="Tên đăng nhập:", font=("Arial", 12, "bold"), bg='white', fg='black')
        label1.grid(row=0, column=1, sticky='w', padx=5)
        value1 = tk.Label(info_frame, text=self.name, font=("Arial", 12), bg="white", fg="#2c3e50")
        value1.grid(row=0, column=2, sticky='w', padx=5)

    # Thông tin: Quyền
        label2 = tk.Label(info_frame, text="Chức vụ:", font=("Arial", 12, "bold"), bg='white', fg='black')
        label2.grid(row=1, column=1, sticky='w', padx=5)
        value2 = tk.Label(info_frame, text=self.role, font=("Arial", 12), bg="white", fg="#2c3e50")
        value2.grid(row=1, column=2, sticky='w', padx=5)

    # Frame Thông tin cá nhân
        thongtincanhan_frame = tk.Frame(self.content_frame, bg='white', relief="groove", bd=2)
        thongtincanhan_frame.pack(side='top', fill='both', expand=True, pady=10, padx=10)

        title_thongtincanhan = tk.Label(
            thongtincanhan_frame,
            text="Thông tin thể trạng cá nhân",
            font=("Arial", 14, "bold"),
            bg='white',
            fg='#2c3e50'
        )
        title_thongtincanhan.pack(pady=10)

        # Frame chứa thông tin và ảnh minh họa
        main_info_frame = tk.Frame(thongtincanhan_frame, bg='white')
        main_info_frame.pack(fill='both', expand=True)

        main_info_frame.columnconfigure(0, weight=3)  # Chiếm 3 phần
        main_info_frame.columnconfigure(1, weight=2)  # Chiếm 2 phần

        thetrang_frame = tk.Frame(main_info_frame, bg='white')
        thetrang_frame.grid(row=0, column=0, padx=20, sticky='n')

        img_minhhoa = tk.Frame(main_info_frame, bg='white')
        img_minhhoa.grid(row=0, column=1, padx=20, sticky='n')

    # Helper function để tạo ô nhập liệu
        def create_input_field(parent, label_text, info):
            frame_item = tk.Frame(parent, bg='white')
            frame_item.pack(anchor='w', pady=5, fill='x')
            label = tk.Label(frame_item, text=label_text, font=("Arial", 11), bg='white', fg='black')
            label.pack(side='left', padx=5)

            entry_frame = tk.Frame(frame_item, bg='white')
            entry_frame.pack(side='left', fill='x', expand=True, padx=5)
            entry = tk.Entry(entry_frame, textvariable = info, font=("Arial", 12), bg='white', fg='black', insertbackground='black', relief='solid', bd=1)
            entry.pack(fill='both', expand=True, ipady=2, ipadx=2)
            return entry
    
        # Tạo các input field

        # Trước khi gọi create_input_field
        self.var_fullname = tk.StringVar(value=self.fullname)
        self.var_age = tk.StringVar(value=self.age)
        self.var_gender = tk.StringVar(value=self.gender)
        self.var_height = tk.StringVar(value=self.height)
        self.var_weight = tk.StringVar(value=self.weight)
        self.var_illness = tk.StringVar(value=self.illness)

        input_hoten = create_input_field(thetrang_frame, "Họ và tên:", self.var_fullname)
        input_tuoi = create_input_field(thetrang_frame, "Tuổi:", self.var_age)
        input_gioitinh = create_input_field(thetrang_frame, "Giới tính:", self.var_gender)
        input_chieucao = create_input_field(thetrang_frame, "Chiều cao (cm):", self.var_height)
        input_cannang = create_input_field(thetrang_frame, "Cân nặng (kg):", self.var_weight)
        input_benhly = create_input_field(thetrang_frame, "Bệnh lý:", self.var_illness)
    
        # Hàm cập nhật hình ảnh theo giới tính
        def update_gender_image(*args):
            self.gender = input_gioitinh.get().strip().lower()
            self.age = input_tuoi.get().strip()

            if not self.age.isdigit():
                print("Tuổi không hợp lệ: phải là số nguyên dương")
                return

            tuoi = int(self.age)

            # Chọn hình ảnh theo giới tính và độ tuổi
            if tuoi < 10:
                path = "Images/baby1.png"
            elif tuoi <18:
                path = "Images/baby2.png"
            elif self.gender== "nam":
                path = "Images/nam.png"
            else:
                path = "Images/nu.png"      

            try:
                img = Image.open(path)
                img = img.resize((100, 300))
                self.photo_gender = ImageTk.PhotoImage(img)
                image_label.config(image=self.photo_gender)
                image_label.image = self.photo_gender
            except Exception as e:
                print("Lỗi hình ảnh giới tính:", e)

        # Hiển thị ảnh ban đầu
        image_label = tk.Label(img_minhhoa, bg='white')
        image_label.pack(pady=10)
        update_gender_image()
      
        #Save Ac và update ảnh
        def save_account_and_updat_anh():
            self.save_account_info()
            update_gender_image()
        # Frame chứa nút
        button_frame = tk.Frame(thongtincanhan_frame, bg='white')
        button_frame.pack(side='bottom', fill='x', pady=10)

        save_button = tk.Button(
            button_frame,
            text="Lưu",
            font=("Arial", 12, "bold"),
            bg="#1abc9c",
            fg="white",
            relief="flat",
            padx=10,
            command=save_account_and_updat_anh
        )
        save_button.pack(side='left', padx=20, pady=5)
        

        def cancel_changes():
            try:
                with open("data/account.json", "r") as file:
                    data = json.load(file)

                for account in data:
                    if account["username"] == self.name:
                        self.var_fullname.set(account.get("fullname", ""))
                        self.var_age.set(str(account.get("age", "")))
                        self.var_gender.set(account.get("gender", ""))
                        self.var_height.set(str(account.get("height", "")))
                        self.var_weight.set(str(account.get("weight", "")))
                        self.var_illness.set(account.get("illness", ""))
                        #messagebox.showinfo("Thông báo", "Đã khôi phục dữ liệu ban đầu.")
                        update_gender_image()
                        break
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể đọc lại dữ liệu: {e}")


        cancel_button = tk.Button(
            button_frame,
            text="Hủy",
            font=("Arial", 12, "bold"),
            bg="#e74c3c",
            fg="white",
            relief="flat",
            padx=10,
            command=cancel_changes
        )
        cancel_button.pack(side='right', padx=20, pady=5)

    def save_account_info(self):
    # Load dữ liệu hiện có
        with open("data/account.json", "r", encoding="utf-8") as f:
            accounts = json.load(f)
    # Cập nhật lại tài khoản hiện tại
        for acc in accounts:
            if acc["username"] == self.name and acc["password"] == self.password:
                acc["fullname"] = self.var_fullname.get()
                acc["age"] = self.var_age.get()
                acc["gender"] = self.var_gender.get()
                acc["height"] = self.var_height.get()
                acc["weight"] = self.var_weight.get()
                acc["illness"] = self.var_illness.get()
                break

    # Ghi lại vào file
        with open("data/account.json", "w", encoding="utf-8") as f:
            json.dump(accounts, f, indent=4, ensure_ascii=False)

        messagebox.showinfo("Thông báo", "Cập nhật thông tin thành công!")

    def show_bmi(self):
        # Xóa nội dung cũ
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        try:
            weight = float(self.weight)
            height_cm = float(self.height)
            height_m = height_cm / 100

            bmi = round(weight / (height_m ** 2), 2)

        # Phân loại theo chỉ số BMI
            if bmi < 18.5:
                category = "Gầy"
            elif 18.5 <= bmi < 24.9:
                category = "Bình thường"
            elif 25 <= bmi < 29.9:
                category = "Thừa cân"
            else:
                category = "Béo phì"

            messagebox.showinfo("Chỉ số BMI", f"BMI của bạn là: {bmi} ({category})")

        except (ValueError, KeyError):
            messagebox.showerror("Lỗi", "Không thể tính BMI do thiếu dữ liệu.")



    #def show_bmi(self):
        #self.update_content("Tính chỉ số BMI")

    def show_calo(self):
        self.update_content("Tính lượng calo cần thiết")

    def show_listUser(self):
        self.update_content("list user")


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



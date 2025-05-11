import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk 
import json
from tkinter import messagebox, ttk


class HomeScreen:
    def __init__(self,name,  role):
        self.root = tk.Tk()
        self.name = name
        self.role = role
        # self.password = password
        # self.fullname = fullname
        # self.age = age
        # self.gender = gender
        # self.height = height
        # self.weight = weight
        # self.illness = illness
        

        self.root.title("MyHealthLog")
        self.root.geometry("1200x800")
        self.root.config(bg="#ecf0f1")

        #Frame menu trái
        self.menu_frame = tk.Frame(self.root, bg="#0BBBB6", width=180)
        self.menu_frame.pack(side="left", fill="y")

        #Nội dung chính (bên phải)
        self.content_frame = tk.Frame(self.root, bg="#ecf0f1")
        self.content_frame.pack(side="right", fill="both", expand=True)


        #title menu
        title = tk.Label(self.menu_frame, text="Menu", font=("Segoe UI", 20, "bold"), bg="#0BBBB6")
        title.pack(pady=20)

        #Button Tài khioan
        self.tai_khoan_btn = tk.Button(self.menu_frame,text="Tài khoản",command=self.show_account,bg="#40E0D0",fg="black",font=("Segoe UI", 12, "bold"), relief="flat",activebackground="#40E0D0",activeforeground="white")
        self.tai_khoan_btn.pack(fill="x", pady=6, padx=5, ipady=8)

        #Button Chỉ số BMI
        self.bmi_btn = tk.Button(self.menu_frame,text="Chỉ số BMI",command=self.show_bmi,bg="#40E0D0",fg="black",font=("Segoe UI", 12, "bold"), relief="flat",activebackground="#40E0D0",activeforeground="white")
        self.bmi_btn.pack(fill="x", pady=6, padx=5, ipady=8)
        
        #Button Tính calo
        self.calo_btn = tk.Button(self.menu_frame,text="Tính calo",command=self.show_calo,bg="#40E0D0",fg="black",font=("Segoe UI", 12, "bold"), relief="flat",activebackground="#40E0D0",activeforeground="white")
        self.calo_btn.pack(fill="x", pady=6, padx=5, ipady=8)

        #Button Danh sách user
        if role == "Manager":
            self.list_user_btn = tk.Button(self.menu_frame,text="Danh sách user",command=self.show_listUser,bg="#40E0D0",fg="black",font=("Segoe UI", 12, "bold"), relief="flat",activebackground="#40E0D0",activeforeground="white")
            self.list_user_btn.pack(fill="x", pady=6, padx=5, ipady=8)

        #button đăng xuất
        self.dang_xuat_btn = tk.Button(self.menu_frame,text="Đăng xuất",command=self.logout,bg="#0BBBB6",fg="red",font=("Segoe UI", 12, "bold"), bd=0,activebackground="#0BBBB6", activeforeground="white")
        self.dang_xuat_btn.pack(fill="x", pady=5, padx=5, ipady=8)

        # ===== Nội dung mặc định =====
        self.label_content = tk.Label(self.content_frame, text="Chào mừng đến với MyHealthLog!",font=("Arial", 22, "bold"), bg="#ecf0f1",fg="#2c3e50")
        self.label_content.pack(pady=30)

        self.root.mainloop()

    def show_account(self):  

        for widget in self.content_frame.winfo_children():
            widget.destroy()

        self.tai_khoan_btn.config(bg="#008080")
        self.bmi_btn.config(bg="#40E0D0")
        self.calo_btn.config(bg="#40E0D0")
        self.list_user_btn.config(bg="#40E0D0")


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

        title_thongtincanhan = tk.Label(thongtincanhan_frame,text="Thông tin thể trạng cá nhân",font=("Arial", 14, "bold"),bg='white',fg='#2c3e50')
        title_thongtincanhan.pack(pady=10)

        # Frame chứa thông tin và ảnh minh họa
        main_info_frame = tk.Frame(thongtincanhan_frame, bg='white')
        main_info_frame.pack(fill='both', expand=True)

        main_info_frame.columnconfigure(0, weight=3)  # Chiếm 3 phần
        main_info_frame.columnconfigure(1, weight=2)  # Chiếm 2 phần

        self.thetrang_frame = tk.Frame(main_info_frame, bg='white')
        self.thetrang_frame.grid(row=0, column=0, padx=10, sticky='n')

        self.img_minhhoa = tk.Frame(main_info_frame, bg='white')
        self.img_minhhoa.grid(row=0, column=1, padx=10, sticky='n')

        tk.Label(self.thetrang_frame, text="Họ và tên",font=("Segoe UI", 12), bg='white', fg='black').grid(column=0, row=0, sticky="w",pady=(0, 10))
        self.fullname_entry = tk.Entry(self.thetrang_frame,font=("Segoe UI", 12), bg='white', fg='black', insertbackground='black', relief='solid', bd=1)
        self.fullname_entry.grid(column=1, row=0, sticky="ew", pady=(0, 10), ipady=2)

        tk.Label(self.thetrang_frame, text="Tuổi", font=("Segoe UI", 12), bg='white', fg='black').grid(column=0, row=1, sticky="w", pady=(0, 10))
        self.age_entry = tk.Entry(self.thetrang_frame,font=("Segoe UI", 12), bg='white', fg='black', insertbackground='black', relief='solid', bd=1)
        self.age_entry.grid(column=1, row=1, sticky="ew", pady=(0, 10), ipady=2)

        tk.Label(self.thetrang_frame, text="Giới tính", font=("Segoe UI", 12), bg='white', fg='black').grid(column=0, row=2, sticky="w", pady=(0, 10))
        self.gender = tk.StringVar(value="Nam")
        gender_btn = tk.Radiobutton(self.thetrang_frame, text="Nam", variable= self.gender,font=("Segoe UI", 12), value="Nam", bg="white", fg="black")
        gender_btn.grid(column=1, row=2, sticky="w", pady=(0, 10))
        gender_btn = tk.Radiobutton(self.thetrang_frame, text="Nữ", variable= self.gender,font=("Segoe UI", 12), value="Nữ", bg="white", fg="black")
        gender_btn.grid(column=1, row=2, sticky="e", pady=(0, 10))
         
        tk.Label(self.thetrang_frame, text="Chiều cao (cm)",font=("Segoe UI", 12), bg='white', fg='black').grid(column=0, row=3, sticky="w", pady=(0, 10))
        self.heigth_entry = tk.Entry(self.thetrang_frame, font=("Segoe UI", 12), bg='white', fg='black', insertbackground='black', relief='solid', bd=1)
        self.heigth_entry.grid(column=1, row=3,sticky="ew", pady=(0, 10), ipady=2)

        tk.Label(self.thetrang_frame, text="Cân nặng (kg)",font=("Segoe UI", 12), bg='white', fg='black').grid(column=0, row=4,sticky="w", pady=(0, 10))
        self.weight_entry = tk.Entry(self.thetrang_frame,font=("Segoe UI", 12), bg='white', fg='black', insertbackground='black', relief='solid', bd=1)
        self.weight_entry.grid(column=1, row=4,sticky="ew", pady=(0, 10), ipady=2)

        self.weight_entry.bind("<KeyRelease>", self.tinh_bmi)

        tk.Label(self.thetrang_frame, text="Bệnh lý",font=("Segoe UI", 12), bg='white', fg='black').grid(column=0, row=5,sticky="w", pady=(0, 10))
        self.illness_entry = tk.Entry(self.thetrang_frame,font=("Segoe UI", 12), bg='white', fg='black', insertbackground='black', relief='solid', bd=1)
        self.illness_entry.grid(column=1, row=5, sticky="ew", pady=(0, 10), ipady=2)

        tk.Label(self.thetrang_frame, text="Cường độ luyện tập",font=("Segoe UI", 12), bg='white', fg='black').grid(column=0, row=6,columnspan=2, sticky="w", pady=(0, 10))

        self.activitylevel = tk.StringVar()
        self.activitylevel.set("1.2") 
        self.activity_options = {
            "Ít vận động (Ngồi nhiều, ít tập)": "1.2",
            "Hoạt động nhẹ (Đi bộ nhẹ, tập nhẹ 1-3 ngày/tuần)": "1.375",
            "Vận động vừa (Tập trung bình 3-5 ngày/tuần)": "1.55",
            "Vận động nhiều (Tập nặng 6-7 ngày/tuần)": "1.725",
            "Vận động rất nhiều 'Vận động viên' (Tập 2 buổi/ngày)": "1.9"
        }

        self.activity_combobox = ttk.Combobox(
            self.thetrang_frame,
            textvariable=self.activitylevel,
            values=list(self.activity_options.keys()),
            font=("Segoe UI", 12),
            state="readonly"
        )
        self.activity_combobox.set("Ít vận động (Ngồi nhiều, ít tập)") 
        self.activity_combobox.grid(column=0, columnspan=2, row=7, sticky="ew", padx=5, pady=5, ipady=3)

        self.activity_combobox.bind("<<ComboboxSelected>>", self.tinh_calo)

        self.bmi_label = tk.Label(self.thetrang_frame, text="Chỉ số BMI hiện tại: ",font=("Segoe UI", 12), bg='white', fg='black')
        self.bmi_label.grid(column=0, columnspan=2, row=8, sticky="w", padx=5, pady=5)

        self.calo_label = tk.Label(self.thetrang_frame, text="Calories cần thiết/ngày: ",font=("Segoe UI", 12), bg='white', fg='black')
        self.calo_label.grid(column=0, columnspan=2, row=9, sticky="w", padx=5, pady=5)

        self.goal_label = tk.Label(self.thetrang_frame, text="Mục tiêu: ",font=("Segoe UI", 12), bg='white', fg='black')
        self.goal_label.grid(column=0, row=10, sticky="w", padx=5, pady=5)

        self.goal_calo = tk.StringVar(value="Giữ cân")
        goal_calo_btn = tk.Radiobutton(self.thetrang_frame, text="Giảm cân", variable= self.goal_calo,font=("Segoe UI", 12), value="Giảm cân", bg="white", fg="black", command=self.show_entry_weight_goal)
        goal_calo_btn.grid(column=0, row=11,columnspan=2, pady=(0, 10), sticky="w")
        goal_calo_btn = tk.Radiobutton(self.thetrang_frame, text="Giữ cân", variable= self.goal_calo,font=("Segoe UI", 12), value="Giữ cân", bg="white", fg="black", command=self.show_entry_weight_goal)
        goal_calo_btn.grid(column=0, row=11,columnspan=2, pady=(0, 10))
        goal_calo_btn = tk.Radiobutton(self.thetrang_frame, text="Tăng cân", variable= self.goal_calo,font=("Segoe UI", 12), value="Tăng cân", bg="white", fg="black",command=self.show_entry_weight_goal)
        goal_calo_btn.grid(column=0, row=11,columnspan=2, pady=(0, 10), sticky="e")

        self.calo_goal_label = tk.Label(self.thetrang_frame, text="Mục tiêu Calories/ngày: ",font=("Segoe UI", 12, 'bold'), bg='white', fg='black')
        self.calo_goal_label.grid(column=0, columnspan=2, row=13, sticky="w", padx=5, pady=5)

        self.save_new_btn = tk.Button(self.thetrang_frame, text="Lưu thông tin", font=("Segoe UI", 12, 'bold'), bg="green", fg="black", bd=0)
        self.save_new_btn.grid(column=0, row=14, sticky="w",pady=10, ipadx=2, ipady=2)

        
        self.huy_btn = tk.Button(self.thetrang_frame, text="Hủy", font=("Segoe UI", 12, 'bold'),bg="red", fg="black", bd=0)
        self.huy_btn.grid(column=1, row=14, sticky="e", pady=10, ipadx=2, ipady=2)
    # def check_input(self):

    #Hàm sự kiện tính BMI
    def tinh_bmi(self, event):
        chieucao = float(self.heigth_entry.get())
        cannang = float(self.weight_entry.get())

        if chieucao <= 0:
            self.bmi_label.config(text="Chiều cao không hợp lệ")
            return

        chieu_cao_m = chieucao / 100
        self.bmi = cannang / (chieu_cao_m ** 2)
        self.bmi = round(self.bmi, 2)

        if self.bmi < 18.5:
            chandoan = "Thiếu cân"
        elif 18.5 <= self.bmi < 24.9:
            chandoan = "Bình thường"
        elif 25 <= self.bmi < 29.9:
            chandoan = "Thừa cân"
        elif 30 <= self.bmi < 34.9:
            chandoan = "Béo phì cấp độ 1"
        elif 35 <= self.bmi < 39.9:
            chandoan = "Béo phì cấp độ 2"
        else:
            chandoan = "Béo phì cấp độ 3"

        self.bmi_label.config(text=f" Chỉ số BMI hiện tại: {self.bmi} {chandoan}")

    #Hàm sự kiện tính calo 1 ngày
    def tinh_calo(self, event):
        chieucao = float(self.heigth_entry.get())
        cannang = float(self.weight_entry.get())
        tuoi = float(self.age_entry.get())
        gioitinh = self.gender.get()
        
        label = self.activity_combobox.get()  
        hoatdong = float(self.activity_options.get(label, 1.2))

        if gioitinh.lower() == 'nam':
            bmr = 10 * cannang + 6.25 * chieucao - 5 * tuoi + 5
        else:
            bmr = 10 * cannang + 6.25 * chieucao - 5 * tuoi - 161

        self.tdee = bmr * hoatdong

        self.calo_label.config(text=f'Calories cần thiết/ngày: {self.tdee}')

    #Hàm sự kiện tính calo mục tiu
    def tinh_calo_muc_tieu(self, event=None):
        

        
    def show_entry_weight_goal(self):
        if hasattr(self, 'weight_goal_label'):
            self.weight_goal_label.destroy()
        if hasattr(self, 'weight_goal'):
            self.weight_goal.destroy()

        if self.goal_calo.get() != "Giữ cân":
            self.weight_goal_label = tk.Label(self.thetrang_frame, text="Cân nặng mong muốn",font=("Segoe UI", 12), bg='white', fg='black')
            self.weight_goal_label.grid(column=0, row=12, sticky="w", pady=(0, 10))

            self.weight_goal = tk.Entry(self.thetrang_frame, font=("Segoe UI", 12),bg='white', fg='black', insertbackground='black',relief='solid', bd=1)
            self.weight_goal.grid(column=1, row=12, sticky="ew", pady=(0, 10), ipady=2)

    def save_account_info(self):
        with open("data/user_health.json", "r", encoding="utf-8") as f:
            data_accounts = json.load(f)

        for acc in data_accounts:
            if acc["username"] == self.name:
                acc["fullname"] = self.fullname_entry.get()
                acc["age"] = self.age_entry.get()
                acc["gender"] = self.gender.get()
                acc["height"] = self.heigth_entry.get()
                acc["weight"] = self.weight_entry.get()
                acc["illness"] = self.illness_entry.get()
                acc["activitylevvel"] = self.activitylevel.get()
                acc["bmi"]
                acc["calories"]
                acc["goal"]
                acc["weight_goal"]
                acc["calories_goal"]
                break


        with open("data/user_health.json", "w", encoding="utf-8") as f:
            json.dump(data_accounts, f, indent=4, ensure_ascii=False)

        messagebox.showinfo("Thông báo", "Cập nhật thông tin thành công!")















        # Helper function để tạo ô nhập liệu
        # def create_input_field(parent, label_text, info):
        #     frame_item = tk.Frame(parent, bg='white')
        #     frame_item.pack(anchor='w', pady=5, fill='x')
        #     label = tk.Label(frame_item, text=label_text, font=("Arial", 11), bg='white', fg='black')
        #     label.pack(side='left', padx=5)

        #     entry_frame = tk.Frame(frame_item, bg='white')
        #     entry_frame.pack(side='left', fill='x', expand=True, padx=5)
        #     entry = tk.Entry(entry_frame, textvariable = info, font=("Arial", 12), bg='white', fg='black', insertbackground='black', relief='solid', bd=1)
        #     entry.pack(fill='both', expand=True, ipady=2, ipadx=2)
        #     return entry
    
        # # Tạo các input field

        # # Trước khi gọi create_input_field
        # self.var_fullname = tk.StringVar(value=self.fullname)
        # self.var_age = tk.StringVar(value=self.age)
        # self.var_gender = tk.StringVar(value=self.gender)
        # self.var_height = tk.StringVar(value=self.height)
        # self.var_weight = tk.StringVar(value=self.weight)
        # self.var_illness = tk.StringVar(value=self.illness)

        # input_hoten = create_input_field(self.thetrang_frame, "Họ và tên:", self.var_fullname)
        # input_tuoi = create_input_field(self.thetrang_frame, "Tuổi:", self.var_age)
        # input_gender = create_input_field(self.thetrang_frame, "Giới tính:", self.var_gender)
        # input_chieucao = create_input_field(self.thetrang_frame, "Chiều cao (cm):", self.var_height)
        # input_cannang = create_input_field(self.thetrang_frame, "Cân nặng (kg):", self.var_weight)
        # input_benhly = create_input_field(self.thetrang_frame, "Bệnh lý:", self.var_illness)
    
        # Hàm cập nhật hình ảnh theo giới tính
        def update_gender_image(*args):
            gender = self.gender.get().strip().lower()
            age = self.age_entry.get().strip()

            if not age.isdigit():
                print("Tuổi không hợp lệ: phải là số nguyên dương")
                return

            tuoi = int(self.age_entry)

            # Chọn hình ảnh theo giới tính và độ tuổi
            if tuoi < 10:
                path = "Images/baby1.png"
            elif tuoi <18:
                path = "Images/baby2.png"
            elif gender== "nam":
                path = "Images/nam.png"
            else:
                path = "Images/nu.png"      

            try:
                img = Image.open(path)
                img = img.resize((100, 300))
                photo_gender = ImageTk.PhotoImage(img)
                image_label.config(image=photo_gender)
                image_label.image = photo_gender
            except Exception as e:
                print("Lỗi hình ảnh giới tính:", e)

        # Hiển thị ảnh ban đầu
        image_label = tk.Label(self.img_minhhoa, bg='white')
        image_label.pack(pady=10)
        update_gender_image()
      
        #Save Ac và update ảnh
        def save_account_and_updat_anh():
            self.save_account_info()
            update_gender_image()
        # Frame chứa nút
        button_frame = tk.Frame(self.thetrang_frame, bg='white')
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


        cancel_button = tk.Button(button_frame,text="Hủy",font=("Arial", 12, "bold"),bg="#e74c3c",fg="white",relief="flat",padx=10,command=cancel_changes)
        cancel_button.pack(side='right', padx=20, pady=5)


    def show_bmi(self):
        # Xóa nội dung cũ
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        self.tai_khoan_btn.config(bg="#40E0D0")
        self.bmi_btn.config(bg="#008080")
        self.calo_btn.config(bg="#40E0D0")
        self.list_user_btn.config(bg="#40E0D0")
 
        
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
        self.tai_khoan_btn.config(bg="#40E0D0")
        self.bmi_btn.config(bg="#40E0D0")
        self.calo_btn.config(bg="#008080")
        self.list_user_btn.config(bg="#40E0D0")
 
        
        self.update_content("Tính lượng calo cần thiết")

    def show_listUser(self):
        self.tai_khoan_btn.config(bg="#40E0D0")
        self.bmi_btn.config(bg="#40E0D0")
        self.calo_btn.config(bg="#40E0D0")
        self.list_user_btn.config(bg="#008080")
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Tiêu đề
        self.title_list = tk.Label(self.content_frame, text="Danh sách người dùng", font=("Segoe UI", 15, "bold"))
        self.title_list.grid(column=0, row=0, columnspan=4, pady=10)

        columns = ["stt", "user", "fullname", "age", "gender", "height", "weight", "illness", "role"]
        self.list_user = ttk.Treeview(self.content_frame, columns=columns, show="headings", height=10)
        self.list_user.grid(column=0, row=1, columnspan=4, sticky="snew", pady=5, padx=5)


        self.list_user.heading("stt", text="Số thứ tự")
        self.list_user.heading("user", text="Tên đăng nhập")
        self.list_user.heading("fullname", text="Họ và tên")
        self.list_user.heading("age", text="Tuổi")
        self.list_user.heading("gender", text="Giới tính")
        self.list_user.heading("height", text="Chiều cao")
        self.list_user.heading("weight", text="Cân nặng")
        self.list_user.heading("illness", text="Bệnh lý")
        self.list_user.heading("role", text="Quyền truy cập")

        self.list_user.column("stt", width=80)
        self.list_user.column("user", width=150)
        self.list_user.column("fullname", width=200)
        self.list_user.column("age", width=80)
        self.list_user.column("gender", width=100)
        self.list_user.column("height", width=100)
        self.list_user.column("weight", width=100)
        self.list_user.column("illness", width=200)
        self.list_user.column("role", width=120)


        try:
            with open("data/account.json", "r", encoding="utf-8") as file:
                self.user_data = json.load(file)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể đọc dữ liệu: {e}")
            return
        for stt, user in enumerate(self.user_data):
            self.list_user.insert("", tk.END, values=(
                stt + 1,
                user.get("username", ""),
                user.get("fullname", ""),
                user.get("age", ""),
                user.get("gender", ""),
                user.get("height", ""),
                user.get("weight", ""),
                user.get("illness", ""),
                user.get("role", "")
            ))


        # Nút Sửa và Xoá (tùy chọn)
        self.edit_btn = tk.Button(self.content_frame, text="Sửa", bg="#3498db", fg="white", width=10)
        self.edit_btn.grid(column=1, row=2, pady=10)

        self.delete_btn = tk.Button(self.content_frame, text="Xoá", bg="#e74c3c", fg="white", width=10)
        self.delete_btn.grid(column=2, row=2, pady=10)



    def logout(self):
        self.tai_khoan_btn.config(bg="#40E0D0")
        self.bmi_btn.config(bg="#40E0D0")
        self.calo_btn.config(bg="#40E0D0")
        self.list_user_btn.config(bg="#40E0D0")

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



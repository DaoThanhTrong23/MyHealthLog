import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk 
import json
from tkinter import messagebox, ttk
from datetime import datetime

class HomeScreen:
    def __init__(self,name,  role):
        self.root = tk.Tk()
        self.name = name
        self.role = role
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

        #Button luyện tập
        self.luyen_tap_btn = tk.Button(self.menu_frame,text="Luyện tập",command=self.show_luyen_tap,bg="#40E0D0",fg="black",font=("Segoe UI", 12, "bold"), relief="flat",activebackground="#40E0D0",activeforeground="white")
        self.luyen_tap_btn.pack(fill="x", pady=6, padx=5, ipady=8)
        
        #Button dinh dưỡng
        self.dinh_duong_btn = tk.Button(self.menu_frame,text="Dinh dưỡng",command=self.show_dinh_duong,bg="#40E0D0",fg="black",font=("Segoe UI", 12, "bold"), relief="flat",activebackground="#40E0D0",activeforeground="white")
        self.dinh_duong_btn.pack(fill="x", pady=6, padx=5, ipady=8)
        

        #Button theo dõi
        self.theo_doi_btn = tk.Button(self.menu_frame,text="Theo dõi",command=self.show_theo_doi,bg="#40E0D0",fg="black",font=("Segoe UI", 12, "bold"), relief="flat",activebackground="#40E0D0",activeforeground="white")
        self.theo_doi_btn.pack(fill="x", pady=6, padx=5, ipady=8)


        #Button Danh sách user
        self.list_user_btn = tk.Button(self.menu_frame,text="Danh sách user",command=self.show_listUser,bg="#40E0D0",fg="black",font=("Segoe UI", 12, "bold"), relief="flat",activebackground="#40E0D0",activeforeground="white")
        if role == "Manager":
            self.list_user_btn.pack(fill="x", pady=6, padx=5, ipady=8)

        #button đăng xuất
        self.dang_xuat_btn = tk.Button(self.menu_frame,text="Đăng xuất",command=self.logout,bg="#0BBBB6",fg="red",font=("Segoe UI", 12, "bold"), bd=0,activebackground="#0BBBB6", activeforeground="white")
        self.dang_xuat_btn.pack(fill="x", side='bottom', pady=20, padx=5, ipady=8)
        
        #gọi lại các chức năng để fill dữ liệu
        self.show_account()
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        self.show_luyen_tap()
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        self.show_dinh_duong()
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        self.show_theo_doi()
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        self.show_listUser()
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        self.tai_khoan_btn.config(bg="#40E0D0")
        self.luyen_tap_btn.config(bg="#40E0D0")
        self.dinh_duong_btn.config(bg="#40E0D0")
        self.theo_doi_btn.config(bg="#40E0D0")
        self.list_user_btn.config(bg="#40E0D0")
        

        # ===== Nội dung mặc định =====
        label_content = tk.Label(self.content_frame, text="Chào mừng đến với MyHealthLog!",font=("Arial", 22, "bold"), bg="#ecf0f1",fg="#2c3e50")
        label_content.pack(pady=30)
        image_path = "Images/logo1.png"
        img = Image.open(image_path)
        img = img.resize((300, 300))
        photo = ImageTk.PhotoImage(img)
        image_label = tk.Label(self.content_frame, image=photo, bg=None)
        image_label.pack(pady=30, anchor="center")
        slogan = tk.Label(self.content_frame, text=" “Lắng nghe cơ thể - Chủ động thay đổi” ", font=("Segoe UI", 20, "italic", "bold"))
        slogan.pack(pady=30, anchor="center")


        self.icon()
        self.root.mainloop()

    def icon(self):
        ico = Image.open('Images/logo1.png')
        photo = ImageTk.PhotoImage(ico)
        self.root.wm_iconphoto(False, photo)

    def fill_data_update(self):
        with open("data/health.json", "r", encoding="utf-8") as f:
            data_accounts = json.load(f)

        for acc in data_accounts:
            if acc["username"] == self.name:
                self.var_fullname.set(acc.get("fullname", ""))
                self.var_age.set(acc.get("age", ""))
                self.var_gender.set(acc.get("gender", "Nam"))
                self.var_heigth.set(acc.get("height", ""))
                self.var_weight.set(acc.get("weight", ""))
                self.var_illness.set(acc.get("illness", ""))
                self.var_activitylevel.set(acc.get("activitylevel", "1.2"))
                self.var_goal.set(acc.get("goal", "Giữ cân"))
                break
    #_____________________________________________________________________TÀI KHOẢN__________________________________________________
    def show_account(self): 
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        self.tai_khoan_btn.config(bg="#008080")
        self.luyen_tap_btn.config(bg="#40E0D0")
        self.dinh_duong_btn.config(bg="#40E0D0")
        self.theo_doi_btn.config(bg="#40E0D0")
        self.list_user_btn.config(bg="#40E0D0")

        self.var_fullname = tk.StringVar()
        self.var_age = tk.StringVar()
        self.var_gender = tk.StringVar(value="Nam")  # mặc định
        self.var_heigth = tk.StringVar()
        self.var_weight = tk.StringVar()
        self.var_illness = tk.StringVar()
        self.var_activitylevel = tk.StringVar(value="1.2")
        self.var_goal = tk.StringVar()  
        self.fill_data_update()
        
        
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
        title_thongtincanhan.pack(pady=20)

        # Frame chứa thông tin và ảnh minh họa
        main_info_frame = tk.Frame(thongtincanhan_frame, bg='white')
        main_info_frame.pack(fill='both', expand=True, pady=20)

        main_info_frame.columnconfigure(0, weight=3)  # Chiếm 3 phần
        main_info_frame.columnconfigure(1, weight=2)  # Chiếm 2 phần

        main_info_frame.grid_rowconfigure(0, weight=1)
        main_info_frame.grid_columnconfigure(0, weight=1)


        self.thetrang_frame = tk.Frame(main_info_frame, bg='white')
        self.thetrang_frame.grid(row=0, column=0, padx=(10, 2), sticky='n')

        self.img_minhhoa = tk.Frame(main_info_frame, bg='white')
        self.img_minhhoa.grid(row=0, column=1, padx=(2, 10), sticky='n')

        tk.Label(self.thetrang_frame, text="Họ và tên",font=("Segoe UI", 12), bg='white', fg='black').grid(column=0, row=0, sticky="w",pady=(0, 10))
        self.fullname_entry = tk.Entry(self.thetrang_frame,font=("Segoe UI", 12),textvariable=self.var_fullname, bg='white', fg='black', insertbackground='black', relief='solid', bd=1)
        self.fullname_entry.grid(column=1, row=0, sticky="ew", pady=(0, 10), ipady=2)

        tk.Label(self.thetrang_frame, text="Tuổi", font=("Segoe UI", 12), bg='white', fg='black').grid(column=0, row=1, sticky="w", pady=(0, 10))
        self.age_entry = tk.Entry(self.thetrang_frame,font=("Segoe UI", 12),textvariable=self.var_age, bg='white', fg='black', insertbackground='black', relief='solid', bd=1)
        self.age_entry.grid(column=1, row=1, sticky="ew", pady=(0, 10), ipady=2)
        #self.age_entry.bind("<KeyRelease>", self.update_gender_image)
        self.age_entry.bind("<KeyRelease>", self.tinh_bmi_calo_gioitingimg_event)

        tk.Label(self.thetrang_frame, text="Giới tính", font=("Segoe UI", 12), bg='white', fg='black').grid(column=0, row=2, sticky="w", pady=(0, 10))
        # self.gender = tk.StringVar(value="Nam")
        self.gender = self.var_gender
        gender_btn = tk.Radiobutton(self.thetrang_frame, text="Nam", variable= self.gender,font=("Segoe UI", 12), value="Nam", bg="white", fg="black")
        gender_btn.grid(column=1, row=2, sticky="w", pady=(0, 10))
        gender_btn = tk.Radiobutton(self.thetrang_frame, text="Nữ", variable= self.gender,font=("Segoe UI", 12), value="Nữ", bg="white", fg="black")
        gender_btn.grid(column=1, row=2, sticky="e", pady=(0, 10))
        gender_btn.bind("<Button-1>", self.tinh_bmi_calo_gioitingimg_event)
        
         
        tk.Label(self.thetrang_frame, text="Chiều cao (cm)",font=("Segoe UI", 12), bg='white', fg='black').grid(column=0, row=3, sticky="w", pady=(0, 10))
        self.heigth_entry = tk.Entry(self.thetrang_frame, font=("Segoe UI", 12),textvariable=self.var_heigth, bg='white', fg='black', insertbackground='black', relief='solid', bd=1)
        self.heigth_entry.grid(column=1, row=3,sticky="ew", pady=(0, 10), ipady=2)
        self.heigth_entry.bind("<KeyRelease>", self.tinh_bmi_calo_gioitingimg_event)

        tk.Label(self.thetrang_frame, text="Cân nặng (kg)",font=("Segoe UI", 12), bg='white', fg='black').grid(column=0, row=4,sticky="w", pady=(0, 10))
        self.weight_entry = tk.Entry(self.thetrang_frame,font=("Segoe UI", 12),textvariable=self.var_weight, bg='white', fg='black', insertbackground='black', relief='solid', bd=1)
        self.weight_entry.grid(column=1, row=4,sticky="ew", pady=(0, 10), ipady=2)
        self.weight_entry.bind("<KeyRelease>", self.tinh_bmi_calo_gioitingimg_event)

        tk.Label(self.thetrang_frame, text="Bệnh lý",font=("Segoe UI", 12), bg='white', fg='black').grid(column=0, row=5,sticky="w", pady=(0, 10))
        self.illness_entry = tk.Entry(self.thetrang_frame,font=("Segoe UI", 12),textvariable=self.var_illness, bg='white', fg='black', insertbackground='black', relief='solid', bd=1)
        self.illness_entry.grid(column=1, row=5, sticky="ew", pady=(0, 10), ipady=2)

        tk.Label(self.thetrang_frame, text="Cường độ luyện tập",font=("Segoe UI", 12), bg='white', fg='black').grid(column=0, row=6,columnspan=2, sticky="w", pady=(0, 10))

        self.activity_options = {
            "Ít vận động (Ngồi nhiều, ít tập)": "1.2",
            "Hoạt động nhẹ (Đi bộ nhẹ, tập nhẹ 1-3 ngày/tuần)": "1.375",
            "Vận động vừa (Tập trung bình 3-5 ngày/tuần)": "1.55",
            "Vận động nhiều (Tập nặng 6-7 ngày/tuần)": "1.725",
            "Vận động rất nhiều 'Vận động viên' (Tập 2 buổi/ngày)": "1.9"
        }

        default_desc = self.get_activity_description_from_value(self.var_activitylevel.get())

        self.activity_combobox = ttk.Combobox(self.thetrang_frame,values=list(self.activity_options.keys()),font=("Segoe UI", 10),state="readonly")
        if default_desc:
            self.activity_combobox.set(default_desc)

        self.activity_combobox.grid(column=0, columnspan=2, row=7, sticky="ew", padx=5, pady=5, ipady=3)
        self.activity_combobox.bind("<<ComboboxSelected>>", self.tinh_bmi_calo_gioitingimg_event)

        self.bmi_label = tk.Label(self.thetrang_frame, text="Chỉ số BMI hiện tại: ",font=("Segoe UI", 12), bg='white', fg='black')
        self.bmi_label.grid(column=0, columnspan=2, row=8, sticky="w", padx=5, pady=5)

        self.calo_label = tk.Label(self.thetrang_frame, text="Calories cần thiết/ngày: ",font=("Segoe UI", 12), bg='white', fg='black')
        self.calo_label.grid(column=0, columnspan=2, row=9, sticky="w", padx=5, pady=5)

        self.goal_label = tk.Label(self.thetrang_frame, text="Mục tiêu: ",font=("Segoe UI", 12), bg='white', fg='black')
        self.goal_label.grid(column=0, row=10, sticky="w", padx=5, pady=5)

        self.goal_calo = self.var_goal
        goal_calo_btn = tk.Radiobutton(self.thetrang_frame, text="Giảm cân", variable= self.goal_calo,font=("Segoe UI", 12), value="Giảm cân", bg="white", fg="black")
        goal_calo_btn.grid(column=0, row=11,columnspan=2, pady=(0, 10), sticky="w")
        goal_calo_btn = tk.Radiobutton(self.thetrang_frame, text="Giữ cân", variable= self.goal_calo,font=("Segoe UI", 12), value="Giữ cân", bg="white", fg="black")
        goal_calo_btn.grid(column=0, row=11,columnspan=2, pady=(0, 10))
        goal_calo_btn = tk.Radiobutton(self.thetrang_frame, text="Tăng cân", variable= self.goal_calo,font=("Segoe UI", 12), value="Tăng cân", bg="white", fg="black")
        goal_calo_btn.grid(column=0, row=11,columnspan=2, pady=(0, 10), sticky="e")
        

        self.save_new_btn = tk.Button(self.thetrang_frame, text="Lưu thông tin", font=("Segoe UI", 12, 'bold'), bg="green", fg="black", bd=0, command=self.save_account_info)
        self.save_new_btn.grid(column=0, row=12, sticky="w",pady=10, ipadx=2, ipady=2)

        self.huy_btn = tk.Button(self.thetrang_frame, text="Hủy", font=("Segoe UI", 12, 'bold'),bg="red", fg="black", bd=0)
        self.huy_btn.grid(column=1, row=12, sticky="e", pady=10, ipadx=2, ipady=2)

        self.tinh_bmi()
        self.tinh_calo()
        self.update_gender_image()

    def get_activity_description_from_value(self, value):
        for desc, val in self.activity_options.items():
            if val == value:
                return desc
        return None

    # def check_input(self)
    def tinh_bmi_calo_gioitingimg_event(self, event):
        self.tinh_bmi()
        self.tinh_calo()
        self.update_gender_image()
    #Hàm sự kiện tính BMI
    def tinh_bmi(self):
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
        return self.bmi

    #Hàm sự kiện tính calo 1 ngày
    def tinh_calo(self):
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
        self.calo_label.config(text=f'Calories cần thiết/ngày: {self.tdee} kcal')        
        return self.tdee

    def save_account_info(self):

        with open("data/health.json", "r", encoding="utf-8") as f:
            data_accounts = json.load(f)

        for acc in data_accounts:
            if acc["username"] == self.name:
                acc["fullname"] = self.fullname_entry.get()
                acc["age"] = self.age_entry.get()
                acc["gender"] = self.gender.get()
                acc["height"] = self.heigth_entry.get()
                acc["weight"] = self.weight_entry.get()
                acc["illness"] = self.illness_entry.get()
                selected_desc = self.activity_combobox.get()
                acc["activitylevel"] = self.activity_options.get(selected_desc, "1.2")
                acc["goal"] = self.goal_calo.get()
                break

        with open("data/health.json", "w", encoding="utf-8") as f:
            json.dump(data_accounts, f, indent=4, ensure_ascii=False)

        messagebox.showinfo("Thông báo", "Cập nhật thông tin thành công!")

    def update_gender_image(self):
        gender = self.gender.get()
        age = self.age_entry.get()
        try:
            tuoi = int(age)
        except ValueError:
            print("Tuổi không hợp lệ")
            return
        if tuoi < 10:
            path = "Images/baby1.png"
        elif tuoi < 18:
            path = "Images/baby2.png"
        elif gender == "Nam":
            path = "Images/nam.png"
        else:
            path = "Images/nu.png"
        try:
            if hasattr(self, "anhminhhoa") and self.anhminhhoa is not None:
                self.anhminhhoa.destroy()
            img = Image.open(path)
            img = img.resize((180, 400))
            photo_gender = ImageTk.PhotoImage(img)
            self.anhminhhoa = tk.Label(self.img_minhhoa, image=photo_gender, bg="white")
            self.anhminhhoa.image = photo_gender
            self.anhminhhoa.pack(pady=5, side="left")
        except Exception as e:
            print("Lỗi hình ảnh giới tính:", e)


    #__________________________________________________________LUYỆN TẬP______________________________________________________________________
    def show_luyen_tap(self):
        # Xóa nội dung cũ
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        self.tai_khoan_btn.config(bg="#40E0D0")
        self.luyen_tap_btn.config(bg="#008080")
        self.dinh_duong_btn.config(bg="#40E0D0")
        self.theo_doi_btn.config(bg="#40E0D0")
        self.list_user_btn.config(bg="#40E0D0")
                                                              
        tk.Label(self.content_frame, text="Luyện tập", font=("Segoe UI", 14, "bold")).grid(column=0, row=0, columnspan=2, sticky='ew', pady=(10, 25))
        self.content_frame.grid_rowconfigure(1, weight=1)
        self.content_frame.grid_rowconfigure(2, weight=0)

        self.content_frame.grid_columnconfigure(1, weight=1)
        self.content_frame.columnconfigure(0, weight=2)  
        self.content_frame.columnconfigure(1, weight=3) 
        # --- FRAME NHẬP ---
        self.input_frame = tk.Frame(self.content_frame, bg="white", bd=1, relief="solid")
        self.input_frame.grid(column=0, row=1, padx=5, pady=10, sticky="nsew")

        tk.Label(self.input_frame, text="Thông tin tập luyện",font=("Segoe UI", 15),bg="white").pack(pady=15)
        tk.Label(self.input_frame, text="Loại bài tập", bg="white", font=("Segoe UI", 12)).pack(pady=5, anchor='w')
        self.exercise_options = ["Chạy bộ", "Đi bộ", "Đạp xe", "Tập gym", "Yoga", "Bơi lội", "Nhảy dây", "Khác"]
        self.exercise_type_combobox = ttk.Combobox(self.input_frame, values=self.exercise_options, font=("Segoe UI", 12), state="readonly")
        self.exercise_type_combobox.current(0)
        self.exercise_type_combobox.pack(pady=5,padx=5, fill='x')
        self.exercise_type_combobox.bind("<<ComboboxSelected>>", self.update_calo_estimate_event)


        tk.Label(self.input_frame, text="Thời lượng (phút):", bg="white", font=("Segoe UI", 12)).pack(pady=5)
        self.duration_entry= tk.Entry(self.input_frame, font=("Segoe UI", 12),bg='white', fg='black')
        self.duration_entry.pack(padx=5,fill='x')
        self.duration_entry.bind("<KeyRelease>", self.update_calo_estimate_event)

        # Calo ước tính
        self.calo_label = tk.Label(self.input_frame, text="Calo ước tính: -", bg="white", font=("Segoe UI", 12, "italic"))
        self.calo_label.pack(pady=10, padx=5)

        tk.Button(self.input_frame, text="Lưu thông tin", bg="green", fg="black", font=("Segoe UI", 12), command=self.save_data_exercise).pack(pady=10, padx=5, fill='x', ipady=2)
        
        tk.Button(self.input_frame, text="Thay đổi",bg="yellow",fg="black", font=("Segoe UI", 12), command=self.update_selected_exercise).pack(pady=5, fill='x', padx=5, ipady=2)
        tk.Button(self.input_frame, text="Xóa",bg="red", fg="black", font=("Segoe UI", 12), command=self.delete_selected_exercise).pack(pady=5, fill='x', padx=5, ipady=2)

        huy = tk.Button(self.input_frame, text="Hủy", bg="white", bd=0, fg="red",font=("Segoe UI", 12), command=self.on_click_huy_them)
        huy.pack(pady=10)

        # --- FRAME LỊCH SỬ ---
        history_frame = tk.Frame(self.content_frame, bg="white", bd=1, relief="solid")
        history_frame.grid(column=1, row=1, padx=10, pady=10, sticky="nsew")
        

        tk.Label(history_frame, text="Lịch sử buổi tập", bg="white", font=("Segoe UI", 13, "bold")).pack(pady=5)

        columns = ("date", "type", "duration", "calories")
        self.exercise_tree = ttk.Treeview(history_frame, columns=columns, show="headings")
        self.exercise_tree.heading("date", text="Ngày")
        self.exercise_tree.heading("type", text="Loại tập")
        self.exercise_tree.heading("duration", text="Thời lượng (phút)")
        self.exercise_tree.heading("calories", text="Calo")

        try:
            with open("data/exercise.json", "r", encoding="utf-8") as file:
                data_ex = json.load(file)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể đọc dữ liệu: {e}")
            return
        for user in data_ex:
            if user["username"] == self.name:
                for ex in user['exercises']:
                    self.exercise_tree.insert("", tk.END, values=(ex.get("date",""),ex.get("exercise_type",""), ex.get("duration",""), ex.get("calories","") ))

        self.exercise_tree.pack(fill="both", expand=True, padx=10, pady=5)
        self.exercise_tree.bind("<<TreeviewSelect>>", self.on_exercise_select)
        self.selected_exercise_index = None 

        self.exercise_mets = {"Chạy bộ": 9.8, "Đi bộ": 3.8, "Đạp xe": 7.5, "Tập gym": 6.0,"Yoga": 2.5, "Bơi lội": 8.0, "Nhảy dây": 12.3,"Khác": 5.0}

    def on_click_huy_them(self):
        self.duration_entry.delete(0, tk.END)
        self.update_calo_estimate()

    def update_calo_estimate_event(self, event=None):
        self.update_calo_estimate()
    def update_calo_estimate(self):
        try:
            exercise_type = self.exercise_type_combobox.get()
            duration = float(self.duration_entry.get())
            weight = float(self.var_weight.get()) 
            met = self.exercise_mets.get(exercise_type, 5.0)
            calories = round(met * weight * (duration / 60), 2)
            self.calo_label.config(text=f"Calo ước tính: {calories} kcal")
        except:
            self.calo_label.config(text="Calo ước tính: -")

    def save_data_exercise(self):
        if not self.duration_entry.get():
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin")
            return
        
        try:
            exercise_type = self.exercise_type_combobox.get()
            duration = float(self.duration_entry.get())
            weight = float(self.var_weight.get())
            met = self.exercise_mets.get(exercise_type, 5.0)
            calories = round(met * weight * (duration / 60), 2)

            today_str = datetime.now().strftime("%d-%m-%Y") 
            # test--------------------------
        
            new_exercise = {
                "date": today_str,
                "exercise_type": exercise_type,
                "duration": duration,
                "calories": calories
            }
        
            with open("data/exercise.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            for user in data:
                if user["username"] == self.name:
                    user["exercises"].append(new_exercise)
                    break
            else:
                messagebox.showerror("Lỗi", "Không tìm thấy người dùng.")
                return
            with open("data/exercise.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                
            messagebox.showinfo("Thành công", "Đã lưu bài tập.")
            self.show_luyen_tap()

        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể lưu dữ liệu: {str(e)}")

    def on_exercise_select(self, event=None):
        selected = self.exercise_tree.selection()
        if selected:
            item = self.exercise_tree.item(selected[0])
            values = item["values"]
            date, exercise_type, duration, calories = values
            self.exercise_type_combobox.set(exercise_type)
            self.duration_entry.delete(0, tk.END)
            self.duration_entry.insert(0, duration)
            self.calo_label.config(text=f"Calo ước tính: {calories} kcal")

    def delete_selected_exercise(self):
        selected = self.exercise_tree.selection()
        if selected:
            item = self.exercise_tree.item(selected[0])
            values = item["values"]
            date, exercise_type, duration, calories = values
            
            self.exercise_type_combobox.set(exercise_type)
            self.duration_entry.delete(0, tk.END)
            self.duration_entry.insert(0, duration)
            self.calo_label.config(text=f"Calo ước tính: {calories} kcal")

            with open("data/exercise.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            for user in data:
                if user["username"] == self.name:
                    for i, ex in enumerate(user["exercises"]):
                        if (ex["date"], ex["exercise_type"], str(ex["duration"]), str(ex["calories"])) == tuple(map(str, values)):
                            self.selected_exercise_index = i
                            break
                        
        if self.selected_exercise_index is None:
            messagebox.showwarning("Chưa chọn bài tập", "Vui lòng chọn bài tập để xóa.")
            return

        confirm = messagebox.askyesno("Xác nhận", "Bạn chắc chắn muốn xóa bài tập này?")
        if not confirm:
            return

        with open("data/exercise.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        for user in data:
            if user["username"] == self.name:
                user["exercises"].pop(self.selected_exercise_index)
                break

        with open("data/exercise.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        self.refresh_exercise_tree()
        self.duration_entry.delete(0, tk.END)
        self.selected_exercise_index = None
        messagebox.showinfo("Thành công", "Đã xóa bài tập.")
    
    
    def update_selected_exercise(self):
        selected = self.exercise_tree.selection()
        if selected:
            item = self.exercise_tree.item(selected[0])
            values = item["values"]
            date, old_type, old_duration, old_calories = values

            with open("data/exercise.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            exercise_type = self.exercise_type_combobox.get()
            duration = float(self.duration_entry.get())
            weight = float(self.var_weight.get())
            met = self.exercise_mets.get(exercise_type, 5.0)
            calories = round(met * weight * (duration / 60), 2)
            self.calo_label.config(text=f"Calo ước tính: {calories} kcal")


            found = False
            for user in data:
                if user["username"] == self.name:
                    for i, ex in enumerate(user["exercises"]):
                        if (ex["date"], ex["exercise_type"], str(ex["duration"]), str(ex["calories"])) == tuple(map(str, values)):
                            ex["exercise_type"] = exercise_type
                            ex["duration"] = duration
                            ex["calories"] = calories
                            found = True
                            break

            if not found:
                messagebox.showwarning("Không tìm thấy", "Không tìm thấy bài tập để cập nhật.")
                return

            with open("data/exercise.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            self.refresh_exercise_tree()
            self.duration_entry.delete(0, tk.END)
            self.selected_exercise_index = None
            messagebox.showinfo("Thành công", "Đã cập nhật bài tập.")

    def refresh_exercise_tree(self):
        for row in self.exercise_tree.get_children():
            self.exercise_tree.delete(row)

        with open("data/exercise.json", "r", encoding="utf-8") as file:
            data_ex = json.load(file)

        for user in data_ex:
            if user["username"] == self.name:
                for ex in user['exercises']:
                    self.exercise_tree.insert("", tk.END, values=(
                        ex.get("date", ""),
                        ex.get("exercise_type", ""),
                        ex.get("duration", ""),
                        ex.get("calories", "")
                    ))

    #______________________________________________________________________Dinh dưỡng_________________________________________________________________
    def show_dinh_duong(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        self.tai_khoan_btn.config(bg="#40E0D0")
        self.luyen_tap_btn.config(bg="#40E0D0")
        self.dinh_duong_btn.config(bg="#008080")
        self.theo_doi_btn.config(bg="#40E0D0")
        self.list_user_btn.config(bg="#40E0D0")

        self.content_frame.grid_rowconfigure(1, weight=1)
        self.content_frame.grid_rowconfigure(2, weight=1)

        tk.Label(self.content_frame, text="Chế độ ăn uống",font=("Segoe UI", 18,"bold")).grid(column=0, row=0, pady=10, columnspan=2)
        #_______________________________________nhập phần ăn
        self.frame_input = tk.Frame(self.content_frame, bg="white", bd=1)
        self.frame_input.grid(column=0, row=1,pady=5, padx=(10, 5), sticky="snwe")
        self.frame_input.columnconfigure(0, weight=1)
        self.frame_input.columnconfigure(1, weight=1)
        self.frame_input.columnconfigure(2, weight=1)
        self.frame_input.columnconfigure(3, weight=1)
        self.frame_input.columnconfigure(4, weight=1)


        tk.Label(self.frame_input, text="Thực đơn bửa ăn",font=("Segoe UI", 15), fg="black",bg="white").grid(row=0, column=0, columnspan=5,padx=10, sticky="ew")
        tk.Label(self.frame_input, text="Món ăn",font=("Segoe UI", 11), fg="black", bg="white").grid(row=1,padx=10, column=0, columnspan=5, sticky="w")
        self.monan_options = [
            "chuối", "táo", "cam", "gạo", "ức gà", "bò bít tết", "sườn heo",
            "cá hồi", "trứng", "bánh mì", "sữa", "phô mai", "sữa chua", "khoai tây", "cà rốt", "cà chua",
            "bông cải xanh", "rau bina", "bơ", "hạnh nhân", "óc chó", "bơ đậu phộng", "yến mạch",
            "mì ống", "pizza", "hamburger", "cơm chiên", "mì sợi", "đậu hũ", "đậu lăng", "đậu gà",
            "đậu đen", "đậu que", "dưa leo", "hành tây", "tỏi", "nấm", "tôm",
            "cua", "tôm hùm", "gà tây", "vịt", "thịt xông khói", "xúc xích", "bơ", "dầu ô liu",
            "đường", "mật ong", "sô cô la", "bánh kem", "bánh quy", "kem", "cà phê", "trà",
            "nước cam", "nước táo", "bia", "rượu vang", "dưa hấu", "nho", "dứa",
            "dâu tây", "việt quất", "mâm xôi", "đào", "lê", "mận", "anh đào",
            "bắp", "khoai lang", "bí đỏ", "bí xanh", "súp lơ", "cải xoăn", "rau xà lách",
            "củ dền", "bắp cải", "củ cải đỏ", "đậu Hà Lan", "đậu nành non", "hạt diêm mạch", "hạt chia",
            "hạt lanh", "dừa", "sữa hạnh nhân", "sữa đậu nành", "kem tươi", "sốt mayonnaise",
            "tương cà", "mù tạt", "sốt salsa", "súp", "bánh sandwich", "gà rán", "viên thịt",
            "cá", "sushi", "mì ramen", "há cảo"
        ]
        
        self.mon_an_type_entry = tk.Entry(self.frame_input, font=("Segoe UI", 12))
        self.mon_an_type_entry.grid(row=2, column=0,padx=10, columnspan=5, sticky="ew")
        self.mon_an_type_entry.bind("<KeyRelease>", self.search_type_mon_an_event)

        self.mon_an_type_listbox = tk.Listbox(self.frame_input,font=("Segoe UI", 11), height=5)
        self.mon_an_type_listbox.grid(row=3,padx=10, column=0, columnspan=5, sticky='ew')
        self.mon_an_type_listbox.bind("<<ListboxSelect>>", self.on_click_select_type)

        tk.Label(self.frame_input, text="Số lượng phần ăn",font=("Segoe UI", 11), bg="white", fg="black").grid(row=4, column=0, columnspan=5, sticky='w', pady=(10, 0))
        self.mon_an_so_luong_entry = tk.Entry(self.frame_input, font=("Segoe UI", 11))
        self.mon_an_so_luong_entry.insert(0, 1)
        self.mon_an_so_luong_entry.grid(row=5, column=0,padx=10, columnspan=5, sticky='ew')
        self.mon_an_so_luong_entry.bind("<KeyRelease>", self.so_luong_mon_an_event)
        

        tk.Label(self.frame_input, text="Buổi ăn",font=("Segoe UI", 11), fg="black", bg="white").grid(row=6,padx=10, column=0, columnspan=5, sticky='w', pady=(10, 0))

        self.buoi_an = tk.StringVar()
        self.buoi_an.set("Sáng")
        buoi_an = tk.Radiobutton(self.frame_input, text="Sáng",font=("Segoe UI", 11), fg="black", bg="white", variable=self.buoi_an, value="Sáng")
        buoi_an.grid(row=7,padx=(10, 0), column=0)
        buoi_an = tk.Radiobutton(self.frame_input, text="Trưa",font=("Segoe UI", 11), fg="black", bg="white", variable=self.buoi_an, value="Trưa")
        buoi_an.grid(row=7, column=1)
        buoi_an = tk.Radiobutton(self.frame_input, text="Chiều",font=("Segoe UI", 11), fg="black", bg="white", variable=self.buoi_an, value="Chiều")
        buoi_an.grid(row=7, column=2)
        buoi_an = tk.Radiobutton(self.frame_input, text="Tối",font=("Segoe UI", 11), fg="black", bg="white", variable=self.buoi_an, value="Tối")
        buoi_an.grid(row=7, column=3)
        buoi_an = tk.Radiobutton(self.frame_input, text="Phụ",font=("Segoe UI", 11), fg="black", bg="white", variable=self.buoi_an, value="Phụ")
        buoi_an.grid(row=7,padx=(0, 10), column=4)

        them_moi_btn = tk.Button(self.frame_input, text="Thêm",font=("Segoe UI", 12, "bold"), bg="green", fg="white", bd=0, command=self.on_click_them_mon_an)
        them_moi_btn.grid(column=0, row=8,padx=10, columnspan=5, sticky="we", pady=(10, 10), ipady=2)

        huy_btn = tk.Button(self.frame_input, text="Hủy",font=("Segoe UI", 12, "bold"), fg="red", bg="white", bd=0)
        huy_btn.grid(column=0, row=9,padx=10, columnspan=5, sticky="we")

        
        #______________________________________Tool tra cứu
        self.frame_search_api = tk.Frame(self.content_frame, bd=1, bg="white")
        self.frame_search_api.grid(column=1, row=1, sticky="snwe",padx=(5,10), pady=5)

        self.frame_search_api.columnconfigure(0, weight=1)

        tk.Label(self.frame_search_api, text="Tra cứu calories các món ăn", font=("Segoe UI", 15), fg="black", bg="white").grid(column=0, row=0,padx=10, pady=15, sticky="we")
        self.tra_cuu_entry = tk.Entry(self.frame_search_api, font=("Segoe UI", 12))
        self.tra_cuu_entry.grid(row=1, column=0, columnspan=5,padx=10, sticky="ew")
        self.tra_cuu_entry.bind("<KeyRelease>", self.search_calo_event)

        self.tra_cuu_listbox = tk.Listbox(self.frame_search_api,font=("Segoe UI", 11), height=5)
        self.tra_cuu_listbox.grid(row=2, column=0, columnspan=5,padx=10, sticky='ew')
        self.tra_cuu_listbox.bind("<<ListboxSelect>>", self.on_click_select_tra_cu)

        self.ten_mon = tk.Label(self.frame_search_api, text="Tên món: ",font=("Segoe UI", 12), bg="white", fg="black")
        self.ten_mon.grid(row=3, column=0,padx=10,pady=(20, 10), sticky="w")
        self.calo_mon = tk.Label(self.frame_search_api, text="Calories: ",font=("Segoe UI", 12), bg="white", fg="black")
        self.calo_mon.grid(row=4, column=0,padx=10,pady=10, sticky="w")

        tk.Button(self.frame_search_api, text="Tra cứu", fg="white", bd=0, bg="blue", font=("Segoe UI", 12, "bold"), command=self.on_click_tra_cuu).grid(column=0, row=5, pady=20,ipady=2, padx=10, sticky="ew")
        tk.Button(self.frame_search_api, text="Hủy", fg="red", bd=0, bg="white", font=("Segoe UI", 12, "bold"), command=self.on_click_huy_tra_cuu).grid(column=0, row=6, pady=20, padx=10, sticky="ew")


        #______________________________________Show thông tin bửa ăn
        self.frame_list_input = tk.Frame(self.content_frame, bg="white")
        self.frame_list_input.grid(column=0, row=2, columnspan=2, sticky="swen", padx=10 ,pady=10)

        self.frame_list_input.columnconfigure(0, weight=1)

        tk.Label(self.frame_list_input, text="Danh sách bửa ăn", font=("Segoe UI", 15), bg="white", fg="black").grid(row=0, column=0)
        columns = ("ngay", "buoi", "monan","calo","soluong", "tongcalo")

        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Arial", 11)) 
        style.configure("Custom.Treeview.Heading", font=("Arial", 12, "bold")) 

        self.health_tree = ttk.Treeview(self.frame_list_input,columns=columns, show="headings", style="Custom.Treeview")
        self.health_tree.heading("ngay", text="Ngày")
        self.health_tree.heading("buoi", text="Buổi ăn")
        self.health_tree.heading("monan", text="Món ăn")
        self.health_tree.heading("calo", text="Calories")
        self.health_tree.heading("soluong", text="Số lượng")
        self.health_tree.heading("tongcalo", text="Tổng calo")
        self.health_tree.grid(column=0, row=1, sticky="swen", pady=(10,0), padx=5)

        # self.update_item_selected = self.health_tree.selection()

        
        self.health_tree.bind("<Button-3>", self.on_click_select_option)

        #________________________

        self.vietnamese_to_english = {
                "chuối": "banana",
                "táo": "apple",
                "cam": "orange",
                "gạo": "rice",
                "ức gà": "chicken breast",
                "bò bít tết": "steak",
                "sườn heo": "pork ribs",
                "cá hồi": "salmon",
                "trứng": "egg",
                "bánh mì": "bread",
                "sữa": "milk",
                "phô mai": "cheese",
                "sữa chua": "yogurt",
                "khoai tây": "potato",
                "cà rốt": "carrot",
                "cà chua": "tomato",
                "bông cải xanh": "broccoli",
                "rau bina": "spinach",
                "bơ": "avocado",
                "hạnh nhân": "almond",
                "óc chó": "walnut",
                "bơ đậu phộng": "peanut butter",
                "yến mạch": "oatmeal",
                "mì ống": "pasta",
                "pizza": "pizza",
                "hamburger": "hamburger",
                "cơm chiên": "fried rice",
                "mì sợi": "noodles",
                "đậu hũ": "tofu",
                "đậu lăng": "lentils",
                "đậu gà": "chickpeas",
                "đậu đen": "black beans",
                "đậu que": "green beans",
                "dưa leo": "cucumber",
                "hành tây": "onion",
                "tỏi": "garlic",
                "nấm": "mushroom",
                "tôm": "shrimp",
                "cua": "crab",
                "tôm hùm": "lobster",
                "gà tây": "turkey",
                "vịt": "duck",
                "thịt xông khói": "bacon",
                "xúc xích": "sausage",
                "bơ": "butter",
                "dầu ô liu": "olive oil",
                "đường": "sugar",
                "mật ong": "honey",
                "sô cô la": "chocolate",
                "bánh kem": "cake",
                "bánh quy": "cookie",
                "kem": "ice cream",
                "cà phê": "coffee",
                "trà": "tea",
                "nước cam": "orange juice",
                "nước táo": "apple juice",
                "bia": "beer",
                "rượu vang": "wine",
                "dưa hấu": "watermelon",
                "nho": "grape",
                "dứa": "pineapple",
                "dâu tây": "strawberry",
                "việt quất": "blueberry",
                "mâm xôi": "raspberry",
                "đào": "peach",
                "lê": "pear",
                "mận": "plum",
                "anh đào": "cherry",
                "bắp": "corn",
                "khoai lang": "sweet potato",
                "bí đỏ": "pumpkin",
                "bí xanh": "zucchini",
                "súp lơ": "cauliflower",
                "cải xoăn": "kale",
                "rau xà lách": "lettuce",
                "củ dền": "beetroot",
                "bắp cải": "cabbage",
                "củ cải đỏ": "radish",
                "đậu Hà Lan": "peas",
                "đậu nành non": "edamame",
                "hạt diêm mạch": "quinoa",
                "hạt chia": "chia seeds",
                "hạt lanh": "flax seeds",
                "dừa": "coconut",
                "sữa hạnh nhân": "almond milk",
                "sữa đậu nành": "soy milk",
                "kem tươi": "whipped cream",
                "sốt mayonnaise": "mayonnaise",
                "tương cà": "ketchup",
                "mù tạt": "mustard",
                "sốt salsa": "salsa",
                "súp": "soup",
                "bánh sandwich": "sandwich",
                "gà rán": "fried chicken",
                "viên thịt": "meatballs",
                "cá": "fish",
                "sushi": "sushi",
                "mì ramen": "ramen",
                "há cảo": "dumplings"
            }
        
        self.search_type_mon_an()
        self.search_calo()
        self.fill_data_health_tree()

    def search_type_mon_an_event(self, event):
        self.search_type_mon_an()
    def search_type_mon_an(self):
        value = self.mon_an_type_entry.get().strip().lower()
        self.mon_an_type_listbox.delete(0, tk.END)
        if not value:
            for mon_an in self.monan_options:
                self.mon_an_type_listbox.insert(tk.END, mon_an)
        
        else:
            for mon_an in self.monan_options:
                if value in mon_an.lower().strip():
                    self.mon_an_type_listbox.delete(0, tk.END)
                    self.mon_an_type_listbox.insert(tk.END, mon_an)

    def on_click_select_type(self, event):
        if not self.mon_an_type_listbox.curselection():
            return
        else:
            selection = self.mon_an_type_listbox.get(self.mon_an_type_listbox.curselection())
            self.mon_an_type_entry.delete(0, tk.END)
            self.mon_an_type_entry.insert(0, selection)
            self.mon_an_type_listbox.delete(0, tk.END)

    def search_calo_event(self, event):
        self.tra_cuu_entry.config(bg="white")
        self.search_calo()

    def search_calo(self):
        value = self.tra_cuu_entry.get().strip().lower()
        self.tra_cuu_listbox.delete(0, tk.END)
        if not value:
            for mon_an in self.monan_options:
                self.tra_cuu_listbox.insert(tk.END, mon_an)
        
        else:
            for mon_an in self.monan_options:
                if value in mon_an.lower().strip():
                    self.tra_cuu_listbox.delete(0, tk.END)
                    self.tra_cuu_listbox.insert(tk.END, mon_an)
    
    def on_click_select_tra_cu(self, event):
         if not self.tra_cuu_listbox.curselection():
            return
         else:
            selection = self.tra_cuu_listbox.get(self.tra_cuu_listbox.curselection())
            self.tra_cuu_entry.delete(0, tk.END)
            self.tra_cuu_entry.insert(0, selection)
            self.tra_cuu_listbox.delete(0, tk.END)

    def on_click_tra_cuu(self):
        if not self.tra_cuu_entry.get():
            self.tra_cuu_entry.config(bg="red")
            messagebox.showinfo("Lỗi", "Vui lòng nhập món ăn cần tra cứu")
            return
        
        else:
            raw_input = self.tra_cuu_entry.get().strip()
            value_vn = raw_input.lower()

            if value_vn not in self.vietnamese_to_english:
                messagebox.showerror("Lỗi", f"Không tìm thấy {value_vn}")
                return
            value_en = self.vietnamese_to_english[value_vn]

            try:
                with open("data/calorie_data_all.json", "r", encoding="utf-8") as file:
                    data_api = json.load(file)
            except Exception as ex:
                messagebox.showerror("Lỗi", f"Lỗi: {ex}")
            
            for item_api in data_api:
                if item_api["food"] == value_en:
                    self.ten_mon.config(text=f"Tên món: {value_vn}")
                    calo = item_api["calories"]
                    self.calo_mon.config(text=f"Calories: {calo}")
                    break
        
    def on_click_huy_tra_cuu(self):
        self.tra_cuu_entry.delete(0, tk.END)
        
        self.ten_mon.config(text="Tên món: ")
        self.calo_mon.config(text="Calories: ")
        self.search_calo()

    def so_luong_mon_an_event(self, event):
        self.mon_an_so_luong_entry.config(bg="white")

    def on_click_them_mon_an(self):
        if not self.mon_an_type_entry.get() or not self.mon_an_so_luong_entry.get():
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin")
            return
        elif not self.mon_an_so_luong_entry.get().strip().isdigit():
            messagebox.showerror("Lỗi", "Số lượng phải là một số nguyên dương.")
            self.mon_an_so_luong_entry.config(bg="red")
            return
        else:
            raw_input = self.mon_an_type_entry.get().strip()
            value_vn = raw_input.lower()

            if value_vn not in self.vietnamese_to_english:
                messagebox.showerror("Lỗi", f"Không tìm thấy {value_vn}")
                return
            value_en = self.vietnamese_to_english[value_vn]
            try:
                with open("data/calorie_data_all.json", "r", encoding="utf-8") as file:
                    data_api = json.load(file)
            except Exception as ex:
                messagebox.showerror("Lỗi", f"{ex}")
            for item in data_api:
                if item["food"] == value_en:
                    calo = item["calories"]
                    break
            soluong = float(self.mon_an_so_luong_entry.get())
            tongcalo = soluong * calo
            buoi_an = self.buoi_an.get()
            today = datetime.now().strftime("%d-%m-%Y")
            new_data_mon_an = {
                "date": today,
                "meal": buoi_an,
                "eating": value_vn,
                "calo": calo,
                "quantity": soluong,
                "totalcalo": tongcalo
            }
            try:
                with open("data/meal.json", "r", encoding="utf-8") as file:
                    data_meal = json.load(file)
            except Exception as ex:
                messagebox.showerror("Lỗi", f"{ex}")
                return
            for user in data_meal:
                if user["username"] == self.name:
                    user["meals"].append(new_data_mon_an)
                break
            try:
                with open("data/meal.json", "w", encoding="utf-8") as file:
                    json.dump(data_meal, file, ensure_ascii=False, indent=4)
                    messagebox.showinfo("Thông báo", "Thêm thành công")
                
                self.mon_an_type_entry.delete(0, tk.END)
                self.mon_an_so_luong_entry.delete(0, tk.END)
                self.buoi_an.set("Sáng")
                self.mon_an_so_luong_entry.insert(0, 1)

                self.reset_fill_data_health_tree_event()

            except Exception as ex:
                messagebox.showerror("Lỗi", f"{ex}")
                return
            
    def fill_data_health_tree(self):
        try: 
            with open("data/meal.json", "r", encoding="utf-8") as file:
                data_meals = json.load(file)
        except Exception as ex:
            messagebox.showerror("Lỗi",f"{ex}")
            return
        for user in data_meals:
            if user["username"] == self.name:
                for item in user["meals"]:
                    self.health_tree.insert("", tk.END, values=(item.get("date", ""), item.get("meal", ""), item.get("eating", ""), item.get("calo", ""), item.get("quantity", ""), item.get("totalcalo", "")))

    def reset_fill_data_health_tree_event(self):
        for row in self.health_tree.get_children():
            self.health_tree.delete(row)
        self.fill_data_health_tree()    

    def on_click_select_option(self, event):
        self.update_item_selected = self.health_tree.selection()

        selected_item = self.health_tree.identify_row(event.y)
        if selected_item:
            self.health_tree.selection_set(selected_item)

            self.health_tree_menu = tk.Menu(self.root, tearoff=0)
            self.health_tree_menu.add_command(label="Chỉnh sửa", font=("Segoe UI", 11), command=lambda: self.on_click_menu_update(self.update_item_selected))
            self.health_tree_menu.add_command(label="Xóa", font=("Segoe UI", 11), command=self.update_creen_menu_click_delete)
            self.health_tree_menu.add_separator()
            self.health_tree_menu.add_command(label="Làm mới", font=("Segoe UI", 11), command=self.on_click_lam_moi)

            self.health_tree_menu.tk_popup(event.x_root, event.y_root)
    
    #Update thông tin khi click trong menu
    def on_click_menu_update(self, update_item_selected):

        if not update_item_selected:
            messagebox.showerror("Lỗi", "Không tìm thấy mục đã chọn")
            return
        item = self.health_tree.item(update_item_selected[0])
        self.values_select_update = item["values"]
        date, meal, eating, calo, quantity, totalcalo = self.values_select_update

        eating_var = tk.StringVar(value=eating)

        self.creen_update = tk.Toplevel(self.root)
        self.creen_update.title("Chỉnh sửa thông tin")
        self.creen_update.geometry("325x415")
        self.creen_update.resizable(False, False)
        frame_update = tk.Frame(self.creen_update)
        frame_update.grid(column=0, row=0, sticky="swen", padx=0)

        icon = tk.PhotoImage(file="Images/logo1.png")
        self.creen_update.iconphoto(False, icon)

        tk.Label(frame_update, text=date, font=("Segoe UI", 12, "bold")).grid(column=0, row=0, columnspan=5,sticky="swen", padx=10)

        tk.Label(frame_update, text="Món ăn",font=("Segoe UI", 12), fg="black", bg=None).grid(column=0, columnspan=5, row=1, padx=10, sticky="w")

        self.update_mon_an_type_entry = tk.Entry(frame_update, font=("Segoe UI", 12), textvariable=eating_var)
        self.update_mon_an_type_entry.grid(column=0, columnspan=5, row=2, padx=10, sticky="swen")
        self.update_mon_an_type_entry.bind("<KeyRelease>", self.update_creen_search_type_mon_an_event)

        self.update_mon_an_type_listbox = tk.Listbox(frame_update,font=("Segoe UI", 11), height=5)
        self.update_mon_an_type_listbox.grid(column=0, columnspan=5, row=3, padx=10,sticky="swen")
        self.update_mon_an_type_listbox.bind("<<ListboxSelect>>", self.update_select_type)
        

        quantity_var = tk.StringVar(value=quantity)
        tk.Label(frame_update, text="Số lượng phần ăn",font=("Segoe UI", 12), bg=None, fg="black").grid(column=0, columnspan=5, row=4,sticky="w", pady=5, padx=10)
        self.update_creen_mon_an_so_luong_entry = tk.Entry(frame_update, font=("Segoe UI", 11), textvariable=quantity_var)
        self.update_creen_mon_an_so_luong_entry.grid(column=0, columnspan=5, row=5, padx=10,sticky="swen")
        self.update_creen_mon_an_so_luong_entry.bind("<KeyRelease>", self.so_luong_mon_an_event)

        tk.Label(frame_update, text="Buổi ăn",font=("Segoe UI", 12), fg="black", bg=None).grid(column=0, columnspan=5, row=6, padx=10,sticky="w", pady=5)
        
        self.update_buoi_an = tk.StringVar()
        self.update_buoi_an.set(meal)
        tk.Radiobutton(frame_update, text="Sáng",font=("Segoe UI", 11), fg="black", bg=None, variable=self.update_buoi_an, value="Sáng").grid(column=0, row=7, padx=(10,2))
        tk.Radiobutton(frame_update, text="Trưa",font=("Segoe UI", 11), fg="black", bg=None, variable=self.update_buoi_an, value="Trưa").grid(column=1, row=7, padx=2)
        tk.Radiobutton(frame_update, text="Chiều",font=("Segoe UI", 11), fg="black", bg=None, variable=self.update_buoi_an, value="Chiều").grid(column=2, row=7, padx=2)
        tk.Radiobutton(frame_update, text="Tối",font=("Segoe UI", 11), fg="black", bg=None, variable=self.update_buoi_an, value="Tối").grid(column=3, row=7, padx=2)
        tk.Radiobutton(frame_update, text="Phụ",font=("Segoe UI", 11), fg="black", bg=None, variable=self.update_buoi_an, value="Phụ").grid(column=4, row=7, padx=(2, 10))

        update_btn = tk.Button(frame_update, text="Lưu thay đổi",font=("Segoe UI", 12, "bold"), bg="green", fg="white", bd=0, command=self.save_updated_meal_info)
        update_btn.grid(column=0, columnspan=5, row=8, padx=10, sticky="swen", pady=10)

        huy_btn = tk.Button(frame_update, text="Hủy",font=("Segoe UI", 12, "bold"), fg="red", bg="white", bd=0, command=self.update_creen_on_click_huy)
        huy_btn.grid(column=0, columnspan=5, row=9, padx=10,pady=(0, 20), sticky="swen")

        self.update_creen_search_type_mon_an()

   

    def update_creen_search_type_mon_an_event(self, event):
        self.update_creen_search_type_mon_an()
    def update_creen_search_type_mon_an(self):
        value = self.update_mon_an_type_entry.get().strip().lower()
        self.update_mon_an_type_listbox.delete(0, tk.END)
        if not value:
            for mon_an in self.monan_options:
                self.update_mon_an_type_listbox.insert(tk.END, mon_an)
        
        else:
            for mon_an in self.monan_options:
                if value in mon_an.lower().strip():
                    self.update_mon_an_type_listbox.delete(0, tk.END)
                    self.update_mon_an_type_listbox.insert(tk.END, mon_an)
    
    def update_select_type(self, event):
        if not self.update_mon_an_type_listbox.curselection():
            return
        else:
            selection = self.update_mon_an_type_listbox.get(self.update_mon_an_type_listbox.curselection())
            self.update_mon_an_type_entry.delete(0, tk.END)
            self.update_mon_an_type_entry.insert(0, selection)
            self.update_mon_an_type_listbox.delete(0, tk.END)

    #lưu dữ liệu update
    def save_updated_meal_info(self):
        date, meal, eating, calo, quantity, totalcalo = self.values_select_update
        new_eating = self.update_mon_an_type_entry.get().strip()
        new_quantity = self.update_creen_mon_an_so_luong_entry.get().strip()
        new_meal = self.update_buoi_an.get()

        if not new_eating or not new_quantity.replace('.', '', 1).isdigit():
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ và đúng định dạng thông tin.")
            return

        new_quantity = float(new_quantity)

        if new_eating not in self.vietnamese_to_english:
            messagebox.showerror("Lỗi", f"Không tìm thấy món ăn '{new_eating}' trong dữ liệu.")
            return

        value_en = self.vietnamese_to_english[new_eating]

        try:
            with open("data/calorie_data_all.json", "r", encoding="utf-8") as file:
                data_api = json.load(file)
        except Exception as ex:
            messagebox.showerror("Lỗi", f"Không thể đọc file calorie_data_all.json: {ex}")
            return

        new_calo = None
        for item in data_api:
            if item["food"] == value_en:
                new_calo = item["calories"]
                break

        if new_calo is None:
            messagebox.showerror("Lỗi", f"Không tìm thấy calo cho món ăn '{new_eating}'.")
            return

        new_total_calo = new_calo * new_quantity

        # Cập nhật vào file meal.json
        try:
            with open("data/meal.json", "r", encoding="utf-8") as file:
                data_meal_update = json.load(file)
        except Exception as ex:
            messagebox.showerror("Lỗi", f"Không thể đọc file meal.json: {ex}")
            return

        updated = False
        for user in data_meal_update:
            if user["username"] == self.name:
                for item in user["meals"]:
                    if (item["date"] == date and item["meal"] == meal and item["eating"] == eating and float(item["calo"]) == float(calo) and float(item["quantity"]) == float(quantity) and float(item["totalcalo"]) == float(totalcalo)):
                        # Cập nhật thông tin mới
                        item["meal"] = new_meal
                        item["eating"] = new_eating
                        item["calo"] = new_calo
                        item["quantity"] = new_quantity
                        item["totalcalo"] = new_total_calo
                        updated = True
                        break
                break

        if not updated:
            messagebox.showerror("Lỗi", "Không tìm thấy mục cần cập nhật.")
            return

        try:
            with open("data/meal.json", "w", encoding="utf-8") as file:
                json.dump(data_meal_update, file, ensure_ascii=False, indent=4)

            messagebox.showinfo("Thành công", "Đã lưu thay đổi thành công.")
            self.creen_update.destroy()
            self.reset_fill_data_health_tree_event() 
        except Exception as ex:
            messagebox.showerror("Lỗi", f"Không thể ghi file meal.json: {ex}")


    def update_creen_menu_click_delete(self):
        # self.update_item_selected = self.health_tree.selection()

        if self.update_item_selected:
            item = self.health_tree.item(self.update_item_selected[0])
            self.values_select_update = item["values"]
            date, meal, eating, calo, quantity, totalcalo = self.values_select_update
        try:
            with open("data/meal.json", "r", encoding="utf-8") as file:
                data_meal_update = json.load(file)
        except Exception as ex:
            messagebox.showerror("Lỗi", f"Không thể đọc file meal.json: {ex}")
            return

        updated = False
        for user in data_meal_update:
            if user["username"] == self.name:
                for index, item in enumerate(user["meals"]):
                    if (item["date"] == date and item["meal"] == meal and item["eating"] == eating and float(item["calo"]) == float(calo) and float(item["quantity"]) == float(quantity) and float(item["totalcalo"]) == float(totalcalo)):
                        del user["meals"][index]
                        updated = True
                        break
                break
        if not updated:
            messagebox.showerror("Lỗi", "Không tìm thấy mục cần xóa.")
            return
        try:
            with open("data/meal.json", "w", encoding="utf-8") as file:
                json.dump(data_meal_update, file, ensure_ascii=False, indent=4)
        except Exception as ex:
            messagebox.showerror("Lỗi", f"Không thể ghi file meal.json: {ex}")
            return
        
        self.reset_fill_data_health_tree_event()
        messagebox.showinfo("Thành công", "Đã xoá mục ăn uống thành công.")

    def update_creen_on_click_huy(self):
        self.creen_update.destroy()
    def on_click_lam_moi(self):
        self.reset_fill_data_health_tree_event()
    #___________________________________________________________________Theo dõi________________________________________
    def show_theo_doi(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        self.tai_khoan_btn.config(bg="#40E0D0")
        self.luyen_tap_btn.config(bg="#40E0D0")
        self.dinh_duong_btn.config(bg="#40E0D0")
        self.theo_doi_btn.config(bg="#008080")
        self.list_user_btn.config(bg="#40E0D0")

        tk.Label(self.content_frame, text="Theo Dõi Sức Khoẻ", font=("Arial", 18, "bold"), fg="#005B9A").pack(pady=15)

        frame_scroll = tk.Frame(self.content_frame)
        frame_scroll.pack(anchor="center", expand=True, fill="both",pady= 10)

        canvas = tk.Canvas(frame_scroll)
        scrollbar = tk.Scrollbar(frame_scroll, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # === Quan trọng: Frame có thể cuộn ===
        scrollable_frame = tk.Frame(canvas)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="center" )

        # === Gắn cuộn chuột ===
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        # === Gắn frame thống kê ===
        self.frame_thongke = tk.Frame(scrollable_frame, bg="white", padx=20, pady=20)
        self.frame_thongke.pack(anchor="center", padx=250)


        today = datetime.now().strftime("%d-%m-%Y")

        top_frame = tk.Frame(self.frame_thongke, bg="white")
        top_frame.pack(pady=10)

        tk.Label(top_frame, text="Chọn ngày (dd-mm-yyyy):", font=("Arial", 11, "bold"), bg="white").grid(row=0, column=0, padx=5, pady=10)
        date_entry = tk.Entry(top_frame, font=("Arial", 11))
        date_entry.insert(0, today)
        date_entry.grid(row=0, column=1, padx=5)
        tk.Button(top_frame, text="Xem", font=("Arial", 11), bg="#3498db", fg="white", command=lambda: self.thong_ke_theo_ngay(date_entry.get())).grid(row=0, column=2, padx=0, ipadx=10)

        self.thong_ke_theo_ngay(today)


    def thong_ke_theo_ngay(self, selected_date):
        for widget in self.frame_thongke.winfo_children()[1:]:
            widget.destroy()

        total_calo_in = 0
        total_calo_out = 0
        food_list = []
        activity_list = []

        try:
            with open("data/health.json", "r", encoding="utf-8") as f:
                health_data = json.load(f)
            for user in health_data:
                if user["username"] == self.name:
                    muctieu = user["goal"]
                    break
            else:
                muctieu = "Không xác định"
        except:
            muctieu = "Không xác định"

        # Dữ liệu calo ăn
        try:
            with open("data/meal.json", "r", encoding="utf-8") as f:
                meals_data = json.load(f)
            for user in meals_data:
                if user["username"] == self.name:
                    for meal in user["meals"]:
                        if meal.get("date") == selected_date:
                            total_calo_in += meal.get("totalcalo", 0)
                            food_list.append(meal["eating"])
        except:
            pass

        # Dữ liệu calo đốt
        try:
            with open("data/exercise.json", "r", encoding="utf-8") as f:
                exercises_data = json.load(f)
            for user in exercises_data:
                if user["username"] == self.name:
                    for ex in user["exercises"]:
                        if ex.get("date") == selected_date:
                            total_calo_out += ex.get("calories", 0)
                            activity_list.append(f"{ex['exercise_type']} - {ex['duration']} phút")
        except:
            pass

        # PHẦN 1: Thông tin tổng quát
        thongtin_frame = tk.LabelFrame(self.frame_thongke, text="Thông tin tổng hợp", font=("Arial", 12, "bold"), bg="white", fg="#005B9A")
        thongtin_frame.pack(padx=10, pady=10, fill="x")

        def info_row(frame, label, value):
            tk.Label(frame, text=label, font=("Arial", 11), bg="white").pack(anchor="w", padx=10, pady=2)
            tk.Label(frame, text=value, font=("Arial", 11, "bold"), bg="white", fg="#2c3e50").pack(anchor="w", padx=20)

        info_row(thongtin_frame, "Lượng calo cần thiết (TDEE):", f"{self.tdee} calo")
        info_row(thongtin_frame, "Mục tiêu:", muctieu)
        info_row(thongtin_frame, "Tổng calo nạp:", f"{total_calo_in} calo")
        info_row(thongtin_frame, "Tổng calo đốt cháy:", f"{total_calo_out} calo")

        # PHẦN 2: Danh sách món ăn
        if food_list:
            meal_frame = tk.LabelFrame(self.frame_thongke, text="Danh sách món ăn", font=("Arial", 12, "bold"), bg="white", fg="#005B9A")
            meal_frame.pack(padx=10, pady=5, fill="x")
            for food in food_list:
                tk.Label(meal_frame, text=f"- {food}", font=("Arial", 11), bg="white", anchor="w").pack(anchor="w", padx=15)

        # PHẦN 3: Danh sách hoạt động
        if activity_list:
            ex_frame = tk.LabelFrame(self.frame_thongke, text="Hoạt động luyện tập", font=("Arial", 12, "bold"), bg="white", fg="#005B9A")
            ex_frame.pack(padx=10, pady=5, fill="x")
            for act in activity_list:
                tk.Label(ex_frame, text=f"- {act}", font=("Arial", 11), bg="white", anchor="w").pack(anchor="w", padx=15)

        # PHẦN 4: Kết luận và lời khuyên
        net_calo = total_calo_in - total_calo_out
        difference = net_calo - self.tdee
        abs_diff = abs(difference)

        if abs_diff < 100:
            ket_luan = "Lượng calo tiêu thụ hôm nay gần đạt mức cần thiết."
        elif difference > 0:
            ket_luan = f"Năng lượng của bạn dư khoảng {difference} calo."
        else:
            ket_luan = f"Năng lượng bạn thiếu khoảng {abs(difference)} calo."

        if muctieu == "Giảm cân":
            if net_calo > self.tdee:
                khuyen = "Bạn nên cắt giảm khẩu phần ăn hoặc tăng cường vận động để đạt mục tiêu giảm cân."
            else:
                khuyen = "Bạn đang đi đúng hướng để giảm cân. Hãy duy trì mức calo tiêu thụ hợp lý."
        elif muctieu == "Tăng cân":
            if net_calo < self.tdee:
                khuyen = "Bạn nên ăn nhiều hơn hoặc giảm hoạt động để đạt mục tiêu tăng cân."
            else:
                khuyen = "Bạn đang đi đúng hướng để tăng cân. Hãy duy trì chế độ hiện tại."
        else:
            if abs_diff < 100:
                khuyen = "Bạn đang duy trì cân nặng khá tốt. Tiếp tục chế độ hiện tại!"
            elif difference > 0:
                khuyen = "Bạn đang nạp dư calo nhẹ, nên điều chỉnh một chút nếu muốn giữ cân."
            else:
                khuyen = "Bạn đang thiếu calo nhẹ, hãy đảm bảo ăn uống đầy đủ để duy trì cân nặng."

        result_frame = tk.LabelFrame(self.frame_thongke, text="Kết luận và lời khuyên", font=("Arial", 12, "bold"), bg="white", fg="#005B9A")
        result_frame.pack(padx=10, pady=10, fill="x")

        tk.Label(result_frame, text=f"Kết luận: {ket_luan}", font=("Arial", 11), bg="white").pack(anchor="w", padx=10, pady=5)
        tk.Label(result_frame, text=f"Lời khuyên: {khuyen}", font=("Arial", 11), bg="white").pack(anchor="w", padx=10, pady=5)


    #___________________________________________________________________List user________________________________________________________________
    def show_listUser(self):
        self.tai_khoan_btn.config(bg="#40E0D0")
        self.luyen_tap_btn.config(bg="#40E0D0")
        self.dinh_duong_btn.config(bg="#40E0D0")
        self.theo_doi_btn.config(bg="#40E0D0")
        self.list_user_btn.config(bg="#008080")

        for widget in self.content_frame.winfo_children():
            widget.destroy()

        tk.Label(self.content_frame, text="Danh sách người dùng", font=("Segoe UI", 15, "bold")).grid(column=0, row=0)

        self.frame_ds_user = tk.Frame(self.content_frame, bg="white", bd=2, relief="solid")
        self.frame_ds_user.grid(column=0, row=1,sticky="snew", padx=20, pady=10)

        tk.Label(self.frame_ds_user, text="Nhập tên tài khoản cần tìm:", font=("Segoe UI", 12, "bold"), bg="white").grid(column=0, row=0, padx=5, pady=10, sticky="w")
        self.search_entry = tk.Entry(self.frame_ds_user,font=("Segoe UI", 12), bd=2,relief="groove", highlightthickness=1, highlightcolor="#4a90e2")
        self.search_entry.grid(column=1, row=0, padx=5,pady=10, ipady=2, sticky="w")
        tk.Button(self.frame_ds_user, text="Tìm",font=("Segoe UI", 11), bd=0, background="green", fg="black", command=self.search_user).grid(column=2, row=0, padx=5,ipadx=20, sticky="w")
        tk.Button(self.frame_ds_user, text="Hủy",font=("Segoe UI", 11), bd=0, background="white", fg="red", command=self.huy_search_user).grid(column=3, row=0, padx=5,ipadx=20, sticky="w")

        columns = ["STT", "Tên Đăng Nhập", "Họ Tên", "Tuổi", "Giới Tính", "Chiều Cao", "Cân Nặng", "Bệnh Lý", "Quyền"]
        self.list_user = ttk.Treeview(self.frame_ds_user, columns=columns, show="headings", height=10)
        self.list_user.grid(column=0, row=2, columnspan=4, sticky="nsew", pady=5, padx=5)

        self.list_user.bind("<Button-3>", self.event_show_menu_edit_user)

        for col in columns:
            self.list_user.heading(col, text=col.capitalize())
            self.list_user.column(col, width=100)

        self.load_user_data()

       

    def load_user_data(self):
        for row in self.list_user.get_children():
            self.list_user.delete(row)
            
        try:
            with open("data/account.json", "r", encoding="utf-8") as file:
                self.user_data = json.load(file)

            for stt, user in enumerate(self.user_data):
                try:
                    with open("data/health.json", "r", encoding="utf-8") as file:
                        self.health_data = json.load(file)

                    for health_user in self.health_data:
                        if health_user["username"] == user["username"]:
                            self.list_user.insert("", tk.END, values=(
                            stt + 1,
                            user.get("username", ""),
                            health_user.get("fullname", ""),
                            health_user.get("age", ""),
                            health_user.get("gender", ""),
                            health_user.get("height", ""),
                            health_user.get("weight", ""),
                            health_user.get("illness", ""),
                            user.get("role", "")
                        ))
                except Exception as e:
                    messagebox.showerror("Lỗi", f"Không thể đọc dữ liệu: {e}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể đọc dữ liệu: {e}")

        


    def search_user(self):
        keyword = self.search_entry.get()

        for row in self.list_user.get_children():
            self.list_user.delete(row)

        try:
            with open("data/account.json", "r", encoding="utf-8") as file:
                user_data = json.load(file)

            for stt, user in enumerate(user_data):
                if user["username"] == keyword:
                    try:
                        with open("data/health.json", "r", encoding="utf-8") as file:
                            health_data = json.load(file)

                        for health_user in health_data:
                            if health_user["username"] == keyword:
                                self.list_user.insert("", tk.END, values=(

                                stt + 1,
                                user.get("username", ""),
                                health_user.get("fullname", ""),
                                health_user.get("age", ""),
                                health_user.get("gender", ""),
                                health_user.get("height", ""),
                                health_user.get("weight", ""),
                                health_user.get("illness", ""),
                                user.get("role", "")
                            ))
                    except Exception as e:
                        messagebox.showerror("Lỗi", f"Không thể đọc dữ liệu: {e}")
                    break
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể đọc dữ liệu: {e}")
    def huy_search_user(self):
        self.search_entry.delete(0, tk.END)
        self.load_user_data()

    def event_show_menu_edit_user(self, event):
        selected = self.list_user.selection()
        selected_item = self.list_user.identify_row(event.y)
        if selected_item:
            self.list_user.selection_set(selected_item)

            self.user_tree_menu = tk.Menu(self.root, tearoff=0)
            self.user_tree_menu.add_command(label="Chỉnh sửa", font=("Segoe UI", 11), command=lambda:self.edit_user(selected))
            self.user_tree_menu.add_command(label="Xóa", font=("Segoe UI", 11), command=lambda: self.delete_user(selected))
            self.user_tree_menu.add_separator()
            self.user_tree_menu.add_command(label="Làm mới", font=("Segoe UI", 11), command=self.load_user_data)

            self.user_tree_menu.tk_popup(event.x_root, event.y_root)

    def edit_user(self, selected):
        if not selected:
            messagebox.showwarning("Chọn người dùng", "Vui lòng chọn một người dùng để sửa.")
            return

        values = self.list_user.item(selected[0])["values"]
        username = values[1]

        if username == "admin":
            messagebox.showerror("Lỗi", "Đây là tài khoản admin không thể chỉnh sửa!")
            return

        user = next((u for u in self.user_data if u["username"] == username), None)
        health_user = next((h for h in self.health_data if h["username"] == username), None)

        if not user or not health_user:
            messagebox.showerror("Lỗi", "Không tìm thấy người dùng.")
            return

        # Tạo cửa sổ sửa
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Sửa thông tin người dùng")
        edit_window.geometry("350x400")

        fields = {
            "fullname": "Họ và tên",
            "age": "Tuổi",
            "gender": "Giới tính",
            "height": "Chiều cao",
            "weight": "Cân nặng",
            "illness": "Bệnh lý",
            "role": "Phân quyền"
        }

        entries = {}

        for i, (field, label) in enumerate(fields.items()):
            tk.Label(edit_window, text=label + ":").grid(row=i, column=0, sticky="w", padx=10, pady=5)

            if field == "gender":
                entry = ttk.Combobox(edit_window, values=["Nam", "Nữ"], state="readonly")
                entry.set(health_user.get("gender", ""))

            elif field == "role":
                entry = ttk.Combobox(edit_window, values=["Manager", "General"], state="readonly")
                entry.set(user.get("role", ""))
            else:
                entry = tk.Entry(edit_window)
                if field in health_user:
                    entry.insert(0, str(health_user.get(field, "")))
                else:
                    entry.insert(0, str(user.get(field, "")))
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries[field] = entry

        def save_changes():
            # Cập nhật health.json
            for field in ["fullname", "age", "gender", "height", "weight", "illness"]:
                health_user[field] = entries[field].get()

            with open("data/health.json", "w", encoding="utf-8") as file:
                json.dump(self.health_data, file, indent=4, ensure_ascii=False)

            # Cập nhật account.json
            user["role"] = entries["role"].get()
            with open("data/account.json", "w", encoding="utf-8") as file:
                json.dump(self.user_data, file, indent=4, ensure_ascii=False)

            self.load_user_data()
            messagebox.showinfo("Thành công", "Đã cập nhật thông tin người dùng.")
            edit_window.destroy()

        tk.Button(edit_window, text="Lưu", command=save_changes, bg="green", fg="white", width=15).grid(row=len(fields), column=0, columnspan=2, pady=15)


    def delete_user(self, selected):
        # selected = self.list_user.selection()
        if not selected:
            messagebox.showwarning("Chọn người dùng", "Vui lòng chọn một người dùng để xoá.")
            return

        values = self.list_user.item(selected[0])["values"]
        username = values[1]
        confirm = messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xoá người dùng '{username}'?")
        if not confirm:
            return
        if username == "admin":
            messagebox.showerror("Lỗi", "Đây là tài khoản admin không thể xóa!")
            return
        
        if username == self.name:
            messagebox.showerror("Lỗi", "Không thể xóa tài khoản đang được sử dụng!")
            return

        # Xoá khỏi account
        self.user_data = [u for u in self.user_data if u["username"] != username]
        with open("data/account.json", "w", encoding="utf-8") as file:
            json.dump(self.user_data, file, indent=4, ensure_ascii=False)

        # Xoá khỏi health
        try:
            with open("data/health.json", "r", encoding="utf-8") as file:
                health_data = json.load(file)
            health_data = [h for h in health_data if h["username"] != username]

            with open("data/health.json", "w", encoding="utf-8") as file:
                json.dump(health_data, file, indent=4, ensure_ascii=False)
            self.health_data = health_data
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi xoá dữ liệu sức khoẻ: {e}")
        #Xóa trong meal
        try:
            with open("data/meal.json", "r", encoding="utf-8") as file:
                meal_data = json.load(file)

            meal_data = [h for h in meal_data if h["username"] != username]

            with open("data/meal.json", "w", encoding="utf-8") as file:
                json.dump(meal_data, file, indent=4, ensure_ascii=False)

        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi xoá dữ liệu meal: {e}")

        #Xóa trong ex
        try:
            with open("data/exercise.json", "r", encoding="utf-8") as file:
                ex_data = json.load(file)
            ex_data = [h for h in ex_data if h["username"] != username]

            with open("data/exercise.json", "w", encoding="utf-8") as file:
                json.dump(ex_data, file, indent=4, ensure_ascii=False)

        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi xoá dữ liệu exercise: {e}")

        self.load_user_data()
        messagebox.showinfo("Đã xoá", f"Đã xoá người dùng '{username}' thành công.")



    def logout(self):
        self.tai_khoan_btn.config(bg="#40E0D0")
        self.luyen_tap_btn.config(bg="#40E0D0")
        self.dinh_duong_btn.config(bg="#40E0D0")
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



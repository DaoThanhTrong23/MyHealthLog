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
        if role == "Manager":
            self.list_user_btn = tk.Button(self.menu_frame,text="Danh sách user",command=self.show_listUser,bg="#40E0D0",fg="black",font=("Segoe UI", 12, "bold"), relief="flat",activebackground="#40E0D0",activeforeground="white")
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


        # self.content_frame.grid_rowconfigure(1, weight=1)
        # self.content_frame.grid_columnconfigure(1, weight=1)

        # self.content_frame.columnconfigure(0, weight=1)  
        # self.content_frame.columnconfigure(1, weight=1)
        # self.content_frame.rowconfigure(0, weight=1)
        # self.content_frame.rowconfigure(1, weight=1)
        

        tk.Label(self.content_frame, text="Chế độ ăn uống",font=("Segoe UI", 18,"bold")).grid(column=0, row=0, pady=10, columnspan=2)
        #_______________________________________nhập phần ăn
        self.frame_input = tk.Frame(self.content_frame, bg="white", bd=1)
        self.frame_input.grid(column=0, row=1,pady=5, padx=(10, 5), sticky="swen")
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

        self.mon_an_calo_label = tk.Label(self.frame_input, text="Lượng calo món ăn: ",font=("Segoe UI", 11), fg="black", bg="white")
        self.mon_an_calo_label.grid(row=8, column=0,padx=(10, 5), columnspan=5, sticky="w")

        them_moi_btn = tk.Button(self.frame_input, text="Thêm",font=("Segoe UI", 12, "bold"), bg="green", fg="white", bd=0, command=self.on_click_them_mon_an)
        them_moi_btn.grid(column=0, row=9,padx=10, columnspan=5, sticky="we", pady=(10, 10), ipady=2)
        #them_moi_btn.bind("<Button-1>", self.reset_fill_data_health_tree_event)

        huy_btn = tk.Button(self.frame_input, text="Hủy",font=("Segoe UI", 12, "bold"), fg="red", bg="white", bd=0)
        huy_btn.grid(column=0, row=10,padx=10, columnspan=5, sticky="we")

        
        #______________________________________Tool tra cứu
        self.frame_search_api = tk.Frame(self.content_frame, bd=1, bg="white")
        self.frame_search_api.grid(column=1, row=1, sticky="swen",padx=(5,10), pady=5)

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
        self.health_tree = ttk.Treeview(self.frame_list_input, columns=columns, show="headings")
        self.health_tree.heading("ngay", text="Ngày")
        self.health_tree.heading("buoi", text="Buổi ăn")
        self.health_tree.heading("monan", text="Món ăn")
        self.health_tree.heading("calo", text="Calories")
        self.health_tree.heading("soluong", text="Số lượng")
        self.health_tree.heading("tongcalo", text="Tổng calo")
        self.health_tree.grid(column=0, row=1, sticky="we", pady=(10,0))

        self.health_tree.bind("<Button-3>", self.on_click_select_option)

        #________________________
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
            vietnamese_to_english = {
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

            if value_vn not in vietnamese_to_english:
                messagebox.showerror("Lỗi", f"Không tìm thấy {value_vn}")
                return
            value_en = vietnamese_to_english[value_vn]

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
        if not self.mon_an_type_entry or not self.mon_an_so_luong_entry:
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin")
            return
        elif not self.mon_an_so_luong_entry.get().strip().isdigit():
            messagebox.showerror("Lỗi", "Số lượng phải là một số nguyên dương.")
            self.mon_an_so_luong_entry.config(bg="red")
            return
        else:
            raw_input = self.mon_an_type_entry.get().strip()
            value_vn = raw_input.lower()

            vietnamese_to_english = {
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

            if value_vn not in vietnamese_to_english:
                messagebox.showerror("Lỗi", f"Không tìm thấy {value_vn}")
                return
            value_en = vietnamese_to_english[value_vn]
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
                #self.mon_an_so_luong_entry.insert(0, "1")
                self.buoi_an.set("Sáng")

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
        selected_item = self.health_tree.identify_row(event.y)
        if selected_item:
            self.health_tree.selection_set(selected_item)

            self.health_tree_menu = tk.Menu(self.root, tearoff=0)
            self.health_tree_menu.add_command(label="Sửa", font=("Segoe UI", 12))
            self.health_tree_menu.add_command(label="Xóa", font=("Segoe UI", 12))
            self.health_tree_menu.add_separator()
            self.health_tree_menu.add_command(label="Thoát", font=("Segoe UI", 12), command=lambda: None)

            self.health_tree_menu.tk_popup(event.x_root, event.y_root)

    # def on_click_select_option(self, event):
    # # Đóng menu cũ nếu có
    #     if hasattr(self, "custom_menu") and self.custom_menu.winfo_exists():
    #         self.custom_menu.destroy()

    #     # Tạo menu popup bằng Toplevel
    #     self.custom_menu = tk.Toplevel(self.root)
    #     self.custom_menu.overrideredirect(True)  # Ẩn viền cửa sổ
    #     self.custom_menu.geometry(f"+{event.x_root}+{event.y_root}")

    #     # Làm nền và bo góc (trong giới hạn)
    #     frame = tk.Frame(self.custom_menu, bg="#f0f0f0", bd=2, relief="raised")
    #     frame.pack()

    #     def close_menu():
    #         self.custom_menu.destroy()

    #     tk.Button(frame, text="Sửa", command=lambda: print("Sửa")).pack(fill="x")
    #     tk.Button(frame, text="Xóa", command=lambda: print("Xóa")).pack(fill="x")
    #     tk.Button(frame, text="Thoát", command=close_menu).pack(fill="x")

    #___________________________________________________________________Theo dõi________________________________________
    def show_theo_doi(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        self.tai_khoan_btn.config(bg="#40E0D0")
        self.luyen_tap_btn.config(bg="#40E0D0")
        self.dinh_duong_btn.config(bg="#40E0D0")
        self.theo_doi_btn.config(bg="#008080")
        self.list_user_btn.config(bg="#40E0D0")

        tk.Label(self.content_frame, text="Theo dõi").grid(column=0, row=0)



    #___________________________________________________________________List user________________________________________________________________
    def show_listUser(self):
        self.tai_khoan_btn.config(bg="#40E0D0")
        self.luyen_tap_btn.config(bg="#40E0D0")
        self.dinh_duong_btn.config(bg="#40E0D0")
        self.theo_doi_btn.config(bg="#40E0D0")
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



import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

# File JSON để lưu trữ dữ liệu
DATA_FILE = "health_log.json"

# Hàm đọc dữ liệu từ file JSON
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

# Hàm ghi dữ liệu vào file JSON
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Hàm thêm dữ liệu mới
def add_entry():
    weight = weight_entry.get()
    height = height_entry.get()
    medical_history = medical_history_entry.get()
    goal = goal_entry.get()

    if not weight or not height or not goal:
        messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")
        return

    new_entry = {
        "weight": weight,
        "height": height,
        "medical_history": medical_history,
        "goal": goal
    }
    data.append(new_entry)
    save_data(data)
    refresh_table()
    clear_entries()
    messagebox.showinfo("Thành công", "Thêm dữ liệu thành công!")

# Hàm làm mới bảng dữ liệu
def refresh_table():
    for row in table.get_children():
        table.delete(row)
    for idx, entry in enumerate(data):
        table.insert("", "end", values=(idx + 1, entry["weight"], entry["height"], entry["medical_history"], entry["goal"]))

# Hàm xóa dữ liệu
def delete_entry():
    selected_item = table.selection()
    if not selected_item:
        messagebox.showerror("Lỗi", "Vui lòng chọn một mục để xóa!")
        return
    item_index = int(table.item(selected_item, "values")[0]) - 1
    del data[item_index]
    save_data(data)
    refresh_table()
    messagebox.showinfo("Thành công", "Xóa dữ liệu thành công!")

# Hàm xóa các trường nhập liệu
def clear_entries():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    medical_history_entry.delete(0, tk.END)
    goal_entry.delete(0, tk.END)

# Tải dữ liệu từ file JSON
data = load_data()

# Tạo giao diện người dùng
root = tk.Tk()
root.title("Ứng dụng Quản lý Nhật ký Sức khỏe")

# Các trường nhập liệu
tk.Label(root, text="Cân nặng (kg):").grid(row=0, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Chiều cao (cm):").grid(row=1, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Lịch sử bệnh lý:").grid(row=2, column=0, padx=10, pady=5)
medical_history_entry = tk.Entry(root)
medical_history_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Mục tiêu sức khỏe:").grid(row=3, column=0, padx=10, pady=5)
goal_entry = tk.Entry(root)
goal_entry.grid(row=3, column=1, padx=10, pady=5)

# Các nút chức năng
tk.Button(root, text="Thêm", command=add_entry).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Xóa", command=delete_entry).grid(row=4, column=1, padx=10, pady=10)

# Bảng hiển thị dữ liệu
columns = ("#1", "#2", "#3", "#4", "#5")
table = ttk.Treeview(root, columns=columns, show="headings")
table.heading("#1", text="STT")
table.heading("#2", text="Cân nặng (kg)")
table.heading("#3", text="Chiều cao (cm)")
table.heading("#4", text="Lịch sử bệnh lý")
table.heading("#5", text="Mục tiêu sức khỏe")
table.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Hiển thị dữ liệu ban đầu
refresh_table()

# Chạy ứng dụng
root.mainloop()
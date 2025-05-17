import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Biểu đồ Line trong Tkinter")
root.geometry("600x400")

# Dữ liệu ví dụ
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Tạo Figure cho biểu đồ
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
ax.plot(x, y, marker='o', color='blue', linestyle='-')
ax.set_title("Biểu đồ Cân nặng theo ngày")
ax.set_xlabel("Ngày")
ax.set_ylabel("Cân nặng (kg)")

# Nhúng Figure vào Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(pady=10)

root.mainloop()

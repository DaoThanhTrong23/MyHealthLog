import tkinter as tk

# Danh sách thực phẩm tiếng Việt
food_list = [
    "chuối", "táo", "cam", "cơm", "ức gà", "bít tết bò", "sườn heo",
    "cá hồi", "trứng", "bánh mì", "sữa", "phô mai", "sữa chua", "khoai tây", "cà rốt", "cà chua",
    "bông cải xanh", "rau bina", "bơ", "hạnh nhân", "óc chó", "bơ đậu phộng", "yến mạch",
    "mì ống", "bánh pizza", "bánh mì kẹp thịt", "cơm chiên", "mì", "đậu hũ", "đậu lăng", "đậu gà",
    "đậu đen", "đậu que", "dưa chuột", "hành tây", "tỏi", "nấm", "tôm",
    "cua", "tôm hùm", "gà tây", "vịt", "thịt xông khói", "xúc xích", "bơ", "dầu ô liu",
    "đường", "mật ong", "sô cô la", "bánh ngọt", "bánh quy", "kem", "cà phê", "trà",
    "nước cam", "nước táo", "bia", "rượu vang", "dưa hấu", "nho", "dứa",
    "dâu tây", "việt quất", "mâm xôi", "đào", "lê", "mận", "anh đào",
    "ngô", "khoai lang", "bí ngô", "bí xanh", "súp lơ", "cải xoăn", "rau diếp",
    "củ dền", "bắp cải", "củ cải", "đậu hà lan", "đậu edamame", "diêm mạch", "hạt chia",
    "hạt lanh", "dừa", "sữa hạnh nhân", "sữa đậu nành", "kem béo", "sốt mayonnaise",
    "sốt cà chua", "mù tạt", "nước xốt salsa", "súp", "bánh mì kẹp", "gà rán", "viên thịt",
    "cá", "sushi", "mì ramen", "há cảo"
]

class AutoCompleteSearch:
    def __init__(self, root):
        self.root = root
        self.root.title("Tìm kiếm thực phẩm")
        
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)
        self.entry.bind("<KeyRelease>", self.on_keyrelease)

        self.listbox = tk.Listbox(root, font=("Arial", 13), width=40)
        self.listbox.pack()
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

    def on_keyrelease(self, event):
        value = self.entry.get()
        self.listbox.delete(0, tk.END)

        if not value:
            for monan in food_list:
                self.listbox.insert(tk.END, monan)

        for item in food_list:
            if value in item.lower():
                self.listbox.insert(tk.END, item)

    def on_select(self, event):
        if not self.listbox.curselection():
            return
        selection = self.listbox.get(self.listbox.curselection())
        self.entry.delete(0, tk.END)
        self.entry.insert(0, selection)
        self.listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoCompleteSearch(root)
    root.mainloop()

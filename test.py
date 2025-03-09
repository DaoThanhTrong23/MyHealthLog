import os

icon_path = "Images/logo.png"

if os.path.exists(icon_path):
    print("✅ Ảnh tồn tại:", icon_path)
else:
    print("❌ Không tìm thấy ảnh:", icon_path)
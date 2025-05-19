from login import LoginApp
import sys
import os

def resource_path(relative_path):
    """ Trả về đường dẫn thực đến file tài nguyên (dùng cho PyInstaller) """
    try:
        # Khi chạy dưới dạng file .exe (PyInstaller), sẽ có biến _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # Khi chạy bằng Python trực tiếp (chưa đóng gói)
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    LoginApp()

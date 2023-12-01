import ctypes

def set_font_size(new_size):
    SPI_SETNONCLIENTMETRICS = 42

    # Khai báo cấu trúc NONCLIENTMETRICS
    class NONCLIENTMETRICS(ctypes.Structure):
        _fields_ = [
            ("cbSize", ctypes.c_uint),
            ("iMenuHeight", ctypes.c_long),
            ("lfMessageFont", ctypes.c_byte * 48)  # Thêm trường lfMessageFont để lưu thông tin về font chữ
        ]

    non_client_metrics = NONCLIENTMETRICS()
    non_client_metrics.cbSize = ctypes.sizeof(NONCLIENTMETRICS)

    # Lấy thông tin hiện tại
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETNONCLIENTMETRICS, non_client_metrics.cbSize, ctypes.byref(non_client_metrics), 0)

    # Thiết lập kích thước font chữ mới
    non_client_metrics.iMenuHeight = new_size

    # Áp dụng thay đổi
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETNONCLIENTMETRICS, non_client_metrics.cbSize, ctypes.byref(non_client_metrics), 2)  # Thêm tham số 2 để áp dụng ngay lập tức

# Thiết lập kích thước font chữ mới (ví dụ: 20)
set_font_size(40)
ctypes.windll.user32.MessageBoxW(0, "KẾT QUẢ TEST PASS", "THÔNG BÁO THÀNH CÔNG", 0x40)
ctypes.windll.user32.MessageBoxW(0, "KẾT QUẢ TEST FAILLLLLLLLLLLLLLLLLLLLLLLLLLLLLL!!!!!!!!!!", "CẢNH BÁO LỖI", 0x10)

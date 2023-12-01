#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Dữ liệu bạn muốn lưu dưới dạng binary
binary_data = b'\x00\x01\x02\x03\x04'

# Tên file bạn muốn tạo hoặc ghi đè
file_path = 'example.bin'

# Mở file với chế độ write binary
with open(file_path, 'wb') as file:
    # Ghi dữ liệu vào file
    file.write(binary_data)

print(f"Dữ liệu đã được lưu vào file {file_path}")

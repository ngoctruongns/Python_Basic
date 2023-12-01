#!/usr/bin/env python
# -*- coding: utf-8 -*-

LICENSE_KEY_DICT = {
    "KEY1": {
        "START": "0000401C3CE0", # Start bluetooth addr
        "STOP" : "F900401C3CE0", # Stop bluetooth addr
        "LICENSE": "DF 83 DA 6A ED"
    },
    "KEY2": {
        "START": "FA00401C3CE0", # Start bluetooth addr
        "STOP" : "E204401C3CE0", # Stop bluetooth addr
        "LICENSE": "C9 FF 28 AA 09"
    },
}

for LICENSE_KEY in LICENSE_KEY_DICT:
    print(LICENSE_KEY)
    print(type(LICENSE_KEY))

# Chuỗi địa chỉ dạng dict
addresses = {
    "KEY1": {
        "START": "0000401C3CE0", # Start bluetooth addr
        "STOP" : "F900401C3CE0", # Stop bluetooth addr
    }
}

# Địa chỉ bạn muốn kiểm tra
address_to_check = "123456789ABC"  # Thay bằng địa chỉ bạn muốn kiểm tra

# Chuyển đổi chuỗi địa chỉ sang dạng hex
start_address = int(addresses["KEY1"]["START"], 16)
stop_address = int(addresses["KEY1"]["STOP"], 16)
address_to_check = int(address_to_check, 16)

# Đảo ngược thứ tự byte của start_address và stop_address
start_address = int.from_bytes(start_address.to_bytes(6, byteorder='big'), byteorder='little')
stop_address = int.from_bytes(stop_address.to_bytes(6, byteorder='big'), byteorder='little')
address_to_check = int.from_bytes(address_to_check.to_bytes(6, byteorder='big'), byteorder='little')

# In ra địa chỉ start_address và stop_address đã đảo ngược thứ tự byte
print(hex(start_address))
print(hex(stop_address))
print(hex(address_to_check))

# Kiểm tra xem địa chỉ có nằm trong giới hạn không
if start_address <= address_to_check <= stop_address:
    print("Địa chỉ nằm trong giới hạn.")
else:
    print("Địa chỉ không nằm trong giới hạn.")

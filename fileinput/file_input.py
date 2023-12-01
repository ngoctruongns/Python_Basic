# import fileinput
import fileinput
import sys

# Mở và đọc tệp tin
for line in fileinput.input('file_text.txt'):
    print(line)




with fileinput.FileInput('file_text.txt', inplace=True, backup='.bak') as file:
    for line in file:
        if 'Hello' in line:
            device_name = "Hello"
            print("")
        else:
            print(line, end="")
# Đóng tệp tin
fileinput.close()
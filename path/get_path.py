import os

# get path this file
file_path = os.path.realpath(__file__)
print(file_path)
# ==> g:\TruongVN\code_ws\Python_Basic\path\get_path.py

# get dir path of this file
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
# ==> g:\TruongVN\code_ws\Python_Basic\path

# jont path
sample_file_path = os.path.join(dir_path, "sample_file.txt")
print(sample_file_path)
# ==> g:\TruongVN\code_ws\Python_Basic\path\sample_file.txt
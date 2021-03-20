import os


folder_path = r"C:\Users\shant\PycharmProjects\codejam\2020\qualification"

print(os.access(folder_path, os.W_OK))
print(os.access(folder_path, os.R_OK))
import os


os.mkdir("my_folder")
print("Directory 'my_folder' created.")


print("Current directory contents:")
print(os.listdir("."))


os.rename("my_folder", "new_folder")
print("Directory renamed to 'new_folder'.")


os.rmdir("new_folder")
print("Directory 'new_folder' deleted.")

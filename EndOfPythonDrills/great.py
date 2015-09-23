import shutil
import os


source = os.listdir("C:\\Users\\student\\Desktop\\FolderA")
destination = ("C:\\Users\\student\\Desktop\\FolderB")

for files in source:
    if files.endswith(".txt"):
        shutil.move(files, destination)

import os
import shutil

srcdir = r'C:\\Users\\student\\Desktop\\FolderA'
destdir = r'C:\\Users\\student\\Desktop\\FolderB'

for filename in os.listdir(srcdir):
    filepath = os.path.join(srcdir, filename)

    with open(filepath, 'r') as f: 
        dataname = f.name

    print dataname

    shutil.move(srcdir, destdir)

#filename or filepath? filepath copies entire folderA over
#and prints out only one file, while filename does nothing

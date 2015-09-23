import os
import shutil

#printing current stats for the source folder
statinfo = os.stat("C:\Users\student\Desktop\source")
#listing out file names in source folder
createdFiles = os.listdir("C:\Users\student\Desktop\source")
#printing out just the modified times of the folder
currentFiles = os.stat("C:\Users\student\Desktop\source").st_mtime

print statinfo
print createdFiles
print currentFiles

#while True:
   # try:
  #     if createdFiles != currentFiles:
  #          print ("updated")
 #  except:
   #     pass


#essentially need to be able to correctly read the files in the create folder and
#execute st_mtime to them and compare the size (st_mtime) with original files and if
#st_mtime is true, then need to me moved to updated folder
            
#how can I list all the files in a list, or array or ? and check if one has been updated?

   

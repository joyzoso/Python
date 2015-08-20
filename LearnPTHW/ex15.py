#Get command line arguments from the sys module or package
from sys import argv
#lins 1-4 uses argv to get the filename, essentially assigning 2 argvs variables
script, filename = argv 

#open is a function and is initially returning the object "txt" and then "txt_again" on line 15
txt = open(filename)
#printing out the argv, in this case the name of the filen
print "Here's your file %r:" % filename
print txt.read() #read is a method, which is being called that is associated with the object "txt"
#prompting user to enter the filename again and adding a prompt character
print "Type the filename again:"
file_again = raw_input("> ")
#once again using a function to return the object, this time called "txt_again"
txt_again = open(file_again)
#print out the file that was entered AND display the contents (do the command or function without any paramaters)
print txt_again.read()

print txt.close()
print txt_again.close()




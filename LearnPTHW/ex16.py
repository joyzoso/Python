from sys import argv
#from the sys module, unpacking argv(s)
script, test = argv

print "We're going to erase %r." % test
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(test, 'w')
#w mode creates the file if it doesn't exist and empties it if it does and opens it for writing

print "Truncating the file. Goodbye!"
target.truncate()
#the above is not really necessary... seems to be done to show that the method exists.
#truncate declares how much of the file you want to remove. 
#but using 'w' also truncates the file if it already exists.

print "Now I'm going to ask for three lines."
#prints these lines but prompts for input at each line
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
#---the above lines is commented out bc below is a better way to code---#

line = '{}\n{}\n{}\n'.format(line1, line2, line3)
target.write(line)
#taking the data and breaking with a new line
target = open(test)
#opening the file again so that you we can...
print target.read()
#actually print out the contents of the file
print "And finally, we close it."
target.close()
#because it is always best practice to do so.
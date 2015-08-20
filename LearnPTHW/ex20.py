from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0) #seek(0) moves the file to the first(0) byte in the file. 


def print_a_line(line_count, f):
	print line_count, f.readline(), #f.readline moves the read head to the right after the /n
	#and adding the comma at the end will eliminate the blank lines inbetween.
current_file = open(input_file)

print "First let's print the whole file: \n"

print_all(current_file)

print "Now lets rewind, kind of like a tape."	

rewind(current_file)	

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1 #this is the same as line 33, just a shorthand way.
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
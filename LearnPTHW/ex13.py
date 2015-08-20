#from sys import argv

#script, first, second, third = argv

#print "The script is called:", script
#print "Your first variable is:", first
#print "Your third variable is:", third

#note that when you run this in the shell, you need to actually
#pass the command line arguments for example:
#python ex13.py first second third


from sys import argv

script, first, second, third = argv
third = raw_input("Where do you live?")

print "In conclusion, your script is called %r, your 1st variable is %r, your 2nd is %r, and you live in %r" % (script, first, second, third)

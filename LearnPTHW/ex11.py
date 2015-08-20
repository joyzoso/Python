print "How old are you?", 
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?"
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (age, height, weight)

#raw_input presents a prompt to the user, gets the input and then returns the data in a string format

#also another edited way to write this is:

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So you're %r old, %r tall and %r heavy." % (age, height, weight)
#defining a function and passing 2 arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	#%d is for decinmal meaning it will take a number
	print "You have %d cheeses!" % cheese_count
	#%d is for decinmal meaning it will take a number
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Wow, that's enough for a party"
	print "Get a party blanket.\n"

#giving the function numbers directly
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)
#using variables within the function and assiging it numbers
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
#calling the function and using the variables defined above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#giving numbers directly in the function but using addition to make it so
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#adding the variables (amt/cheese & crack) with 100/100 respectively
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)



tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" % i,

		#Super neato
		#you may want to comment the loop out before running it or you'll need to force exit the 
		#terminal unless you can figure out the soultion!
		

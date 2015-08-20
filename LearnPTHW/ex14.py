from sys import argv

script, user_name, adjective = argv
prompt = 'You say... '

print "Hi %s, I'm the %s script. You are %s" % (user_name, script, adjective)
print "I'd like to ask you some questions."
print "Do you like me, %s %s?" % (adjective, user_name)
likes = raw_input(prompt)

print "Where do you live, %s %s?" % (adjective, user_name)
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
OK, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer.  Cool. Thanks %s %s!
""" % (likes, lives, computer, adjective, user_name)

#adjective = friendly, racy, cute, etc.... (duh)

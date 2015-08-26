"""
These are 3 ways to get things

#dict style
mystuff['apples']

#module style
mystuff.apples()
print mystuff.tangerine

#class style
thing = MyStuff()
thing.apples()
print thing.tangerine

"""

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])


bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])

led_zeppelin = Song(["Want to tell you about the girl I love",
						"My she looks so fine"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

led_zeppelin.sing_me_a_song()

Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> my_list = ['one', 'two', 'three']
>>> my_list_len = len(my_list)
>>> for i in range(0, my_list_len):
	print(my_list[i])

	
one
two
three
>>> for i in range(3, 0, -1):
	print (i)

	
3
2
1
>>> for i in range(3, -1, -1):
	print (i)

	
3
2
1
0
>>> for in in range (8, 0, 2):
	
SyntaxError: invalid syntax
>>> for i in range (8, 0, 2):
	print (i)

	
>>> for i in range(8, 0, -2):
	print (i)

	
8
6
4
2
>>> 

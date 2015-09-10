def joysort(my_list):
	for placeholder in range(len(my_list)-1, 0, -1):
		maxPosition = 0
		for location in range(1, placeholder+1):
			if my_list[location]>my_list[maxPosition]:
				maxPosition = location

		temp = my_list[placeholder]
		my_list[placeholder] = my_list[maxPosition]
		my_list[maxPosition] = temp

my_list = [67, 45, 2, 13, 1, 998]
joysort(my_list)
print(my_list)

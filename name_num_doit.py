#!/Users/bmsnook/anaconda3/bin/python

from name_num import name_num

def numbers2words():
	"""
	Turn numbers into words
	"""
	my_num = None
	while my_num != "0":
		my_num = input("Please enter a number greater than 0 and less than 1 trillion: ")
		print(name_num(int(my_num.replace(",",""))))
		
# Main
numbers2words()
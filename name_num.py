#!/usr/local/bin/python3

# Include me like this: "from name_num import name_num"

# Set up lists of the words we need; including zero lets indexing work properly
cardinal_unit = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
cardinal_tens = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
cardinal_teen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

def name_num(num, numstr=""):
	"""
	Return a number between 0 and 1 trillion, not inclusive, in words.
	"""
	if num // 1000000000 != 0:
		if num % 1000000000 != 0:
			numstr = name_num(num//1000000000) + " billion, " + name_num(num%1000000000)
		else:
			numstr = name_num(num//1000000000) + " billion"
	else:
		if num // 1000000 != 0:
			if num % 1000000 != 0:
				numstr = name_num(num//1000000) + " million, " + name_num(num%1000000)
			else:
				numstr = name_num(num//1000000) + " million"
		else:
			if num // 1000 != 0:
				if num % 1000 != 0:
					numstr = name_num(num//1000) + " thousand, " + name_num(num%1000)
				else:
					numstr = name_num(num//1000) + " thousand"
			else:
				if num // 100 != 0:
					if num % 100 != 0:
						numstr = name_num(num//100) + " hundred " + name_num(num%100)
					else:
						numstr = name_num(num//100) + " hundred"
				else:
					if num // 10 != 0:
						# Treat numbers >= 20 differently from teens
						if num // 10 > 1:
							if num % 10 != 0:
								numstr = cardinal_tens[num//10] + "-" + cardinal_unit[num%10]
							else:
								numstr = cardinal_tens[num//10]
						else:
							numstr = cardinal_teen[num%10]
					else:
						if num % 10 != 0:
							numstr = cardinal_unit[num]
	return numstr

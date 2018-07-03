#coding: utf-8

repeat = int(raw_input())


for n in range(0,repeat):
	cl = "NULL"
	number = int(raw_input())
	
	if(number%2 == 0):
		if(number > 0 ):
			cl = "EVEN POSITIVE"
		if(number < 0):
			cl = "EVEN NEGATIVE"
	elif(number%2 != 0):
		if(number > 0 ):
			cl = "ODD POSITIVE"
		if(number < 0):
			cl = "ODD NEGATIVE"
		
	print cl

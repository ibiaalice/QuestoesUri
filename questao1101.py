#coding; utf-8


while(True):
	n = raw_input().split()
	n1 = int(n[0])
	n2 = int(n[1])
	
	if(n1 == 0 or n2 == 0):
		break
		
	soma = 0
	numeros = ""
	if (n1 < n2):
		for i in range(n1, n2 + 1):
			soma += i
			numeros += str(i) + " "
	
	if (n2 < n1):
		for i in range(n2, n1 + 1):
			soma += i
			numeros += str(i) + " "
	
	print ( "%sSum=%d" %(numeros , soma))

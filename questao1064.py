#coding: utf-8

positivos = []

for i in range(6):
	n = float(raw_input())
	if n > 0:
		positivos.append(n)

soma = 0	
for i in positivos:
	soma += i 
	
print("%d valores positivos" % len(positivos))
print ("%.1f" %(soma / len(positivos)))

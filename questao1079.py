#coding: utf-8


n = int(raw_input())


for i in range(n):
	notas = raw_input().split(" ")
	n1 = float(notas[0]) * 2
	n2 = float(notas[1]) * 3
	n3 = float(notas[2]) * 5
	
	print("%.1f" % ((n1 + n2 + n3)/10))
	

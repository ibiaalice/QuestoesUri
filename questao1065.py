#coding: utf-8

par = 0 
for i in range(5):
	num = int(raw_input())
	if num % 2 == 0:
		par += 1

print ("%d valores pares" % par)

#coding: utf-8

maior = 0
posicao = 0

for i in range(100):
	n = int(raw_input())
	if (n > maior):
		maior = n
		posicao = i
		
print(maior)
print(posicao + 1)

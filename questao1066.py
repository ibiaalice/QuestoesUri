#coding: utf-8


par = 0
impar = 0
positivo = 0
negativo = 0


for i in range(5):
	n = int(raw_input())
	if n % 2 == 0:
		par += 1
	else:
		impar += 1
	if n > 0:
		positivo += 1
	elif n < 0:
		negativo +=1

print("%d valor(es) par(es)" %par)
print("%d valor(es) impar(es)" %impar)
print("%d valor(es) positivo(s)" %positivo)
print("%d valor(es) negativo(s)" %negativo)

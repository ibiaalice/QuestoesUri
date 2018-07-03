# coding: utf-8


n = int(raw_input())

cobaias = 0
coelho = 0 
rato = 0
sapo = 0

for i in range(n):
	cobaia = raw_input().split(" ")
	n_cobaia = int(cobaia[0])
	
	if(cobaia[1] == "S"):
		sapo += n_cobaia
	elif(cobaia[1] == "R"):
		rato += n_cobaia
	elif(cobaia[1] == "C"):
		coelho += n_cobaia
	
	cobaias += n_cobaia

print ("Total: %d cobaias" % cobaias)
print ("Total de coelhos: %d" % coelho)
print ("Total de ratos: %d" % rato)
print ("Total de sapos: %d" % sapo)

print ("Percentual de coelhos: %.2f %%" % ((100.00 * coelho)/cobaias))
print ("Percentual de ratos: %.2f %%" % ((100.00 * rato) /cobaias))
print ("Percentual de sapos: %.2f %%" % ((100.00 * sapo)/cobaias))

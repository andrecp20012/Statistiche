from math import sqrt

def media(lista):
	s=0
	for i in lista:
		s=s+i
	return s/len(lista)
		
	
def dev(listino):
	s=0
	m=media(listino)
	for i in listino:
		s=(i-m)**2+s
	return sqrt(s/(len(listino)-1))
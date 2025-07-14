from math import sqrt
from scipy.stats import t

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
		
		
def confidenza(listozzo, confidence):
	alpha=(100-confidence)/200
	j=len(listozzo)
	k=dev(listozzo)
	tval=t.ppf(1 - alpha, df=j-1)
	return tval*k/sqrt(j)
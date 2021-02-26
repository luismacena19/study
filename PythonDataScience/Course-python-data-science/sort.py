#!/bin/env python

def searchMinFromList(L,n):
	minValue = L[0]
	idx = 0
	counter = 1
	while(counter <= n):
		v = L[counter]
		if(v < minValue ):
			minValue = v
			idx = counter
		else:
			pass
			counter = counter + 1
	return minValue, idx

def sortList(L,n):
	L2 = []
	counter = 0 
	while(counter <= n):
		m, idx = searchMinFromList(L,n)
		L2.append(m)
		del L[idx]
		n = n - 1
	return L2


L = [0,2,-1,7,8,9]
n = 5
print("\nMenor valor da lista:\n(Valor,Index)")
print(searchMinFromList(L,n), "\n")
print("Lista ordenada:")
print(sortList(L,n))

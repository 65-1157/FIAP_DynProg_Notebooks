# coding: utf-8

#Exercícios de recursão em python 

""" 1. O fatorial de um número natural n é o produto de todos os inteiros positivos menores ou iguais a n. Crie a chamada recursiva de n fatorial"""

def fatorial(n):
	if n == 1:
		return 1
		
	return n* fatorial(n - 1)
	
"""implemente uma função reccursiva que, dados dois números inteiros x e n, calcula o valor de x ** n"""

def exponencial(x, n):
	if n == 0:
		return 1
		
	return x * exponencial(x, n - 1)
	
"""Usando recursividade, calcule a soma de todos os valores de um array de reais"""

def soma(a, n):
	if n == len(a):
		return 0
		
	return a[n] + soma(a, n + 1)
	
"""Dado um array de inteiros inverta a posição dos seus elementos"""

def inverte(a, i):
	if i == len(a) / 2:
		return a
		
	a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]
	return inverte(a, i + 1)
	
"""Em uma função recursiva determine quantas vezes um digito k ocorre em um numero naturaln."""

def conta_digito(d, n, i):
	n = str(n)
	d = str(d)
	
	if i == len(n):
		return 0
		
	if n[i] == d:
		return 1 + conta_digito(d, n, i + 1)
		
	return conta_digito(d, n, i + 1)
	
"""O máximo divisor comum de dois números inteiros x e y pode ser calculado usando-se uma definição recursiva:
 mdc(x, y) = mdc(x - y, y) , se x > y
 mdc(x, y) = mdc(y,x)
 mdc(x, x) = x """
 
def mdc(x, y):
	if x == y:
		return x
		
	if x > y :
		return mdc(x - y, y)
		
	return mdc(y, x)
	






		

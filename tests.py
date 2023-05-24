
from tsp import TSP
from pandas import DataFrame, set_option
import time
from tkinter import *
import itertools
import random as rd
def createRandomCompleteGraph(n, symmetric=True):
	"""
    create a complete symmetric graph with 
	random edge weight
	"""
	from random import randint
	v = [i for i in range(1, n+1)]

	e = []
	M = [[0 for v1 in v] for v2 in v]
	for ind1, i in enumerate(v):
		ind2 = ind1+1
		for j in v[ind1+1:]:
			if i != j:
				w = randint(1, 100)
				e.append((i,j,w))
				e.append((j,i,w))
				M[ind1][ind2] = w
				if symmetric:
					M[ind2][ind1] = w
				else:
					w = randint(1, 10)
					M[ind2][ind1] = w
				ind2 += 1
                

	import numpy as np
	M = np.array(M)
	#print(M, "\n")
	print(M)
	return v, e, M
def random_tour(M):
	N = M.shape[0]
	array = [i for i in range(2,N+1,1)]
	array_per = list(rd.choice(list(itertools.permutations(array))))
	array_per.append(1)
	array_per.insert(0,1)
	return array_per
def brute_force_tour(M, tour):

	_tour = tour[1:-1]

	listt = list(itertools.permutations(_tour))
	brf_tour = []
	import sys
	min_length = sys.maxsize
	for i in listt:
		i = list(i)
		i.append(tour[0])
		i.insert(0,tour[0])
		tourlen = 0
		for j in range(len(i)-1):
			tourlen += M[i[j] - 1, i[j+1] - 1]
		if tourlen < min_length:
			min_length = tourlen
			brf_tour = i
	return brf_tour, min_length
def callAndTime(input_):
	"""
	Wrapper for calling and timing a function
	args:
		input: List 
			func at zeroth index and
			rest are arguments
	"""
	func= input_[0]
	args = input_[1:]
	
	start = time.time()
	ret = func(*args)
	timetaken = time.time() - start
	return ret, timetaken


def test2(n=10):
	"""
	Given number of nodes -
	Test greedy tour using default starting node, 
	two optimal tour using greedy tour
	three optimal tour using greedy tour 
	three optimal tour using two optimal tour
	"""
	v, e, M = createRandomCompleteGraph(n)
	tsp = TSP(v, e)

	print("Greedy tour")
	(greedytour, greedytourlen), time = callAndTime((tsp.greedyTour,)) 
	# print(greedytour, greedytourlen, time)
	array = random_tour(M)
	print(array)
	print("\n2OPT:")
	(twoopttour, twooptlen), time = callAndTime((tsp.twoOPT, array))
	print(twoopttour, twooptlen)
	brf_tour, min_length = brute_force_tour(M, array)
	print('Brute force Algorithm:\n',brf_tour, min_length)
import networkx as nx
import matplotlib.pyplot as plt
   

if __name__ == '__main__':
	test2() 
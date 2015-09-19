# problem is simple, find cycles in the graph.
# HOWEVER, time efficient is the KEY
# use array, set, flags to speed up, store past result, avoid recalculate

# Enter your code here. Read input from STDIN. Print output to STDOUT
from operator import mul
n = int(raw_input())
pointers = []
probs = []
for i in range(n):
    [point, prob] = map(int, raw_input().strip().split(' '))
    pointers.append(point)
    probs.append(prob)
citys = set([i for i in range(1,n+1)]) # set, remove unnecessary loops in the array
cycle_flag = [0]*n # count which cycle the node is in
cycle_count = 1 # count cycle number
expected = 0.0
while len(citys) > 0:
    in_cycle = [] # store nodes in this cycles, for efficient calculation of products
    in_cycle_prob = []
    start = citys.pop()
    in_cycle.append(start)
    in_cycle_prob.append(probs[start-1]/100.0)
    cycle_flag[start-1] = cycle_count
    start = pointers[start-1]
    while start in citys:
        cycle_flag[start-1] = cycle_count
        citys.remove(start)
        in_cycle.append(start)
        in_cycle_prob.append(probs[start-1]/100.0)        
        start = pointers[start-1]
    # found start point of the cycle
    if cycle_flag[start-1] != cycle_count:
        cycle_count += 1
        continue
    start_idx = in_cycle.index(start)
    this_expected = reduce(mul,in_cycle_prob[start_idx:],1)
    expected += this_expected
    cycle_count += 1
print "%.2f" % expected


/*
There are n cities in QuantumLand. Each of the cities may have a one-way road toward another city. QuantumLand is strange, and nothing is certain here; sometimes a road will exist, sometimes it won't!

Given the description of all the cities and roads in QuantumLand and the probability of each road's existence, can you determine the expected number of cycles formed in QuantumLand?

Note: A cycle of length m is is a sequence of nodes u1,u2...,um,u1 such that for every i<m, there is an edge between ui and ui+1. The length of any cycle is at least 2.

Input Format

First line will have an integer n. Each of the next n lines will have two integers w and p. Each ith line denotes that there is a one-way road from city i to city wi with p% probability.
*/

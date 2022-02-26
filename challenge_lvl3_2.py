import random
import time
from collections import deque

def randomList(length, max=1000000):
    l = []
    while len(l) < length:
        i = random.randint(1,max)
        if i not in l:
            l.append(i)
    return list(l)

def divide(a,b):
    return b % a == 0

def copy(l):
    return [i for i in l]

def solution(l):
    n = 0
    t = []
    for index,i in enumerate(l):
        for index2,j in enumerate(l[index+1:]):
            if not divide(i,j):
                continue
            for k in l[index+index2+2:]:
                if divide(j,k):
                    n+=1
                    t.append((i,j,k))
    return t,n

def solution2(l):
    t = []
    u = []
    for index,i in enumerate(l):
        for index2,j in enumerate(l[index+1:]):
            if divide(i,j):
                for k in t:
                    if k['b'][0] == i and k['b'][1] == index: # faut juste trouver la bonne comparaison
                        u.append((k['a'][0], k['b'][0], j))
                t.append({'a':(i, index), 'b':(j,index2+index+1)})
    return (u,len(u))


def solution3(l):
    n = 0
    for index,i in enumerate(l):
        a = 0
        b = 0
        for j in l[index+1:]:
            if divide(i,j):
                a+=1
        for j in l[:index]:
            if divide(j,i):
                b+=1
        n+= a * b
    return n

# tree traversal
# def solution2(l):
#     n = 0
#     t = []
#     for index,i in enumerate(l):
#         t.append[{'k':index, 'v':i}]
#     for i in t:


# l = [1,16,32,2,4,8,16]
# l = [1,1,1]
l = [1,2,3,4,5,6]
print solution(l)
# print solution2(l)
print solution3(l)

# print ""
# print solution(l)
# print solution2(l)

# print ""
# # l = [1,2,3,4,5,6]
# l = [2,4,8,3,6,12]
# print solution(l)
# print solution2(l)
# exit(0)
# l = [1,1,1]
# totaltime1 = 0
# totaltime2 = 0
# for i in xrange(100):
#     l = randomList(500, max=700)
#     t0 = time.time()
#     for i in xrange(10000):
#         s1 = solution(l)
#     t1 = time.time()
#     print "solution : ", t1-t0
#     totaltime1 += t1-t0
#     # print s
#     t0 = time.time()
#     for i in xrange(10000):
#         s2 = solution2(l)
#     t1 = time.time()
#     totaltime2 += t1-t0
#     print "solution 2 : ", t1-t0
#     # print s
#     if s1[1] != s2[1]:
#         print("ERROR:")
#         print "for ", l
#         print "s1 : ", s1
#         print "s2 : ", s2

#     print totaltime1
#     print totaltime2


# print solution(l)

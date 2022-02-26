def convert(n,base):
    neg = n < 0
    n = abs(n)
    tab = []
    while n > 0:
        tab.insert(0, str(n % base))
        n//=base
    if tab == []:
        tab.append(str(0))
    n = ''.join(tab)
    if neg:
        return "-{}".format(n)
    return n

def minusBase(a,b,base):
    res = int(a,base) - int(b, base)
    if base == 10:
        return str(res)
    return convert(res, base)

def sortBase(a,b,base):
    x = minusBase(a,b,base)
    if int(x) == 0:
        return 0
    if x[0] == '-':
        return -1
    return 1

def nextMinion(n, b):
    k = len(n)
    x = ''.join(reversed(sorted([i for i in n])))
    y = ''.join(sorted([i for i in n]))
    z = minusBase(x,y,b)
    while len(z) < k:
        z = "0"+z
    return z

def isTwoTimes(x, tab):
    n = 0
    for i in range(len(tab)):
        if x == tab[i]:
            n+=1
        if n >= 2:
            return True
    return False

def findCycle(tab):
    n = tab[-1]
    m = 0
    for i in range(len(tab)-2, 0, -1):
        if tab[i] != n:
            m+=1
        elif tab[i] == n:
            break
    return m+1

def solution(n,b):
    tab = []
    while True:
        n = nextMinion(n, b)
        tab.append(n)
        if isTwoTimes(n, tab):
            break
    return findCycle(tab)

print solution('210022', 3)
print solution('1211', 10)

# print findCycle([1,1])
# print findCycle([1,2,1])
# print findCycle([1,2,3,4,5,1])
# print isTwoTimes(1,[1,2,3,4,1])


# solution('12343', 10)

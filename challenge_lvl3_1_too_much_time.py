def copy(l):
    c = []
    for i in l:
        c.append(i)
    return c

def innerCombination(cur, index, num, reducedNum, res):
    if reducedNum < 0:
        return
    if reducedNum == 0:
        return res.append(copy(cur[:index]))
    prev = 1 if(index == 0) else cur[index - 1]
    for k in range(prev, num +1):
        cur[index] = k
        innerCombination(cur, index +1, num, reducedNum -k, res)

def combinations(n):
    res = []
    cur = [0] * n
    innerCombination(cur, 0, n, n, res)
    return res

def isValidStair(s):
    s = list(reversed(sorted(s)))
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            return False
    return True

def filterCombinations(comb):
    comb = filter(lambda x : len(x) != 1, comb)
    comb = filter(lambda x : isValidStair(x), comb)
    return comb

def solution(n):
    return len(filterCombinations(combinations(n)))

# print combinations(10)
print len(filterCombinations(combinations(13)))
print ""
print filterCombinations(combinations(13))

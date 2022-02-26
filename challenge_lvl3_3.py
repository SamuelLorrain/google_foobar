import math

def isSquare(x):
    x = math.log(x,2)
    truncX = math.trunc(x)
    return x == truncX

def choose(x):
    a = math.log(x+1,2)
    b = math.log(x-1,2)
    truncA = math.trunc(a)
    truncB = math.trunc(b)
    if truncA == a:
        return x + 1
    if truncB == b:
        return x - 1
    return x-1

def choose2(x, n):
    bNotValid = False
    incX = 1
    a = math.log(x+incX,2)
    while math.trunc(a) != a:
        incX += 1
        a = math.log(x+incX,2)
    decX = 1
    b = math.log(x-decX, 2)
    while math.trunc(b) != b:
        decX += 1
        if (x-decX) <= 0:
            bNotValid = True
            break
        b = math.log(x-decX, 2)
    if bNotValid:
        return (x+incX,n+incX)
    if incX < decX:
        return (x+incX,n+incX)
    else:
        return (x-decX,n+decX)

def choose(n, memo):
    if n in memo:
        return memo[n]
    if n % 2 == 0:
        memo[n] = choose(n/2, memo) + 1
    else:
        a = choose((n+1)/2, memo) + 2
        b = choose((n-1)/2, memo) + 2
        memo[n] = min(a,b)
    return memo[n]

def solution(x):
    x = int(x)
    n = 0
    while x > 1:
        if x & 1 == 0:
            x /= 2
        elif x % 4 == 3 and x > 3:
            x += 1
        else:
            x -= 1
        n+=1
    return n

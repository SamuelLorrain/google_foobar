def copy(l):
    c = []
    for i in l:
        c.append(i)
    return c

def solution(s):
    ## init
    l = len(s)
    right = []
    left = []
    for j,i in enumerate(s):
        if i == '>':
            right.append(j)
        elif i == '<':
            left.append(j)
    n = 0
    old_right = []
    while right != [] and left != []:
        # case 1
        for i in right:
            for j in left:
                if i == j:
                    n+=1

        # case 2
        for i in old_right:
            for j in left:
                if i == j:
                    n+=1
        old_right = copy(right)
        for i in range(0, len(right)):
            right[i] +=1
        for i in range(0, len(left)):
            left[i] -=1
        right = [i for i in right if i < l]
        left = [i for i in left if i > -1]
    return n*2


print solution(">----<")
print solution("<<>><")
print solution("--->-><-><-->-")

def copy(l):
    return [i for i in l]

def addListToDict(newEntry, oldEntry, d, pushFront):
    values = d[oldEntry]
    for i in values:
        t = copy(i)
        t.insert(0, pushFront)
        d[newEntry].append(t)

def getCombinations(n):
    d = {}
    # passed = []
    for a in xrange(3,n+1):
        i = a-1
        j = 1
        for _ in xrange(0,n):
            if i < j:
                # if (j,i) in passed:
                #     break
                if d.get(j, False):
                    for k in d[j]:
                        if k[0] < i:
                            t = [i]
                            for l in k:
                                t.append(l)
                            d[a].append(t)
            elif i == j:
                if d.get(j, False):
                    addListToDict(a, j, d, i)
            else:
                if d.get(a, False):
                    d[a].append([i,j])
                else:
                    d[a] = [[i,j]]
                if d.get(j):
                    addListToDict(a,j,d,i)
            # passed.append((i,j))
            i-=1
            j+=1
    return d

def getComb2(n):
    d = {}
    for a in xrange(3,n+1):
        i = a-1
        j = 1
        for _ in xrange(0,n):
            if i < j:
                break #pb unable to compute those cases
            elif i == j:
                if d.get(j):
                    d[a]+=d[j]
            else:
                if d.get(a, False):
                    d[a]+=1
                else:
                    d[a]=1
                if d.get(j):
                    d[a]+=d[j]
            i-=1
            j+=1
    return d

def getComb3(n):
    d = {}
    for a in xrange(3,n+1):
        i = a-1
        j = 1
        for _ in xrange(0,n):
            if i < j:
                if d.get(j):
                    x = d[j]['beg']
                    y = 0
                    for key,value in x.items():
                        if key < i:
                            y+=value
                    if y != 0:
                        d[a]['total']+=y
                        d[a]['beg'][i]=y
            elif i == j:
                if d.get(j):
                    d[a]['total']+=d[j]['total']
                    d[a]['beg'][i]=d[j]['total']
            else:
                if d.get(a, False):
                    d[a]['total']+=1
                    d[a]['beg'][i]=1
                else:
                    d[a]={'total':1, 'beg':{i:1}}
                if d.get(j):
                    d[a]['total']+=d[j]['total']
                    d[a]['beg'][i]+=d[j]['total']
            i-=1
            j+=1
    return d

def solution(n):
    return getComb3(n)[n]['total']

n = 100
print len(getCombinations(n)[n])
print ""
print getComb3(n)[n]['total']

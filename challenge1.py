def solution(area):
    tab = []
    while area > 0:
        for i in range(area, 0, -1):
            x = i*i
            if x <= area:
                area-=x
                tab.append(x)
                break
    return tab

print solution(12)
print solution(15324)

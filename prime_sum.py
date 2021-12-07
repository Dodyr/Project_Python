N = 2000000
crossed = [False]*N
summ=0
i = 2
while i<N:
    summ = summ + i
    j = i*2
    while j<N:
        crossed[j]=True
        j = j + i
    i = i + 1
    while i < N and crossed[i]:
        i = i + 1
print(summ)

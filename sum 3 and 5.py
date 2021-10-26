sum_ = 0
i = 1
while i<1000:
    if i%3==0 or i%5==0:
        sum_ = sum_ + i
    i = i + 1
print(sum_)

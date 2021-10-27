x1 = 1
x2 = 2
x3 = 3
sum_ = x2
while x3<=4000000:
    x1 = x2
    x_ad = x3
    x3=x3+x2
    x2 = x_ad
    if x3%2==0:
        sum_+=x3
print(sum_)

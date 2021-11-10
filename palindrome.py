#!/usr/bin/python
def is_pal(num):
    temp=num
    rev=0
    while(temp>0):
        dig=temp%10
        rev=rev*10+dig
        temp=temp//10
    return (num==rev)

def div_100(num):
    found=False
    sec_dig=0
    i=999
    while i>100 and not found:
        if num%i==0:
            sec_dig=num//i
            if sec_dig>99 and sec_dig<1000:
                found=True
        i = i-1
    return found

number=998001
found=False
while not found:
    if is_pal(number):
        if div_100(number):
            found=True
    if not found:
        number= number-1
print(number)

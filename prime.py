def isPrime(num):
    for i in range(2,int(sqrt(num))+1):
        if (num%i==0):
            return false
    return true

problem = 600851475143
i = 2
large_prime = 0
while i<=problem:
    while (problem % i ==0):
        problem =  problem / i
        large_prime = i
    i = i + 1
print(large_prime)

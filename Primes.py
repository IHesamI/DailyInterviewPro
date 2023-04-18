def implement_algorithm(number:int,primes:list):
    new_prime=primes
    for i in range(number*2,len(primes),number):
        new_prime[i]=False
    return new_prime
def find_primes(n):
    primes=n*[True]
    primes[0]=False
    primes[1]=False
    for i in range(2,n):
        if primes[i]==True:
            primes=implement_algorithm(i,primes)
            
    return [index for index,value in enumerate(primes) if value==True]

print(find_primes(14))
# [2, 3, 5, 7, 11, 13]
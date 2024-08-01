def prime_generator(limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    num = 2
    while num <= limit:
        if is_prime(num):
            yield num
        num += 1

for prime in prime_generator(20):
    print(prime)  

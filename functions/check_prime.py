def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def list_primes(limit):
    return [num for num in range(2, limit+1) if is_prime(num)]


number = int(input("Enter a number to check prime or not: "))
print(is_prime(number)) 

limit = int(input("Enter the limit to get the list of primes: "))
prime_list = list_primes(limit)

print(prime_list)
"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if check(number_of_primes) == False:
        return Null
    
    list = []
    counter = 2
    while len(list) <number_of_primes :
        verification = False
        print(list)
        for div in range(2,counter):
            
            if counter % div == 0:
                verification = True
            div += 1
            
        if verification == False:
            list.append(counter)
        counter += 1
    return list

def check(number_of_primes):
    if number_of_primes < 1:
        return False
    else:
        return True

print(primes(10))

"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
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

print(primes(10))

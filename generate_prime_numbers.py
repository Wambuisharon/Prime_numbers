def generate_primes(number):

    #make sure its a number
    if not isinstance(number,int):
        return "Invalid input!Enter a digit"
    # make sure x is a positive integer
    if number<0:
        return "Negative numbers are not permited"
    
    prime_numbers = []    
    for n in range(2,number):
        prime = True    
        for y in range(2, int(n**0.5) + 1, 2):
            if n % y == 0:
                prime = False
        if prime : prime_numbers+=[n]        
    return prime_numbers
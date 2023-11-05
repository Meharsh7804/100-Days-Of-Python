def isPrime(number):
    if number <= 1:
        return False  # 1 and numbers less than 1 are not prime
    
    if number <= 3:
        return True  # 2 and 3 are prime

    if number % 2 == 0:
        return False  # Even numbers greater than 2 are not prime

    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False  # It's divisible by some other number
    
    return True  # It's prime

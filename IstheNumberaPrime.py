def primeorno(n):
    factor = 2
    if n > 1:
        while factor < n:
            if n % factor == 0:
                return False
            else:
                factor += 1
    elif n <= 1:
        return False
    else:
        return True
if primeorno(int(input())) == False:
    print ('The number is not prime.')
else:
    print ('The number is prime.')
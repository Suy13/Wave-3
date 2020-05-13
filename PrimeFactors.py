n = int(input('Enter an integer (2 or greater):'))
factor = 2
if n < 2:
    print ('ERROR :)')
else:
    print ('The prime factors of',n,'are:')
while factor <= n:
    if n % factor == 0:
        print (factor)
        n //= factor
    else:
        factor += 1
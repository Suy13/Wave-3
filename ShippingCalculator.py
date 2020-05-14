#format (value,'.2f') - value = number, '.2f' = decimal places after
def charge(n):
    if n > 1:
        return format(round((((n - 1) * 2.95) + 10.95),2),'.2f')
    elif n == 1:
        return round(10.95,2)
    elif n == 0:
        return 0
print ('$',charge(int(input())))
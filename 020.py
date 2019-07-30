import math

def sum_of_digits(n):
    t = 0;
    while n != 0:
        t += n % 10;
        n //= 10;
    return t;

print(sum_of_digits(math.factorial(100)));

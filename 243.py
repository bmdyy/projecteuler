# totient function
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47];
def r(d):
    prod = d;
    for prime in primes:
        if d % prime == 0:
            prod *= (1 - 1/prime);
    return prod / (d - 1);

def is_prime(n):
    if n <= 3:
        return n > 1;
    elif n % 2 == 0 or n % 3 == 0:
        return False;
    i = 5;
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False;
        i += 6;
    return True;

ul = 15499 / 94744;
a = 2 * 3 * 5 * 7 * 9 * 11 * 13 * 17 * 19;
r_a = 1;
best_low = 1;
while r_a > ul:
    r_a = r(a);
    if r_a < best_low:
        best_low = r_a;
        print(a, r_a);
    if r_a <= ul:
        print(a, 'winner');
        break;
    a += 1;

# all prime have r(d) = 1.0 -> skip

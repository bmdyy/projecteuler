def match(n):
    p = 1020304050607080900;

    while n > 0:
        n_ = n % 10;
        p_ = p % 10;

        if n_ != p_:
            return False;

        n //= 100; # skip _
        p //= 100;
    return True;

l_lim = 1010101010; # sqrt(1020304050607080900)
u_lim = 1389026623; # sqrt(1929394959697989990)

for i in range(l_lim, u_lim + 1, 10): # form ends with 0 -> i must end with 0
    if match(i * i):
        break;
    
print(i);

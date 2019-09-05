def ways_to_create(n, c):
  # n = coinsum to create,
  # c = set of denominations
  W = [0] * (n + 1); # +1 to avoid overflow
  W[0] = 1; # there is 1 way to create a sum of '0'
  for i in range(len(c)): # iterate through all coins 
    for j in range(len(W)): # compare each coin to the 'ways' index
      if c[i] <= j: # if the coin amt is lower than the index of 'ways'
                    # then there are additional ways to create the sum 
        W[j] += W[j - c[i]]; # add the additional ways 

  return W[n]; # return the number at index n

british_denominations = [1, 2, 5, 10, 20, 50, 100, 200];
print(ways_to_create(200, british_denominations));

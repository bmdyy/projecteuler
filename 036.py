def is_palindrome(n):
  n_ = str(n);
  len_n_ = len(n_) - 1;
  for i in range(len_n_):
    if n_[i] != n_[len_n_ - i]:
      return False;
  return True;

total = 0;
for i in range(1000000):
  if is_palindrome(i) and is_palindrome(bin(i)[2:]): # bin returns 0b??...?
    total += i;
print(total);

def seq(n):
  if n % 2 == 0:
    return n / 2;
  else:
    return 3 * n + 1;

def len_seq(n):
  length = 1;
  while n != 1:
    length += 1;
    n = seq(n);
  return length;

curr = 999999;
longest_chain = 0;
longest_chain_start = 0;

while curr > 1:
  curr_chain = len_seq(curr);
  if (curr_chain > longest_chain):
    longest_chain_start = curr;
    longest_chain = curr_chain;
  curr -= 1;

print(longest_chain_start);

a = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'];
b = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'];

for i in range(len(a)):
  a[i] = len(a[i]);

for i in range(len(b)):
  b[i] = len(b[i]);

def len_num_as_text(n):
  ret = 0;

  if n == 1000:
    return len('onethousand');

  if n >= 100:
    m = n // 100;
    ret += a[m - 1] + len('hundred');
    n %= 100;
    if n > 0:
      ret += len('and');

  if n >= 20:
    m = n // 10;
    ret += b[m - 2];
    n %= 10;

  if n > 0 and n < 20:
    ret += a[n - 1];

  return ret;

total = 0;
for i in range(1, 1001):
  total += len_num_as_text(i);
print(total);

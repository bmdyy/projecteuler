curr = 1; # f2
prev = 1; # f1
index = 2;

while curr < 10**999:
  temp = curr;
  curr = curr + prev;
  prev = temp;
  index = index + 1;

print(index);

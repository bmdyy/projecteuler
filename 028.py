wh = 1001; # width/height
total = 0;
while wh > 0:
  if wh == 1:
    total += 1;
  else:
    a = wh * wh;
    b = wh - 1;
    total += 4 * a - 6 * b;
  wh -= 2;
print(total);

'''
tr = wh * wh; # top right;
tl = tr - (wh - 1); # top left
bl = tl - (wh - 1); # bottom left;
br = bl - (wh - 1); # bottom right
total += tr + tl + bl + br;
----------------------------------
a = wh*wh;
b = (wh-1);
tr = a;
tl = a - b;
bl = a - b - b;
br = a - b - b - b;
# total += a + a - b + a - b - b + a - b - b - b;
total += 4 * a - 6 * b;
'''

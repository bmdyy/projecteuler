def generate_permutations2(a, size, n, A):
  if (size == 1):
    a_str = "";
    for i in a:
      a_str += str(i);
    A.append(a_str);
    return;
  
  for i in range(size):
    generate_permutations2(a, size - 1, n, A);
    
    if (size & 1):
      a[0], a[size - 1] = a[size - 1], a[0];
    else:
      a[i], a[size - 1] = a[size - 1], a[i];


def generate_permutations(a, A):
  return generate_permutations2(a, len(a), len(a), A);

def merge_sort(a):
  if len(a) > 1:
    mid = len(a)//2; # 1.
    left = a[:mid];
    right = a[mid:];

    merge_sort(left); # 2.
    merge_sort(right);

    i = j = k = 0;

    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        a[k] = left[i];
        i += 1;
      else:
        a[k] = right[j];
        j += 1;
      k += 1;

    while i < len(left):
      a[k] = left[i];
      i += 1;
      k += 1;

    while j < len(right):
      a[k] = right[j];
      j += 1;
      k += 1;

PERM = [];
generate_permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], PERM);
merge_sort(PERM);
print(PERM[999999]); # millionth lexographical permutation of 0-9

import random

def insertion_sort_inplace(array):
  for index, value in enumerate(array):
    if index == 0:
      continue

    i = index - 1
    while i>=0 and array[i] > value:
      array[i+1] = array[i]
      i = i - 1

    array[i + 1] = value

  return array

my_randoms = [random.randrange(1, 101, 1) for _ in range(20)]
print(insertion_sort_inplace(my_randoms))
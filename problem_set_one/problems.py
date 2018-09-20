# Given a set of integers (distinct), find pairs which differ by a given integer k


def find_pairs_with_difference(input_set, difference):
  pairs_with_difference = []
  sorted_set = sorted(input_set)
  print(sorted_set)
  for index, value in enumerate(sorted_set):
    for value2 in sorted_set[index + 1:]:
      if (value2 - value == difference):
        print (value, value2)
        pairs_with_difference.append((value, value2))
  return pairs_with_difference



def test_find_pairs_with_difference():
  input_set = {1, 7, 5, 3, 9, 12}
  difference = 2
  expected_pairs = [(1, 3), (3, 5), (5, 7), (7, 9)]
  pairs = find_pairs_with_difference(input_set, difference)
  print(pairs == expected_pairs)

test_find_pairs_with_difference()

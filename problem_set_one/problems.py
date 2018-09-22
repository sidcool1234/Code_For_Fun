# 1. Given a set of integers (distinct), find pairs which differ by a given integer k


def find_pairs_with_difference(input_set, difference):
  sorted_set = sorted(input_set)
  return [(value, value+difference) for value in sorted_set if value + difference in sorted_set]



def test_find_pairs_with_difference():
  input_set = {1, 7, 5, 3, 9, 12, 37}
  difference = 2
  expected_pairs = [(1, 3), (3, 5), (5, 7), (7, 9)]
  pairs = find_pairs_with_difference(input_set, difference)
  print pairs
  print("Test Passing?", pairs == expected_pairs)


test_find_pairs_with_difference()

# -----------------------------------------------------------------------------#

# 2.


# https://www.interviewbit.com/problems/min-steps-in-infinite-grid/

class Solution:
  # @param A : list of integers
  # @param B : list of integers
  # @return an integer
  def cover_points(self, A, B):
    count = 0

    for idxA, valA in enumerate(A):
      if(idxA < len(A) - 1):
        valB = B[idxA]
        source = [valA, valB]
        target = [A[idxA + 1], B[idxA + 1]]
        count = self.cover_pair(source, target) + count


    return count

  def cover_pair(self, source, target):
    count = 0
    x_from = source[0]
    x_to = target[0]
    y_from = source[1]
    y_to = target[1]

    while x_from!=x_to or y_from!=y_to:
      if x_from!=x_to and y_from!=y_to:
        if(x_from < x_to):
          x_from = x_from + 1
        else:
          x_from = x_from - 1

        if(y_from < y_to):
          y_from = y_from + 1
        else:
          y_from = y_from - 1
        count = count + 1

      if x_from!=x_to and y_from==y_to:
        if(x_from < x_to):
          x_from = x_from + 1
        else:
          x_from = x_from - 1

        count = count + 1

      if x_from==x_to and y_from!=y_to:
        if(y_from < y_to):
          y_from = y_from + 1
        else:
          y_from = y_from - 1

        count = count + 1

    return count


# def test_cover_pair():
#   x = Solution().cover_pair([0,1], [4,3])
#   print(x)
#
# def test_cover_points():
#   x = Solution().cover_points([-7, -13], [1, -5])
#   print(x)
#
# test_cover_points()
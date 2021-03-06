# https://www.interviewbit.com/problems/min-steps-in-infinite-grid/

class Solution_p1:
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

  # Better Solution
  def another_cover_pair(self, source, target):
    #return max(abs(point_from[0] - point_to[0], point_from[1] - point_to[1]))
    return max(abs(source[0]-target[0]), abs(source[1]-target[1]))


  # Bad Solution
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


class Solution:
  def addTwoNumbers(self, l1, l2):
      l1.reverse()
      l2.reverse()

      print(l1, l2) 

      total = int("".join("{0}".format(n) for n in l1)) + int("".join("{0}".format(n) for n in l2))
      list = []
      for i in reversed(str(total)):
        list.append(i)

      return list

  def fibonacci(self, till_number):
    if till_number <= 1:
      return till_number

    return self.fibonacci(till_number - 1) + self.fibonacci(till_number - 2)

print(Solution().fibonacci(12))
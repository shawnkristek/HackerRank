# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

class Solution:
    def diagonalDifference(arr):
        # Write your code here
        def get_diagonal_sum(dir: str, matrix: list[list[int]]) -> int:
            _sum = 0
            for i in range(len(matrix)):
                if dir=='left':
                    _sum += matrix[i][i]
                else:
                    _sum += matrix[i][len(matrix)-1-i]
            return _sum
        
        left = get_diagonal_sum('left', arr)
        right = get_diagonal_sum('right', arr)
        return abs(left-right)

# tests
tests = [ 
    (
        [[11,2,4],
         [4,5,6],
         [10,8,-12]],
         15
    ),
]

for arr, solution in tests:
    sol = Solution.diagonalDifference(arr)
    print( sol == solution )
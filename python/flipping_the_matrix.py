from timeit import timeit

class Solution:
    @timeit
    def flippingMatrix(matrix):
        # https://www.hackerrank.com/challenges/flipping-the-matrix/
        # flip a 2nx2n matrix
        # 1. split matrix into 4 quadrants
        # 2. add the max of the 4 possible values for each position
        # 3. return total

        size = len(matrix)
        N = size // 2

        #adjust for 0 index
        size -= 1 

        total = 0

        for i in range(N):
            for j in range(N):
                total += max(
                    # flipping rows/cols means each position has 4 possible values
                    # add the max to the total
                    matrix[i][j],
                    matrix[i][size-j],
                    matrix[size-i][j],
                    matrix[size-i][size-j],
                )

        return total 
    

# testing
tests = [
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 54),
    ([[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]], 414),
    ([[1,2],[4,3]], 4),
    ([[107, 54, 128, 15],[12, 75, 110, 138],[100, 96, 34, 85],[75, 15, 28, 112]], 488),
]

# run tests
for matrix, solution in tests:
    sol = Solution.flippingMatrix(matrix)
    print( sol )
    assert sol == solution
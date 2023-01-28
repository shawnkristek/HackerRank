class Solution:
    # Complete the 'gridChallenge' funciton below.
    def gridChallenge(grid):

        # explode immutable strings
        grid = [list(row) for row in grid]

        # sort rows
        for row in grid:
            row.sort()

        # check order of columns
        for j in range(len(grid[0])):
            for i in range(1, len(grid)):
                if not grid[i-1][j] <= grid[i][j]:
                    return "NO"

        return "YES"

# tests

tests = [
    (
        [
            'ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'
        ],
        "YES"
    ),
    (
        [
            'abc', 'lmp', 'qrt'
        ],
        "YES"
    ),
    (
        [
            'mpxz', 'abcd', 'wlmf'
        ],
        "NO"
    ),
    (
        [
            'abc', 'hjk', 'mpq', 'rtv'
        ],
        "YES"
    )
]

# run tests
for grid, solution in tests:
    sol = Solution.gridChallenge(grid)
    print( sol )
    assert sol == solution


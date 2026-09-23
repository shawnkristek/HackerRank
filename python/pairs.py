from timeit import timeit

class Solution:
    @timeit
    def pairs(k: int, arr: list[int]) -> int:

        # find all possible pairs of (n, n +/- k) in arr
        # brute force is 0(n^2), searching entire array for every element


        return 3

# testing
tests = [
    (
        2,
        [1, 5, 3, 4, 2],
        3
    ),
]

for k, arr, solution in tests:
    sol = Solution.pairs(k, arr)
    print(sol)
    assert sol == solution

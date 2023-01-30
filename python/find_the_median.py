from timeit import timeit

class Solution:
    @timeit
    def findMedian(arr):
        arr.sort()
        return arr[len(arr)//2]

#testing
tests = [
    ([0,2,3,4,6,5,3], 3),
    ([1,2,3,4,5,5,6,7,8,9,19], 5),
    ([1,2,3,4,5], 3)

]

# run tests
for arr, solution in tests:
    sol = Solution.findMedian(arr)
    print( sol )
    assert sol == solution
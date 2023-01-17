class Solution1:
    def hourglassSum(arr):
        _max = float('-inf')

        for i in range(1,5):
            for j in range(1,5):
                _sum = 0
                _sum += arr[i][j]
                _sum += arr[i-1][j-1]
                _sum += arr[i-1][j]
                _sum += arr[i-1][j+1]
                _sum += arr[i+1][j-1]
                _sum += arr[i+1][j]
                _sum += arr[i+1][j+1]
                _max = max(_max, _sum)

        return _max

class Solution2:
    def hourglassSum(arr):
        # is there a way to reuse previous sums?
        # breaking it down into sums of three rows: always need to access middle value, top and btm sums could be reused
        # subtract last left value, add new right value
        # it would save to array reads per hourglass, requires storing two sum values
        # did not take into account the need to initialize the top and btm sums on each row, this adds more complexity that may negate the benefits
        _max = float('-inf')

        for i in range(1,5):
            _sumTop = 0
            _sumBtm = 0
            for j in range(1,5):
                _sum = 0
                # middle value
                _sum += arr[i][j]

                # top row
                _sumTop += -arr[i-1][j-2] + arr[i-1][j+1]
                _sum += _sumTop

                # btm row
                _sumBtm += -arr[i+1][j-2] + arr[i+1][j+1]

                # max
                _max = max(_max, _sum)
        
        return _max



# tests 
tests = [
    (
        [[-9,-9,-9,1,1,1],
         [0,-9,0,4,3,2],
         [-9,-9,-9,1,2,3],
         [0,0,8,6,6,0],
         [0,0,0,-2,0,0],
         [0,0,1,2,4,0]],
         28
    ),
    (
        [[1,1,1,0,0,0],
         [0,1,0,0,0,0],
         [1,1,1,0,0,0],
         [0,0,2,4,4,0],
         [0,0,0,2,0,0],
         [0,0,1,2,4,0]],
         19
    ),
]

for arr, solution in tests:
    sol = Solution2.hourglassSum(arr)
    print(sol == solution)
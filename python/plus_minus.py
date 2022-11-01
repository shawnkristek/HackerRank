#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

class Solution:
    def plusMinus(arr):
        # Write your code here
        #counters + - 0
        counts = [0,0,0] 
        for n in arr:
            if n > 0:
                counts[0] += 1 
            elif n < 0:
                counts[1] += 1
            else:
                counts[2] += 1
                
        output = [0]*3
        for i in range(3):
            ratio = counts[i]/len(arr)
            # print('%.6f'%ratio)
            output[i] = '%.6f'%ratio
        return output
    
    # tests
tests = [ 
    (
        [1,1,0,-1,-1],
        ["0.400000",
        "0.400000",
        "0.200000"]
    ),
]
    
for arr, solution in tests:
    sol = Solution.plusMinus(arr)
    print( sol == solution )
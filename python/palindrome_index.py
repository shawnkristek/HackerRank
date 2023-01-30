from timeit import timeit

# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
class Solution:
    @timeit
    def palindromeIndex(s):
        # Write your code here
        
        # shrinking window / two pointers left, right
        l, r = 0, -1
        index = -1
        found = False
        while l <= len(s)+r:
            if s[l] != s[r]:
                if found:
                    return -1
                # peak two char left, one right
                if s[l+1]==s[r] and s[l+2]==s[r-1]:
                    found = True
                    index = l
                    # bump left pointer
                    l += 1
                # peak two char right, one left
                elif s[l]==s[r-1] and s[l+1]==s[r-2]:
                    found = True
                    index = len(s)+r
                    # bump right pointer
                    r -= 1
            l += 1
            r -= 1
        return index
                    
    
# tests
tests = [ 
    ( "a", -1 ),
    ( "", -1 ),
    ( "acbdbba", -1),
    ( "aaab", 3 ),
    ( "acbba", 1 ),
    ( "hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh", 44 ),
]

for s, solution in tests:
    sol = Solution.palindromeIndex(s)
    print( sol )
    assert( sol == solution ) 

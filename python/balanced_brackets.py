from timeit import timeit

class Solution:
    def isBalanced(s: str) -> str:

        # use a stack
        stack = []

        for b in s:
            if b in '({[':
                # push opening brackets to stack
                stack.append(b)
            else:
                if len(stack) == 0:
                    return 'NO'
                else:
                    # pop and check when current is closing bracket
                    top = stack.pop()
                    if ( 
                        ( b == ')' and top == '(' ) or
                        ( b == '}' and top == '{' ) or 
                        ( b == ']' and top == '[' )
                    ):
                        continue
                    else:
                        return 'NO' 

        # account for last bracket = open bracket
        return 'YES' if len(stack) == 0 else 'NO'

# testing

tests = [
    ( '{[()]}', 'YES' ),
    ( '{[(])}', 'NO' ),
    ( '{{[[(())]]}}', 'YES' ),
    ( '{{([])}}', 'YES' ),
    ( '{{)[](}}', 'NO' ),
    ( '{(([])[])[]}', 'YES' ),
    ( '{(([])[])[]]}', 'NO' ),
    ( '{(([])[])[]}[]', 'YES' ),
    ( '{(([])[])[]}[', 'NO' ),
]

for s, solution in tests:
    sol = Solution.isBalanced(s)
    print( sol )
    assert sol == solution 
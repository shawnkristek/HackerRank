from timeit import timeit

class Solution:
    @timeit
    def minimumBribes(q: list[int]) -> int | str:

        bribes = 0
        # for ea person in q
        for i, p in enumerate(q):
            # check positions from original
            diff = p - (i+1)
            if diff > 2:
                return 'Too chaotic'
            # count individuals that bribed current person 
            for n in q[max(p-2, 0): i]:
                if n > p:
                    bribes += 1

        return bribes


#test

tests = [
    (
        [2, 1, 5, 3, 4],
        3
    ),
    (
        [2, 5, 1, 3, 4],
        'Too chaotic'
    ),
    (
        [1, 2, 5, 3, 7, 8, 6, 4],
        7
    ),
    (
        [5, 1, 2, 3, 7, 8, 6, 4],
        'Too chaotic'
    ),
    (
        [2, 1, 5, 6, 3, 4, 8, 7], 
        6
    )
]

for q, solution in tests:
    sol = Solution.minimumBribes(q)
    print(sol)
    assert sol == solution
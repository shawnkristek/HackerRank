"""
FizzBuzz
Given a number N, print the numbers from 1 to N. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". Also for number which are multiple of both three and five, print "FizzBuzz".

"""

class Solution:
    def fizzBuzz(n):
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
        
tests = [
    (
        15,
        ["1", "2", "Fizz", ]
    ),
    (
    ),
]
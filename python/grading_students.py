class Solution1:
    def gradingStudents(grades):
        def round5(number):
            return 5 * round(number/5)
            
        rounded_grades = []
        for i in range(len(grades)):
            if grades[i] < 38:
                rounded_grades.append(grades[i])
            elif round5(grades[i]) < grades[i]:
                rounded_grades.append(grades[i])
            else:
                rounded_grades.append(round5(grades[i]))

        return rounded_grades

# tests
tests = [
    (
        [73,67,38,33],
        [75,67,40,33]
    ),
    (
        [33,38,73],
        [33,40,75]
    ),
    (
        [73,67,38,33,33],
        [75,67,40,33,33]
    ),
]

# run tests
for grades, solution in tests:
    sol = Solution1.gradingStudents(grades)
    print(sol)
    assert sol == solution 
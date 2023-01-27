from timeit import timeit

class Solution:
    # input: n: string, k: integer
    # output: single digit integer
    # @timeit
    # def superDigit(n: str, k: int) -> int:

    #     def helper(n: ) -> int:
    #     # sum digits while digit sum > 9 
    #         while (n > 9):
    #             n = sum( [int(i) for i in str(n)] )

    #         return n

    #     p = helper(n) * k
    
    #     return helper(p)
    pass

class Solution1:
    @timeit
    def superDigit(n: str, k: int) -> int:

        def helper(n: str) -> int:
            total = 0
            # convert digits to int and add to total
            for num in n:
                total += int(num)
            # total = str(total)
            # return total if total is a single digit
            if total < 10:
                return total
            else:
                # recurse 
                return helper(str(total))

        p = str(helper(n) * k)

        return helper(p)


tests = [
    ( '148', 3, 3 ),
    ( '9875', 4, 8 ),
    ( '123', 3, 9 ),
    ( '1', 1, 1 ),
    (
        '7404954009694227446246375747227852213692570890717884174001587537145838723390362624487926131161112710589127423098959327020544003395792482625191721603328307774998124389641069884634086849138515079220750462317357487762780480576640689175346956135668451835480490089962406773267569650663927778867764315211280625033388271518264961090111547480467065229843613873499846390257375933040086863430523668050046930387013897062106309406874425001127890574986610018093859693455518413268914361859000614904461902442822577552997680098389183082654625098817411306985010658756762152160904278169491634807464356130877526392725432086439934006728914411061861235300979536190100734360684054557448454640750198466877185875290011114667186730452681943043971812380628117527172389889545776779555664826488520325234792648448625225364535053605515386730925070072896004645416713682004600636574389040662827182696337187610904694029221880801372864040345567230941110986028568372710970460116491983700312243090679537497139499778923997433720159174153',
        100000,
        3
    )
]

for n, k, solution in tests:
    sol = Solution1.superDigit(n, k)
    print(sol)
    assert sol == solution
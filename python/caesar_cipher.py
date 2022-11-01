class Solution1:
    def caesarCipher(s: str, k: int) -> str:
        output = [""] * len(s)
        for i,char in enumerate(s): 
            # determine if char upper, lower, or non-alpha
            dec = ord(char)
            upper = char.isupper()
            alpha = char.isalpha()
            
            if not alpha:
                output[i] = s[i]
    
            # adjust for shifts passing end of alphabet
            if alpha:
                new_chr = dec + k
                if upper:
                    A = ord('A')
                    Z = ord('Z')
                    while new_chr > Z:
                        new_chr -= Z 
                    if new_chr < A:
                        new_chr += ord('A') - 1
                if not upper:
                    a = ord('a')
                    z = ord('z')
                    while new_chr > z:
                        new_chr -= z
                    if new_chr < a:
                        new_chr += ord('a') - 1
                # update character in output
                output[i] = chr(new_chr)
        
        return "".join(output)

class Solution2:
    def caesarCipher(s: str, k: int) -> str:
        a = ord('a')
        z = ord('z')
        # generate the k-shifted alphabet
        shifted_alphabet = [''] * 26
        shift = k % 26
        for i in range(26):
            dec = a + i + shift
            if dec > z:
                dec += a - z - 1
            shifted_alphabet[i] = chr(dec) 

        # build output string
        output = [''] * len(s)
        for i,char in enumerate(s):
            alpha = char.isalpha()
            upper = char.isupper()

            if alpha:
                dec = ord(char) if not upper else ord(char.lower())
                indx = dec - a
                new_chr = shifted_alphabet[indx] if not upper else shifted_alphabet[indx].upper()
            else:
                new_chr = char

            output[i] = new_chr

        return "".join(output)

class Solution3:
    def caesarCipher(s: str, k: int) -> str:
        a = ord('a')
        z = ord('z')
        # generate the k-shifted alphabet
        shifted_alphabet = {}
        shift = k % 26
        for i in range(26):
            dec = a + i + shift
            if dec > z:
                dec += a - z - 1
            shifted_alphabet[chr(a+i)] = chr(dec) 
        
        # build output string
        output = [''] * len(s)
        for i,char in enumerate(s):
            alpha = char.isalpha()
            upper = char.isupper()

            if alpha:
                key = char if not upper else char.lower()
                new_chr = shifted_alphabet[key] if not upper else shifted_alphabet[key].upper()
            else:
                new_chr = char

            output[i] = new_chr

        return "".join(output)



# test
tests = [ 
    (
        "middle-Outz",
        2,
        "okffng-Qwvb"
    ),
    (
        "There's-a-starman-waiting-in-the-sky",
        3,
        "Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb"
    ),
    (
        "abcxyz",
        26,
        "abcxyz"
    )
]

for s,k,solution in tests:
    sol = Solution3.caesarCipher(s,k)
    print( sol == solution)

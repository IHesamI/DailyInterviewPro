import re
class Solution():
    def __init__(self) -> None:
        self.dict_of_Alphabet = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }
        self.regex = r'L|V|M|D|(I(?!(X|V))|IV|IX)|(X(?!(C|L))|XL|XC)|(C(?!(M|D))|CD|CM)'
    def romanToInt(self, s):
        x = 0
        print(s)
        for roman in  [x.group() for x in re.finditer(self.regex, s)]:
            x+=self.dict_of_Alphabet[roman]
        return x
n = 'IX'
print(Solution().romanToInt(n))
# 1910

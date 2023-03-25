import re
class Solution:
    def isValid(self, s):
        crosspend={
            '}':'{',
            ']':'[',
            ')':'(',
        }
        stack = []
        for char in s:
            if re.match(r'\(|\[|\{', char):
                stack.append(char)
            else:
                try:
                   if crosspend[char]== stack[-1]:
                       stack.pop()
                   else:
                       return False
                except Exception:
                    return False
        return True if len(stack) == 0 else False


# # Test Program
s = "({[)]}"
# # should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))

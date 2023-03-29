class Solution:
    def reverseWords(self, str):
        new_str = ''
        words=str.split(' ')
        for word in words:
            new_str+=word[::-1]+' '
        return new_str.strip()


print(Solution().reverseWords("The cat in the hat"))
# ehT tac ni eht tah

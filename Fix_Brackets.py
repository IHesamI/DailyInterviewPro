def fix_brackets(s):
    stack = []
    for char in s:
        if '(' == char:
            stack.append(char)
        else:            
            try:
                if stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(char)
            except Exception:
                stack.append(char)
    return len(stack)

print(fix_brackets('(()()))'))
# 1

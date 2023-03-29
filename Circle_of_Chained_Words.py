def chainedWords(words):
    for i in range(len(words)-1):
        if words[i+1][0]!=words[i][-1]:
            return False
    return True


print(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))
# True

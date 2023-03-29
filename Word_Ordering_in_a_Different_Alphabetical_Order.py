import re
def isSorted(words, order):
    order_regex = order.replace('', '*')[1:]
    order_regex = re.compile(order_regex)
    for each_word in words:
        if not re.fullmatch(order_regex, each_word):
            return False
        
        
    return True


print(isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False
print(isSorted(["zyx", "zyxw", "zyyxw"], "zyxwvutsrqponmlkjihgfedcba"))
# True

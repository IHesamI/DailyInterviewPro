import math
def change_order(start,stop,list_char):
    for index in range(0,stop-start):
        if index+start==math.ceil((start+stop)/2):
            break
        list_char[start+index],list_char[stop-index]=list_char[stop-index],list_char[start+index]        

def reverse_words(words:list):
    index_of_spaces=[]
    new_word=words[::-1]
    for index,char in enumerate(new_word):
        if char==' ':
            index_of_spaces.append(index)
    index_of_spaces.append(len(new_word))
    start=-1
    for each_index in index_of_spaces:
        change_order(start+1,each_index-1,new_word)
        start=each_index
    return new_word
s = list("can you read this")
s=reverse_words(s)
print(''.join(s))
# this read you can

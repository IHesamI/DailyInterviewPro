def should_break(d):
    for value in d.values():
        if type(value)==dict().__class__:
            return False
    return True
def flatten_dictionary(d:dict):
    keys=list(d.keys())
    while True:
        for i in keys:
            if type(d[i])==dict().__class__:
                innerdict={ i+"."+key:value   for key,value in d[i].items()}
                d.pop(i)
                d.update(innerdict)
        keys=list(d.keys())
        if should_break(d):
            break
    return d
            
    
#   for key,value in d.items():
#       if type(value)==flated_dict:
#           flat_dic(key,value)
#       else:
#           flated_dict[key]=value

d = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    }
}
print(flatten_dictionary(d))
# {'a': 1, 'b.c': 2, 'b.d.e': 3}
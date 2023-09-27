# unpack operator: unpack values from iterable objects as:lists and dict
# * -> any iterable object, ** -> for dict
# it unpack the iterable to seperated varibles with 
l= [1,2,3]
print(l)
print(*l) # print(1,2,3) -> 1 2 3
 
def sum_num(x,y,z):
    return x+y+z


print(sum_num(*l))



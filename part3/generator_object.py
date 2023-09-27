# we use it only to itetate over it's items, we don't care about it's len or ......
# it us efficient in using the memory when dealing with large numbers
from sys import getsizeof

values = (i*2 for i in range(1000))   # ( )
print(getsizeof(values))
print(type(values))


#Array:

from array import array
numbers = array('i',[1,2,3,4]) #it's typed which mean that all have the same type inside it

# ----------------------
#sets:
# - unorder so you can not access its elements using index like lists
# - don't accept duplicats - if you have list with duplicated and convert it to set, so duplicated will be removed - 
# - you can use the sets know operatioin on it
first = [1,2,3,4]
second = {1,7,9}
first = set(first)
print( first | second)

# -----------------------
#Dictionary:
# keys of dic should be immutable only, but valued can be from anytype
dic_1 = {"x":'Mohamed' ,"y":1} 
dic_2 = dict(x = 1, y = 4) # keyword argumemt
dic_1['x'] 
# dic_1['z'] #it will return error, because we are accessing an element that don't exist
dic_1.get('z',0)  #if z not exist as a key, it will return 0
del dic_2['y'] #if you del key,then you delete the value
print('here',dic_1.items())

for key,value in dic_1.items():   #items turn dic to listt of tupels, and then we can unpack it
    print(key,value)
# ----------
# we can also use the dic comperhension
list1 = [1,2,3]
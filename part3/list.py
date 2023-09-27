#list Charastericts:

# Casting to a list:

zero = [0]*10  #-> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

numbers = list(range(20)) # ->[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] 



# UNPACKING:
letters= ["A","B","C"]

letters[0:-2]   #-> from 0 to (3+(-2)) = [0,1]
first,*other,last = letters
print(first,last)
print(other)

#
for x in zip(range(len(letters)),letters):
    print(x)  # -> list of tuples 
    
for i,f in enumerate(letters): #match index with values in a tuple, it's the same as above
    print(i,f)


lst = [1,2,3,4,5]
for i ,y in zip(range(len(lst)),lst):
    print(f"the value of i is : {i} and the value of y is: {y}")

# --------------------------------
letters= ["A","B","C","D"]

#Adding element:
letters.append("Mohamed")       #insert the value in the end of the list
letters.insert(0,"fathi")       #insert a value in a specific index, without losing the original element by overriding

#Deleting:
letters.pop()                   # if you don't define the index,it will delete the last element
letters.pop(1)                  # if you don't define the index,it will delete the last element
del letters[0:3]                #slice and del 
letters.remove("D")             #remove list by the value not the index
letters.clear()                 # clear the vlaues
# -----------------------------
#Finding index:
letters= ["A","B","C","D"]

letters.index("A")              #find the index of the vlaue A,it will give an error if this value has no index so should check at first

if "G" in letters:                             
    letters.index("G")


# ----------------------------------------
person = [
    ("ali",19,2500),
    ("hassan",20,3000),
    ("ahmed",5,10000)
]

data = [1,2,5,8,6,4]
print(id(data))
data.sort()                     #apply sorting in the original list
print(id(data))

new_data = sorted(data,reverse=True) # make a copy of the original and apply sorting to ti
#How to sort a dic or tuple with the value of a custom field? select this field by build a func -> pass it 
def sort_fn(person):
    return person[1]
person.sort(key=sort_fn) 


# or
person.sort(key=sort_fn,reverse=True)
person.sort(key = lambda peron:peron[2])
person_sorted = False
person_list = sorted(person,key=lambda person:person[2] if person_sorted ==1 else person[1]) # lambda function used

# -----------------------------------------
salary = list(map(lambda person:(person[0],person[2]),person)) #map take the lamda and applay it to each item of iterable 
print(salary)

def calculate_tax(item):
    return item[1]*item[2]

salary =list(map(calculate_tax,person)) # we can use any functoiin to applay not only the lampda
print(salary)


salary = list(map(lambda person:person[1]>10,person)) # return the boolean result
print(salary)
salary = list(filter(lambda person:person[1]>10,person)) # return the whole item
print(salary)

new_salary = [calculate_tax(person) for person in person]
print(new_salary)

#-----------------------------
# 2 Lists Combination:

list1 = [1,2,3,4,5]
list2 = [9,5,7,0]

x = list(zip(list1,list2))

# # ----------------------------
# DEQUE and stack-quae to effictive left append
from collections import deque
list2 = deque([9,5,7,0])

#1- not support sorting
#2- mutable: change value but kept id

# list2.insert(2, "c")
# # ---------------------------
# #Tuple secial data_structure:
# t= (1,2,3,4)
# t_1=tuple([1,2,3,4]) #you can add any iterable
# t_2 = 1,2,3
# t_3 = 1,
# # ---------------------------
#Swaping 2 Variables:
x,y = 5,5 #here we define a tuple and unpack it
x,y = (5,5)
# ------------------------
sentence = input("Write your sentense: ")
dic1 = {}
for letter in sentence:
    if letter not in dic1.keys():
        dic1[letter]=1
    else:
        dic1[letter]+=1
print(dic1)
print(dic1.items())

# l= []
# i = 0

# for key,val in dic1.items():
#     if val >i:
#         l.clear()
#         i = val
#         l.append(key)
#     elif val == i:
#         l.append(key)
# print(l)

sorted_dic= sorted(dic1.items(),key=lambda x:x[1])
print(sorted_dic[0])
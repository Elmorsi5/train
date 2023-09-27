dic1 = {}
nums = [3,2,3]
for i in nums:
    if i not in dic1:
        dic1[i] = 1
    else: 
        dic1[i] = dic1[i] + 1

print(dic1)
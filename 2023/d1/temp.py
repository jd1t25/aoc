dic = {
    "one" : 1,
    "two" : 2
}

l = "one1two2"

for key,val in dic.items():
    res=l.replace(key,str(val))
    l=res

res = [i for i in res if i.isdigit()]
print(res)

# dic ={
#     'one' : 1,
#     'two' : 2,
# } 
# l = "1two3twoone"
# t = {}
# temp,temp2 = [],[]



# for key,val in dic.items():
#     index = 0
#     while index < len(l):
#         index = l.find(key,index)
#         if index == -1:
#             break
#         temp.append(key)
#         temp.append(index)
#         index += len(key)
#     temp2.append(temp)
#     temp = []

# print(temp2)
total = 0
t = []
temp = []
string = ""
dic = {
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9
}


sublist,mainlist = [],[]

with open(r"I:\Code\AOC\d1\1.txt", "r") as f:
    for q,line in enumerate(f):
        for key,val in dic.items():
            index = 0
            length = len(key)
            while index+length < len(line):
                if index+length < len(line):
                    if line[index:index+length] == key:
                        t.extend([dic[key],index])
                        temp.append(t)
                        t = []
                        index += length
                        n = 1
                    index += 1
        for index,i in enumerate(line):
            if i.isdigit():
                t.extend([i,index])
                temp.append(t)
                t = []
                n = 1
        res = list(sorted(temp, key=lambda x:x[1]))
        result = str(res[0][0]) + str(res[-1][0])
        total += int(result)
        temp = []
print(total)
                # if n==1:
                #     t.append

                

    #     for key,val in dic.items():
    #         sublist.extend([val,line.rfind(key)])
    #         sublist.extend([val,line.find(key)])
    #         if not sublist[1] == -1:
    #             mainlist.append(sublist)
    #         sublist = []

    #     for index,i in enumerate(line):
    #         if i.isdigit():
    #             sublist.extend([i,index])
    #             mainlist.append(sublist)
    #             sublist = []
        
    #     res = list(sorted(mainlist, key=lambda x:x[1]))
    #     result = str(res[0][0]) + str(res[-1][0])
    #     total += int(result)
    #     mainlist = []
    # print(total)

# with open(r"I:\Code\AOC\d1\1.txt", "r") as f:
#     for line in f:
#         for key,val in dic.items():
#             index = 0
#             while index<len(line):
#                 index = line.find(key,index)
#                 if index == -1:
#                     break
#                 sublist.append(key)
#                 sublist.append(index)
#                 index += len(key)
#             mainlist.append(sublist)
#             # if key in line:
#             #     t.update({val:line.find(key)})
        
#         for index,i in enumerate(line):
#             if i.isdigit():
#                 t.update({i:index})
        
#         res = list(sorted(t.items(), key=lambda x:x[1]))

#         result = str(res[0][0]) + str(res[-1][0])

#         total += int(result)
#         t = {}
#         # if len(res) > 1:
#         #     num1,num2 = str(res[0]),str(res[-1])
#         #     num1 += num2
#         #     total += int(num1)
#         # else:
#         #     num = str(res[0])
#         #     num += num
#         #     total += int(num)
#     print(total)
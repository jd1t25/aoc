with open(r'I:\Code\AOC\d5\1.txt','r') as file:
    board = [f.strip() for f in file]
    board.append('')

find = board[0].split()[1:]
find = [int(f) for f in find]

find_new = []


index = []

for idx,i in enumerate(board):
    temp = i.split('\n')
    if "map" in temp[0]:
        index.append(idx+1)
index.append(len(board))

def mapping(mapping_list,seed_find):
    # mapping_get = []
    mapping_list = mapping_list
    mapping_found = 0
    i = 0
    while i < len(mapping_list):
        map_list = mapping_list[i].split(' ')
        if map_list != ['']:
            if int(map_list[1]) <= seed_find and (int(map_list[1])+ int(map_list[2])) >= seed_find:
                mapping_found = 1
                break
            # return ((seed_find - int(map_list[1])) + int(map_list[0]))
        # else:
        #     return(seed_find)
        i += 1
    if mapping_found:
        return ((seed_find - int(map_list[1])) + int(map_list[0]))
    else:
        return(seed_find)

    # for mapping_find in seed_find:
    #     while mapping_list[i] != "":
    #         s2smap = mapping_list[i].split(' ')
    #         if int(s2smap[1]) <= mapping_find and (int(s2smap[1])+int(s2smap[2])) >= mapping_find:
    #             mapping_found = 1
    #             break
    #         i += 1

    #     if mapping_found:
    #         mapping_get.append((mapping_find - int(s2smap[1])) + int(s2smap[0]))
    #     else:
    #         mapping_get.append(mapping_find)
    #     i = 0
    #     mapping_found = 0
    # return mapping_get
open(r'I:\Code\AOC\d5\output.txt','w').close()
idx = 0
find_main = []
file_output = open(r'I:\Code\AOC\d5\output.txt','w')
while idx in range(len(find)):
    if idx % 2 == 0:
        count = int(find[idx+1])
        jdx = 0
        # find_new = [f+find[idx] for f in range(count)]
        while jdx < count:
            find_new = jdx+find[idx]
            seed_2_soil_map_got = mapping(board[index[0]:index[1]-1],find_new)
            soil_2_fer_map_got = mapping(board[index[1]:index[2]-1],seed_2_soil_map_got)
            fer_2_water_map_got = mapping(board[index[2]:index[3]-1],soil_2_fer_map_got)
            water_2_light_map_got = mapping(board[index[3]:index[4]-1],fer_2_water_map_got)
            light_2_temp_map_got = mapping(board[index[4]:index[5]-1],water_2_light_map_got)
            temp_2_hum_map_got = mapping(board[index[5]:index[6]-1],light_2_temp_map_got)
            hum_2_loc_map_got = mapping(board[index[6]:len(board)],temp_2_hum_map_got)
            file_output.write(str(hum_2_loc_map_got) + "\t")
            jdx += 1
        file_output.write("\n")
            # find_main.append(min(hum_2_loc_map_got))
    else:
        pass
    idx += 1

file_output.close()


open(r'I:\Code\AOC\d5\min_output.txt','w').close()
min_output = open(r'I:\Code\AOC\d5\min_output.txt','w')
with open(r'I:\Code\AOC\d5\output.txt','r') as f:
    board = [lines.rstrip('\n').split('\t') for lines in f]
    # board = [lines.replace(' ', '') for lines in f]
    # board = board.split("\n")
    # print(board[0][:-1])
    for lines in board:
        min_board = lines[:-1]
        min_output.write(str(min(min_board)) + "\t")
        # print(min(min_board))
    
    # min_board = [min(lines) for lines in board[][:-1]]
    # print(min_board)
# print(min(find_main))
min_output.close()

with open(r'I:\Code\AOC\d5\min_output.txt','r') as f:
    board = f.readlines()
    board = board[0].split('\t')
    # board = lines.split('\t') for lines in f
    print(min(board[:-1]))

# mapp_temp = []

# for i in range(7):
#     if i != 0:
#         mapp_temp.append(mapping(board[index[i]:index[i+1]-1],mapp_temp[i-1]))
#     else:
#         mapp_temp.append(mapping(board[index[i]:index[i+1]-1],find))
    # mapp1 = "mapp"+str(i)
    # mapp2 = "mapp"+str(i-1)
    # if i != 0:
    #     mapp1=mapping(board[index[i]:index[i+1]-1],mapp2)
    # else:
    #     mapp1=mapping(board[index[i]:index[i+1]-1],find)
# print(mapp_temp[len(mapp_temp)-1])

# print(seed_2_soil_map_got)
# print(soil_2_fer_map_got)
# print(fer_2_water_map_got)
# print(water_2_light_map_got)
# print(light_2_temp_map_got)
# print(temp_2_hum_map_got)

# seed_find = int(find[0])
# soil_get = []

# for seed_find in find:
#     while board[i] != "":
#         s2smap = board[i].split(' ')
#         if int(s2smap[1]) <= seed_find and (int(s2smap[1])+int(s2smap[2])) >= seed_find:
#             seed_found = 1
#             break
#         i += 1

#     if seed_found:
#         soil_get.append((seed_find - int(s2smap[1])) + int(s2smap[0]))
#     else:
#         soil_get.append(seed_find)
#     i = 0
#     seed_found = 0

# print(soil_get)

# idx=0
# while idx < len(board):
#     if board[idx] == "seed-to-soil map:":
#         print(idx)
#     idx += 1


# print(board[index[0]:index[1]-1])
# print(board[index[6]:len(board)])
# index.append(len(board))
    # if type(i) == str:
    #     index.append(int(i))

# seed_2_soil = 0
# soil_2_fer = 0
# fer_2_water = 0
# water_2_light = 0
# light_to_temperature = 0

# i = 0
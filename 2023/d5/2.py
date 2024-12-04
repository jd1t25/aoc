with open(r'I:\Code\AOC\d5\test.txt','r') as file:
    board = [f.strip() for f in file]
    board.append('')

map = ['seeds','soil_to_soil','soil_to_fer','fer_to_water','water_to_light','light_to_temp','temp_to_hum','hum_to_loc']

map_range = []

def initial_mapping():
    temp = []
    
    for lines in board:
        if lines != '':
            temp.append(lines)
        else:
            map_range.append(temp)
            temp = []
   
def string_to_int(string):
    string_int = [int(i) for i in string]
    return string_int

# print(board)
initial_mapping()

 # print(map_range)
seed_find = map_range[0][1].split(' ')
seed_find = string_to_int(seed_find)
seed_to_soil = map_range[1][1:]
soil_to_fer = map_range[2][1:]
fer_to_water = map_range[3][1:]
water_to_light = map_range[4][1:]
light_to_temp = map_range[5][1:]
temp_to_hum = map_range[6][1:]
hum_to_loc = map_range[7][1:]
# print(hum_to_loc)
    
# print(seed_find)
# print(map_range)
print(seed_find)
print(seed_to_soil)

main = []

def s2s():
    for string in seed_to_soil:
        string_map = string_to_int(string.split(' '))
        if string_map[1] <= seed_find[0] <= string_map[1]+string_map[2]:
           for idx,i in enumerate(range(string_map[0])):
                if idx == 1:
                    
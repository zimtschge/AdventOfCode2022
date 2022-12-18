import os.path

input_file = os.path.dirname(os.path.realpath(__file__)) + "/ExampleInput.txt"
input_file = os.path.dirname(os.path.realpath(__file__)) + "/MyInput.txt"

#First read in the hight map
hight_map = []
with open(input_file) as map:
    for row in map.readlines():
        row_list = []
        for point in row:
            try:
                row_list.append(int(point))
            except:
                pass
        hight_map.append(row_list)

map_size = len(hight_map[0])

visible_cnt = 0

for row_ind in range(map_size):
    for col_ind in range(map_size):
        visible = False
        tree_hight = hight_map[row_ind][col_ind]

        # Trees at the edge of the map are visible
        if (row_ind == 0) \
            or (col_ind == 0) \
            or (row_ind == (map_size-1)) \
            or (col_ind == (map_size-1)): 
            visible = True
        
        # Is the tree visible from top?
        if not visible:
            blocked = False
            for i in range(row_ind):
                if hight_map[i][col_ind] >= tree_hight:
                    blocked = True

            if not blocked: visible = True
        
        # Is the tree visible from bottom?
        if not visible:
            blocked = False
            for i in range(row_ind+1, map_size):
                if hight_map[i][col_ind] >= tree_hight:
                    blocked = True

            if not blocked: visible = True

        # Is the tree visible from the left?
        if not visible:
            blocked = False
            for i in range(col_ind):
                if hight_map[row_ind][i] >= tree_hight:
                    blocked = True

            if not blocked: visible = True

        # Is the tree visible from the right?
        if not visible:
            blocked = False
            for i in range(col_ind+1, map_size):
                if hight_map[row_ind][i] >= tree_hight:
                    blocked = True

            if not blocked: visible = True

        if visible: 
            visible_cnt = visible_cnt +1 

print("Answer for part 1: ", visible_cnt)

# Now calculate the viewing distance
viewing_distance_map = []

for row_ind in range(map_size):
    viewing_distance_row = []
    for col_ind in range(map_size):
        tree_hight = hight_map[row_ind][col_ind]
        
        # Viewing distance up
        up_distance = 0
        for i in range(row_ind-1,-1,-1):
            up_distance = up_distance + 1
            if hight_map[i][col_ind] >= tree_hight:
                break

        # Viewing distance down
        down_distance = 0
        for i in range(row_ind+1, map_size):
            down_distance = down_distance + 1
            if hight_map[i][col_ind] >= tree_hight:
                break

        # Viewing distance left
        left_distance = 0
        for i in range(col_ind-1, -1, -1):
            left_distance = left_distance + 1
            if hight_map[row_ind][i] >= tree_hight:
                break

        # Viewing distance right
        right_distance = 0
        for i in range(col_ind+1, map_size):
            right_distance = right_distance + 1
            if hight_map[row_ind][i] >= tree_hight:
                break

        viewing_distance = up_distance*down_distance*left_distance*right_distance
        viewing_distance_row.append(viewing_distance)

    viewing_distance_map.append(viewing_distance_row)

print("Answer for part 2:", max(max(x) for x in viewing_distance_map))
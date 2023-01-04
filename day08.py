def construct_map_from_data(input_file):
    
    map = []
    
    with open(input_file) as file:
    
        row = 0
        for line in file:
            map.append([])

            line = line.split()
            
            col = 0
            for num in line[0]:
                map[row].append(int(num))
                
            row += 1

    return map

def find_visible_trees(map):
    
    visible_count = 0

    row = 0    
    for r in map:

        col = 0
        for c in r:

            if (
                is_visible_left (map[row][col], row, col, map) or
                is_visible_right(map[row][col], row, col, map) or
                is_visible_up   (map[row][col], row, col, map) or
                is_visible_down (map[row][col], row, col, map)
            ):
                visible_count += 1
            
            col += 1
        
        row += 1

    return visible_count

def viewing_dist_left(height, row, col, map):
    
    viewing_distance = 0

    if col == 0:
        return 0
    elif height > map[row][col-1]:
        viewing_distance += 1
        return viewing_distance + viewing_dist_left(height, row, col-1, map)
    else:
        return 1

def viewing_dist_right(height, row, col, map):
    
    viewing_distance = 0

    if col == len(map[row])-1:
        return 0
    elif height > map[row][col+1]:
        viewing_distance += 1
        return viewing_distance + viewing_dist_right(height, row, col+1, map)
    else:
        return 1

def viewing_dist_up(height, row, col, map):
    
    viewing_distance = 0

    if row == 0:
        return 0
    elif height > map[row-1][col]:
        viewing_distance += 1
        return viewing_distance + viewing_dist_up(height, row-1, col, map)
    else:
        return 1

def viewing_dist_down(height, row, col, map):
    
    viewing_distance = 0

    if row == len(map)-1:
        return 0
    elif height > map[row+1][col]:
        viewing_distance += 1
        return viewing_distance + viewing_dist_down(height, row+1, col, map)
    else:
        return 1

def find_max_scenic_score(map):
    max_scenic_score = 0

    row = 0
    for r in map:

        col = 0
        for c in r:

            scenic_score = (
                viewing_dist_left (map[row][col], row, col, map) *
                viewing_dist_right(map[row][col], row, col, map) *
                viewing_dist_up   (map[row][col], row, col, map) *
                viewing_dist_down (map[row][col], row, col, map)
            )

            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

            col += 1
        
        row += 1

    return max_scenic_score

def is_visible_left(height, row, col, map):

    if col == 0:
        return True
    elif height > map[row][col-1]:
        return is_visible_left(height,row, col-1, map)
    else:
        return False

def is_visible_right(height, row, col, map):

    if col == len(map[row])-1:
        return True
    elif height > map[row][col+1]:
        return is_visible_right(height, row, col+1, map)
    else:
        return False

def is_visible_up(height, row, col, map):
    
    if row == 0:
        return True
    elif height > map[row-1][col]:
        return is_visible_up(height, row-1, col, map)
    else:
        return False

def is_visible_down(height, row, col, map):
    
    if row == len(map)-1:
        return True
    elif height > map[row+1][col]:
        return is_visible_down(height, row+1, col, map)
    else:
        return False


# part 1
map = construct_map_from_data("day8_input.txt")
print(find_visible_trees(map))

# part 2
map = construct_map_from_data("day8_input.txt")
print(find_max_scenic_score(map))


# testing area

# row = 3
# col = 2

# print('height:  ' + str(map[row][col]))
# print('left:    ' + str(is_visible_left (map[row][col], row, col, map)))
# print('right:   ' + str(is_visible_right(map[row][col], row, col, map)))
# print('up:      ' + str(is_visible_up   (map[row][col], row, col, map)))
# print('down:    ' + str(is_visible_down (map[row][col], row, col, map)))

# print('height:  ' + str(map[row][col]))
# left = viewing_dist_left (map[row][col], row, col, map)
# right = viewing_dist_right (map[row][col], row, col, map)
# up = viewing_dist_up (map[row][col], row, col, map)
# down = viewing_dist_down (map[row][col], row, col, map)
# print('left:    ' + str(left))
# print('right:   ' + str(right))
# print('up:      ' + str(up))
# print('down:    ' + str(down))
# print('scenic score: '+ str(left*right*up*down))

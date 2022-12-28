import matplotlib.pyplot as plt
import matplotlib.animation as animation

def get_moves(input_file):
    
    moves = []
    
    with open(input_file) as file:
        
        for line in file:

            line = line.split()
            move=(line[0],int(line[1]))
            
            moves.append(move)

    return moves

def get_head_positions(moves):
    
    head_positions = [(0,0)]
    
    position_index = 0 
    
    for move in moves:
        direction = move[0]
        amount = move[1]
        
        for step in range(amount):
            current_position = head_positions[position_index]
            
            match direction:
                case 'R':
                    new_position = (current_position[0]+1,current_position[1])
                case 'U':
                    new_position = (current_position[0],current_position[1]+1)
                case 'L':
                    new_position = (current_position[0]-1,current_position[1])
                case 'D':
                    new_position = (current_position[0],current_position[1]-1)
                case _:
                    print("Encountered invalid direction")
            
            head_positions.append (new_position)
            position_index += 1
            
    return head_positions

def get_tail_positions(head_positions):
    
    tail_positions = []
    
    position_index = -1
    
    previous_head_position = (0,0)
    
    for head_position in head_positions:
        if len(tail_positions) == 0:
            previous_tail_position = (0,0)
        else:
            previous_tail_position = tail_positions[position_index]
        
        if is_tail_adjacent(head_position, previous_tail_position):
            new_tail_position = previous_tail_position
        else:
            # # clever part 1 solution:
            # new_tail_position = previous_head_position
            
            # part 2 solution:
            tail_position_delta = (head_position[0] - previous_tail_position[0], head_position[1] - previous_tail_position[1])
            match tail_position_delta:
                case (1, 2) | (2, 1):
                    new_tail_position = previous_tail_position[0] + 1, previous_tail_position[1] + 1
                case (-1, -2) | (-2, -1):
                    new_tail_position = previous_tail_position[0] - 1, previous_tail_position[1] - 1
                case (-1, 2) | (-2, 1):
                    new_tail_position = previous_tail_position[0] - 1, previous_tail_position[1] + 1
                case (1, -2) | (2, -1):
                    new_tail_position = previous_tail_position[0] + 1, previous_tail_position[1] - 1
                case _:
                    new_tail_position = (previous_tail_position[0] + tail_position_delta[0] // 2, previous_tail_position[1] + tail_position_delta[1] // 2)
            
        
        tail_positions.append(new_tail_position)
        position_index += 1
        previous_head_position = head_position
            
    return tail_positions

def is_tail_adjacent(head_position, tail_position):
    if abs(head_position[0]-tail_position[0]) <=1 and abs(head_position[1]-tail_position[1]) <= 1:
        return True
    else:
        return False
    
def ceildiv(a, b):
    return -(a // -b)
    
def get_visited_tail_positions(tail_positions):
    
    visited_tail_positions = {}
    
    for position in tail_positions:
        if position in visited_tail_positions:
            visited_tail_positions[position] += 1
        else:
            visited_tail_positions[position] = 1
        
    return visited_tail_positions



moves = get_moves("day9_input.txt")
# print(moves)

# part 1
head_positions = get_head_positions(moves)
# print(head_positions)
tail_positions = get_tail_positions(head_positions)
# print(tail_positions)
visited_tail_positions = get_visited_tail_positions(tail_positions)
# print(visited_tail_positions)
print("Part 1: " + str(len(visited_tail_positions)))


# part 2
positions_dict = {}
positions_dict["knot_0_positions"] = get_head_positions(moves)
for i in range (1,10):
    positions_dict["knot_{0}_positions".format(i)] = get_tail_positions(positions_dict["knot_{0}_positions".format(i-1)])
visited_knot_9_positions = get_visited_tail_positions(positions_dict["knot_9_positions"])

print("Part 2: " + str(len(visited_knot_9_positions)))

print('debug')
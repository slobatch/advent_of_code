import copy

"""
                    [Q]     [P] [P]
                [G] [V] [S] [Z] [F]
            [W] [V] [F] [Z] [W] [Q]
        [V] [T] [N] [J] [W] [B] [W]
    [Z] [L] [V] [B] [C] [R] [N] [M]
[C] [W] [R] [H] [H] [P] [T] [M] [B]
[Q] [Q] [M] [Z] [Z] [N] [G] [G] [J]
[B] [R] [B] [C] [D] [H] [D] [C] [N]
 1   2   3   4   5   6   7   8   9 
"""



def extract_moves_data(input_filename):
    list_of_moves = []
    with open(input_filename) as f:
        for line in f:
            move = [int(i) for i in line.split() if i.isdigit()]
            list_of_moves.append(move)
    return list_of_moves

crates = []
crates.append(['B','Q','C'])
crates.append(['R','Q','W','Z'])
crates.append(['B','M','R','L','V'])
crates.append(['C','Z','H','V','T','W'])
crates.append(['D','Z','H','B','N','V','G'])
crates.append(['H','N','P','C','J','F','V','Q'])
crates.append(['D','G','T','R','W','Z','S'])
crates.append(['C','G','M','N','B','W','Z','P'])
crates.append(['N','J','B','M','W','Q','F','P'])

def sort_crates(moves_input, input_crates):
    crates=copy.deepcopy(input_crates)
    for step in moves_input:
        quant = step[0]
        c_start = step[1]-1
        c_end = step[2]-1
        # print('quant:'+str(quant)+', from: '+str(c_start+1)+', to: '+str(c_end+1))
        # print_crates(crates)
        for i in range(quant):
            crane_crate = crates[c_start].pop()
            crates[c_end].append(crane_crate)
            # print_crates(crates)
    return crates

def sort_crates_new(moves_input, input_crates):
    crates=copy.deepcopy(input_crates)
    for step in moves_input:
        quant = step[0]
        c_start = step[1]-1
        c_end = step[2]-1
        print('quant:'+str(quant)+', from: '+str(c_start+1)+', to: '+str(c_end+1))
        print_crates(crates)
        crane_crate=[]
        for i in range(quant):
            crane_crate.append(crates[c_start].pop())
        crane_crate.reverse()
        crates[c_end].extend(crane_crate)
        print_crates(crates)
    return crates

def print_crates(crates):
    for crate_stack in crates:
        print(crates.index(crate_stack)+1, end=" | ")
        for crate in crate_stack:
            print(crate, end=" ")
        print("")
    print("")


list_of_moves = extract_moves_data('day5_input.txt')

#part 1
print_crates(sort_crates(list_of_moves, crates))

#part 2
print_crates(sort_crates_new(list_of_moves, crates))


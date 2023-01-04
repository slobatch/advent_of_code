def get_commands(input_file):
    
    commands = []
    
    with open(input_file) as file:
        
        for line in file:

            line = line.split()
            if len(line) == 1:
                command=line[0]
            else:
                command=(line[0],int(line[1]))
            
            commands.append(command)

    return commands

def calculate_signal_strengths(register_values):
    signal_strengths = {}
    X = 1
    cycle = 1
    
    for cycle in register_values:
        signal_strengths[cycle] = cycle * register_values[cycle]
                
    return signal_strengths

def generate_register_values(commands):
    register_values = {}
    X = 1
    cycle = 1
    
    for command in commands:
        match command:
            case 'noop':
                register_values[cycle] = X
                cycle += 1
            case ('addx', *val):
                register_values[cycle] = X
                cycle += 1
                register_values[cycle] = X
                cycle += 1
                X += val[0]
            case _:
                print("Invalid command")
        register_values[cycle] = X
                
    return register_values
                
def generate_screen(register_values):
    screen = []
    
    row = []
    x_pos = 0
    
    for cycle in register_values:
        
        sprite = (register_values[cycle] - 1, register_values[cycle], register_values[cycle]+1)
        
        if x_pos in sprite:
            row.append('#')
            x_pos += 1
        else:
            row.append('.')
            x_pos += 1
                
        if cycle % 40 == 0:
            screen.append(row)
            row = []
            x_pos = 0
            
    return screen

def print_screen(screen):
    for row in screen:
        for pixel in row:
            print(pixel, end="")
        print()
        

# part 1
command_list = get_commands("day10_input.txt")
# print(command_list)
register_values = generate_register_values(command_list)
# print(register_values)
signal_strengths = calculate_signal_strengths(register_values)
# print(signal_strengths)

print(signal_strengths[20]+signal_strengths[60]+signal_strengths[100]+signal_strengths[140]+signal_strengths[180]+signal_strengths[220])

# part 2
screen = generate_screen(register_values)
print_screen(screen)
def get_start_of_packet_marker(input_filename):
    last_four_chars=''
    position = 0
    with open(input_filename) as f:
        while 1:
            if len(last_four_chars) >=4:
                break
            
            char = f.read(1)
            if not char:
                break
            
            if last_four_chars.count(char) < 1:
                last_four_chars+=char
                position+=1
            elif last_four_chars.count(char) >= 1:
                last_four_chars = last_four_chars[last_four_chars.index(char)+1:]
                last_four_chars+=char
                position+=1

    return position


def get_start_of_message_marker(input_filename):
    last_four_chars=''
    position = 0
    with open(input_filename) as f:
        while 1:
            if len(last_four_chars) >=14:
                break
            
            char = f.read(1)
            if not char:
                break
            
            if last_four_chars.count(char) < 1:
                last_four_chars+=char
                position+=1
            elif last_four_chars.count(char) >= 1:
                last_four_chars = last_four_chars[last_four_chars.index(char)+1:]
                last_four_chars+=char
                position+=1

    return position

#part 1
print(get_start_of_packet_marker('day6_input.txt'))

#part 2
print(get_start_of_message_marker('day6_input.txt'))

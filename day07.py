def build_directory_tree(input_file):

    with open(input_file) as file:
        commands = file.readlines() 

    directories = {"/root":0}
    path = "/root"

    for command in commands:
        command = command.split()

        # commands starting with "$"
        if command[0] == "$":

            if command[1] == "ls":
                continue
            
            elif command[1] == "cd":

                if command[2] == "/":
                    path = "/root"   

                elif command[2] == "..":
                    path = path[0:path.rfind("/")]

                else:
                    directory_name = command[2]
                    path = path + "/" + directory_name
                    directories.update({path:0})

        elif command[0] == "dir":
            continue

        else:
            size = int(command[0])
            file_name = command[1]
            path = path + "/" + file_name + ".file"
            directories.update({path:size})
            
            directory = path[0:path.rfind("/")]
            # directory = path
            for i in range(path.count("/")-1):
                directories[directory]+=size
                directory = directory[0:directory.rfind("/")]

            path = path[0:path.rfind("/")]

            
    return directories

def calculate_total_size_up_to_threshold(directory_tree, threshold):
    total = 0

    for dir in directory_tree:
        if directory_tree[dir] <= threshold:
            total += directory_tree[dir]

    return total

def identify_deletion_candidate(directory_tree, total_size, os_size, free_space_required):

    candidate_tree = {key: value for key, value in directory_tree.items() if ((os_size - total_size + directory_tree[key]) >= free_space_required)}

    return min(candidate_tree.values())

#part 1
directories = build_directory_tree("day7_input.txt")            
directory_only_tree = {key: value for key, value in directories.items() if ".file" not in key}
total = calculate_total_size_up_to_threshold(directory_only_tree, 100000)
print(total)

#part 2
deletion_size = identify_deletion_candidate(directory_only_tree, directory_only_tree["/root"], 70000000, 30000000)
print(deletion_size)
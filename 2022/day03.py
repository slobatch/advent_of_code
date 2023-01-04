import os
import re

input = 'day3_input.txt'

def extract_data(input_filename):
    with open(input_filename) as f:
        lines = f.read()

    lines = lines.split('\n')
    return lines

def find_shared_item(input):
    h1, h2 = input[:len(input)//2], input[len(input)//2:]
    for i in h1:
        if h2.count(i) >= 1:
            return i

def list_shared_items(input):
    shared_items = []
    for i in input:
        shared_items.append(find_shared_item(i))
    return shared_items

def calculate_priority_sum(input_list):
    priority_sum = 0
    for i in input_list:
        if i.isupper():
            priority_sum+=(ord(i)-38)
        else:
            priority_sum+=(ord(i)-96)
    return priority_sum

def generate_grouped_lists(input):
    grouped_lists = []
    group_list = []
    for i in range(len(input)):
        if i != 0 and i%3 == 0:
            grouped_lists.append(group_list)
            group_list = []
        group_list.append(input[i])
    grouped_lists.append(group_list)
    return grouped_lists

def identify_badges(input):
    badges=[]
    for i in input:
        p1, p2, p3 = i[0], i[1], i[2]
        for j in p1:
            if p2.count(j) >= 1 and p3.count(j) >= 1:
                badges.append(j)
                break
    return badges

# part 1
print('part 1')
packs = extract_data(input)
print(packs)
shared_item_list = list_shared_items(packs)
print(shared_item_list)
print(calculate_priority_sum(shared_item_list))

#part 2
print('part 2')
grouped_packs = generate_grouped_lists(packs)
print(grouped_packs)
badges = identify_badges(grouped_packs)
print(badges)
print(calculate_priority_sum(badges))
import os
import re

input = 'day1_input.txt'

def extract_data(input_filename):
    list_of_lists = []
    with open(input_filename) as file:
        list = []
        for line in file:            
            if line != '\n':
                list.append(int(line))
            if line == '\n':
                list_of_lists.append(list)
                list = []
    return list_of_lists


def sum_each_list(list_of_lists):
    summed_list = []
    for list in list_of_lists:
        summed_list.append(sum(list))
    return summed_list


elf_calorie_inventory = extract_data(input)
summed_elf_calorie_inventory = sum_each_list(elf_calorie_inventory)
max_elf_calories = max(summed_elf_calorie_inventory)

print(max_elf_calories)


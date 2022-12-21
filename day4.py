def extract_data(input_filename):

    ror = []

    with open(input_filename) as f:
        for line in f:
            line = line.strip()
            r = line.split(',')
            for i in range(len(r)):
                r[i]=r[i].split('-')
                for j in range(len(r[i])):
                    r[i][j]=int(r[i][j])
            ror.append(r)
    return ror

def count_fully_overlapping_range_pairs(range_pair_list):
    fully_overlapping_pairs_count = 0
    for range_pair in range_pair_list:
        r1, r2 = range_pair[0], range_pair[1]
        if (
            (r1[0] >= r2[0] and r1[1] <= r2[1]) or
            (r2[0] >= r1[0] and r2[1] <= r1[1])
        ):
            fully_overlapping_pairs_count += 1
    return fully_overlapping_pairs_count

def count_overlapping_range_pairs(range_pair_list):
    overlapping_pairs_count = 0
    start = 0
    end = 1
    for range_pair in range_pair_list:
        r1, r2 = range_pair[0], range_pair[1]
        if (
            (r1[start] >= r2[start] and r1[end] <= r2[end]) or
            (r2[start] >= r1[start] and r2[end] <= r1[end]) or
            (r1[start] >= r2[start] and r1[start] <= r2[end]) or
            (r2[start] >= r1[start] and r2[start] <= r1[end])
        ):
            overlapping_pairs_count += 1
    return overlapping_pairs_count
            


print('part 1')
range_pair_list = extract_data('day4_input.txt')
print(len(range_pair_list))
print(count_fully_overlapping_range_pairs(range_pair_list))

print('part 2')
print(count_overlapping_range_pairs(range_pair_list))





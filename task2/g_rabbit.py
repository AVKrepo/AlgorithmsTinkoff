field_height, field_width = [int(x) for x in input().strip().split()]

prev_row = [int(x) for x in input().strip().split()]
absolute_max = max(prev_row)

for i in range(1, field_height):
    row = [int(x) for x in input().strip().split()]
    for j in range(1, field_width):
        if row[j] == 0:
            continue
        row[j] = min(prev_row[j - 1], prev_row[j], row[j - 1]) + 1
    curr_max = max(row)
    if curr_max > absolute_max:
        absolute_max = curr_max
    prev_row = row

print(absolute_max)

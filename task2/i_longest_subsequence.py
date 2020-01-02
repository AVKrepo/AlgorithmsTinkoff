values = [int(x) for x in input().strip().split()]


length = [1 for v in values]

for i in range(1, len(values)):
    value = values[i]
    possible_prev_lengths = [length[j] for j in range(i) if values[i] % values[j] == 0]
    length[i] = max(possible_prev_lengths, default=0) + 1
    
print(max(length))

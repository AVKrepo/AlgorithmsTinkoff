n = int(input())
heights = [int(x) for x in input().strip().split()]
max_difference = 9999

min_height = min(heights)
counter = [0 for _ in range(max_difference + 1)]
for height in heights:
    counter[height - min_height] += 1
sorted_heights = []
for diff in range(max_difference + 1):
    sorted_heights += [str(min_height + diff)] * counter[diff]
print(" ".join(sorted_heights))

board_length, max_jump = [int(x) for x in input().strip().split()]

number_of_ways = [1]
for i in range(1, board_length):
    possible_initial_points = [i - jump for jump in range(1, max_jump + 1) if i - jump >= 0]
    number_of_ways.append(sum([number_of_ways[initial_point] 
                               for initial_point in possible_initial_points]))


print(number_of_ways[-1])


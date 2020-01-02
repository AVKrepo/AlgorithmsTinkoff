board_height, board_width = [int(x) for x in input().strip().split()]

number_of_ways = [[0 for i in range(board_width)] for j in range(board_height)]
number_of_ways[0][0] = 1

for num_diagonal in range(1, (board_height - 1) + (board_width - 1) + 1):
    for i in range(0, num_diagonal + 1):
        j = num_diagonal - i
        if i >= board_height or j >= board_width:
            continue
        
        possible_initial_points = []
        if i - 1 >= 0 and j - 2 >= 0:
            possible_initial_points.append((i - 1, j - 2))
        if i - 2 >= 0 and j - 1 >= 0:
            possible_initial_points.append((i - 2, j - 1))
        if i + 1 < board_height and j - 2 >= 0:
            possible_initial_points.append((i + 1, j - 2))
        if i - 2 >= 0 and j + 1 < board_width:
            possible_initial_points.append((i - 2, j + 1))
        
        for possible_initial_point in possible_initial_points:
            x, y = possible_initial_point
            number_of_ways[i][j] += number_of_ways[x][y]
            
print(number_of_ways[-1][-1])


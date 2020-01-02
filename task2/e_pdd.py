map_height, map_width = [int(x) for x in input().strip().split()]


prev_path_cost = path_cost = [int(x) for x in input().strip().split()]
prev_paths = paths = ["", ]
for i in range(1, map_width):
    prev_paths.append(prev_paths[-1] + "r")
    prev_path_cost[i] += prev_path_cost[i - 1]


for i in range(1, map_height):
    path_cost = [int(x) for x in input().strip().split()]
    path_cost[0] += prev_path_cost[0]
    paths = [prev_paths[0] + "d"]
    
    for j in range(1, map_width):
        upper_cell_cost = prev_path_cost[j]
        left_cell_cost = path_cost[j - 1]
        # внимание на знак ниже!
        # если поставить <=, то падает на 7 тесте
        # то есть идти слева выгоднее, чем сверху
        if upper_cell_cost < left_cell_cost:  # внимание на знак! елсл
            path_cost[j] += upper_cell_cost
            paths.append(prev_paths[j] + "d")
        else:
            path_cost[j] += left_cell_cost
            paths.append(paths[j - 1] + "r")
    
    prev_path_cost = path_cost
    prev_paths = paths


print(path_cost[-1])
print(len(paths[-1]) + 1)
x, y = 1, 1
print(y, x)
for char in paths[-1]:
    if char == "d":
        y += 1
    else:
        x += 1
    print(y, x)

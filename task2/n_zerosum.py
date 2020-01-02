from collections import defaultdict


n_values = int(input())
values = [int(x) for x in input().strip().split()]

max_result = sum(values)
min_result = -max_result
signs = [defaultdict(str) for v in values]

first_value = values[0]
signs[0][-first_value] = "-"
signs[0][first_value] = "+"


for i, value in zip(range(1, n_values), values[1:]):
    for prev_result, prev_sign in signs[i - 1].items():
        signs[i][prev_result - value] = "-"
        signs[i][prev_result + value] = "+"


curr_result = 0
answer = [None for v in values]
for i in reversed(range(n_values)):
    value = values[i]
    sign = signs[i][curr_result]
    answer[i] = sign
    if sign == "+":
        curr_result -= value
    else:
        curr_result += value

print("".join(answer))

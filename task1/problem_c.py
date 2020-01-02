n, k = [int(x) for x in input().strip().split()]

stack = [n]
num_actions = 0
while len(stack) > 0:
    group = stack.pop()
    if group <= k:
        num_actions += 1
    else:
        first_subgroup = group // 2
        second_subgroup = group - first_subgroup
        stack += [first_subgroup, second_subgroup]

print(num_actions)

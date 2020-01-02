sequence = input().strip()

is_good_sequence = True
stack = []
close2open = {")": "(", "}": "{", "]": "["}

for bracket in sequence:
    if bracket in close2open.values():
        stack.append(bracket)
    elif bracket in close2open.keys():
        if len(stack) <= 0 or stack.pop() != close2open[bracket]:
            is_good_sequence = False
            break
    else:
        assert False, "Unknown type of bracket"

if len(stack) > 0:
    is_good_sequence = False

print("YES" if is_good_sequence else "NO")

n_values = int(input())
values = [int(x) for x in input().strip().split()]
max_amount = int(input())


amount2quantity = [0] + [float("inf") for i in range(max_amount)]
    
for amount in range(min(values), max_amount + 1):
    prev_amounts = [amount - v for v in values if amount - v >= 0]
    prev_quantities = [amount2quantity[a] for a in prev_amounts]
    amount2quantity[amount] = min(prev_quantities, default=float("inf")) + 1

curr_quantity = amount2quantity[max_amount]
if curr_quantity < float("inf"):
    print(curr_quantity)
    curr_amount = max_amount
    change = []
    while curr_quantity > 0:
        for value in reversed(values):
            prev_amount = curr_amount - value
            if prev_amount >= 0 and amount2quantity[prev_amount] == curr_quantity - 1:
                change.append(value)
                curr_quantity -= 1
                curr_amount -= value
                break
    print(" ".join([str(c) for c in change]))
    assert sum(change) == max_amount
else:
    print(-1)

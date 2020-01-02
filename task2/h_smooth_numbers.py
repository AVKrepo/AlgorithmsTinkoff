max_number_length = int(input().strip())

length2number = [-1, 9]  # pre-calculated values for length <= 1

# initial state is for length = 1
end2quantity = {i: 1 if i > 0 else 0 for i in range(10)}

for i in range(2, max_number_length + 1):
    next_end2quantity = {
        i: sum(end2quantity[j] if abs(i - j) <= 1 else 0 
               for j in range(0, 10)) 
        for i in range(0, 10)
    }
    end2quantity = next_end2quantity
    length2number.append(sum(end2quantity.values()))

print(length2number[max_number_length])

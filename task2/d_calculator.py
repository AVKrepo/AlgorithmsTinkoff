#
#   Примечание: данное решение не зашло (неправильный ответ на 2 тесте, хз почему)
#   Смотри решение на плюсах
#
max_number = int(input().strip())

number_of_operations = [0 for i in range(max_number + 1)]
previous_number = [-1 for i in range(max_number + 1)]

for i in range(2, max_number + 1):
    possible_previous_numbers = [i - 1]
    if i % 2 == 0:
        possible_previous_numbers.append(i // 2)
    if i % 3 == 0:
        possible_previous_numbers.append(i // 3)

    possible_previous_operations = [(number_of_operations[prev], prev) 
                                    for prev in possible_previous_numbers]
    n_operations, prev_number = min(possible_previous_operations)
    number_of_operations[i] = n_operations + 1
    previous_number[i] = prev_number

print(number_of_operations[max_number])

result_path = []
curr_number = max_number
while curr_number >= 0:
    result_path.append(curr_number)
    curr_number = previous_number[curr_number]
print(" ".join([str(x) for x in reversed(result_path)]))




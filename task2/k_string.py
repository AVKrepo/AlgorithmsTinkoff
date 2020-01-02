first_string = input().strip()
second_string = input().strip()

common_substr_len = [[0 for j in range(len(second_string) + 1)] 
                     for i in range(len(first_string) + 1)]
max_common_substr_len = 0
position = 0

for i in range(len(first_string)):
    for j in range(len(second_string)):
        if first_string[i] == second_string[j]:
            new_len = common_substr_len[i][j] + 1
            common_substr_len[i + 1][j + 1] = new_len
            if new_len > max_common_substr_len:
                max_common_substr_len = new_len
                position = i

answer = first_string[position - max_common_substr_len + 1:position + 1]
print(answer)

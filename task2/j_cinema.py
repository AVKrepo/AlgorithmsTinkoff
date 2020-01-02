#
#  Данное решение не зашло по времени, см. решение на плюсах (с такой же логикой)
#
from collections import defaultdict


films_counts = [int(x) for x in input().strip().split()]
films_sequences = []
for _ in range(len(films_counts)):
    films_sequences.append([int(x) for x in input().strip().split()])

common_subsequence_len = [[[0] * films_counts[2]] * films_counts[1]] * films_counts[0]
for i in range(films_counts[0]):
    for j in range(films_counts[1]):
        for k in range(films_counts[2]):
            if films_sequences[0][i] == films_sequences[1][j] == films_sequences[2][k]:
                if i == 0 or j == 0 or k == 0:
                    common_subsequence_len[i][j][k] = 1
                else:
                    common_subsequence_len[i][j][k] = common_subsequence_len[i - 1][j - 1][k - 1] + 1
            else:
                common_subsequence_len[i][j][k] = max(common_subsequence_len[i - 1][j][k], 
                                                      common_subsequence_len[i][j - 1][k], 
                                                      common_subsequence_len[i][j][k - 1])

print(common_subsequence_len[films_counts[0] - 1][films_counts[1] - 1][films_counts[2] - 1])

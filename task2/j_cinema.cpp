#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<size_t> films_counts(3);
    std::cin >> films_counts[0] >> films_counts[1] >> films_counts[2];

    std::vector<std::vector<int>> films_sequences;
    for (int i = 0; i < 3; ++i) {
        std::vector<int> sequence;
        int value;
        for (int j = 0; j < films_counts[i]; ++j) {
            std::cin >> value;
            sequence.push_back(value);
        }
        films_sequences.push_back(sequence);
    }

    std::vector<std::vector<std::vector<int>>> common_subsequence_len;
    for (int i = 0; i < films_counts[0]; ++i) {
        std::vector<std::vector<int>> matrix;
        for (int j = 0; j < films_counts[1]; ++j) {
            std::vector<int> vector;
            for (int k = 0; k < films_counts[2]; ++k) {
                vector.push_back(0);
            }
            matrix.push_back(vector);
        }
        common_subsequence_len.push_back(matrix);
    }

    for (int i = 0; i < films_counts[0]; ++i) {
        for (int j = 0; j < films_counts[1]; ++j) {
            std::vector<int> vector(films_counts[2]);
            for (int k = 0; k < films_counts[2]; ++k) {
                if (films_sequences[0][i] == films_sequences[1][j] &&
                    films_sequences[0][i] == films_sequences[2][k]) {
                    if (i == 0 || j == 0 || k == 0) {
                        common_subsequence_len[i][j][k] = 1;
                    } else {
                        common_subsequence_len[i][j][k] = common_subsequence_len[i - 1][j - 1][k - 1] + 1;
                    }
                } else {
                    int max_value = 0;
                    if (i > 0 && common_subsequence_len[i - 1][j][k] >= max_value) {
                        max_value = common_subsequence_len[i - 1][j][k];
                    }
                    if (j > 0 && common_subsequence_len[i][j - 1][k] >= max_value) {
                        max_value = common_subsequence_len[i][j - 1][k];
                    }
                    if (k > 0 && common_subsequence_len[i][j][k - 1] >= max_value) {
                        max_value = common_subsequence_len[i][j][k - 1];
                    }
                    common_subsequence_len[i][j][k] = max_value;
                }
            }
        }
    }

    std::cout << common_subsequence_len.back().back().back() << std::endl;

    return 0;
}
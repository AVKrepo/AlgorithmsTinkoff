#include <iostream>
#include <vector>
#include <string>

int main() {
    int max_number;
    std::cin >> max_number;
    std::vector<int> number2operations(max_number + 1);
    std::vector<int> number2prev_number(max_number + 1);
    number2operations[1] = 0;
    number2prev_number[1] = -1;

    for (int i = 2; i <= max_number; ++i) {
        int prev_number = i - 1;
        int prev_operations = number2operations[prev_number];
        if (i % 2 == 0 && number2operations[i / 2] < prev_operations) {
            prev_number = i / 2;
            prev_operations = number2operations[prev_number];
        }
        if (i % 3 == 0 && number2operations[i / 3] < prev_operations) {
            prev_number = i / 3;
            prev_operations = number2operations[prev_number];
        }
        number2operations[i] = prev_operations + 1;
        number2prev_number[i] = prev_number;
    }

    std::cout << number2operations[max_number] << std::endl;
    int curr_number = max_number;
    std::string path = "";
    while (curr_number > 0) {
        path = std::to_string(curr_number) + " " + path;
        curr_number = number2prev_number[curr_number];
    }
    std::cout << path << std::endl;

    return 0;
}
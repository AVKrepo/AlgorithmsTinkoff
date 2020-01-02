#include <iostream>
#include <vector>


struct Node {
    Node(int data_to_store) {
        data = data_to_store;
        next = nullptr;
    }

    int data;
    Node *next;
};

class Queue {
public:
    void push_back(int data) {
        Node *new_node = new Node(data);
        if (len == 0) {
            begin = end = new_node;
        } else {
            end->next = new_node;
            end = new_node;
        }
        len++;
        if (min_node == nullptr || data <= min) {
            min_node = new_node;
            min = data;
        }
    }

    void __find_min() {
        Node *node = begin;
        min = node->data;
        min_node = node;
        while (node->next != nullptr) {
            node = node->next;
            if (node->data <= min) {
                min = node->data;
                min_node = node;
            }
        }
    }

    int pop_first() {
        Node* node_to_return = begin;
        int data_to_return = node_to_return->data;
        if (len == 1) {
            begin = end = min_node = nullptr;
            min = 0;
        } else {
            begin = begin->next;
            if (node_to_return == min_node) {
                __find_min();
            }
        }
        len--;
        delete(node_to_return);
        return data_to_return;
    }

    int find_min() {
        return min;
    }

    ~Queue() {
        while (len > 0) {
            pop_first();
        }
    }
private:
    int len{0};
    Node *begin{nullptr};
    Node *end{nullptr};
    int min{0};
    Node *min_node{nullptr};
};


int main() {
    int n, k;
    std::cin >> n >> k;
    std::vector<int> sequence(n);
    int value;
    for (int i = 0; i < n; ++i) {
        std::cin >> value;
        sequence[i] = value;
    }

    Queue window = Queue();
    for (int i = 0; i < k; ++i) {
        window.push_back(sequence[i]);
    }
    std::cout << window.find_min() << std::endl;

    for (int i = k; i < n; ++i) {
        window.pop_first();
        window.push_back(sequence[i]);
        std::cout << window.find_min() << std::endl;
    }
    return 0;
}
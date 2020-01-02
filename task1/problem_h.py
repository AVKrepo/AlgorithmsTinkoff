#
# This solution doesn't reach good results, so look at the c++ implementation
#
n, k = [int(x) for x in input().strip().split()]
sequence = [int(x) for x in input().strip().split()]


class Queue:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.len = 0
        self.begin = self.end = None
        self.min = None
        self.last_min = None
        
    def push_back(self, data):
        new_node = self.Node(data)
        if self.len == 0:
            self.begin = self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node
        self.len += 1
        if self.last_min is None or data <= self.min:
            self.last_min = new_node
            self.min = data
            
    def __linear_find_min(self):
#         assert(self.len > 0)
        node = self.begin
        self.min = node.data
        self.last_min = self.begin
        while node.next is not None:
            node = node.next
            if node.data <= self.min:
                self.last_min = node
                self.min = node.data
            
    def pop_first(self):
#         assert(self.len > 0)
        node_to_return = self.begin
        if self.len == 1:
            self.begin = self.end = None
            self.last_min = self.min = None
        else:
            self.begin = self.begin.next
            if node_to_return == self.last_min:
                self.__linear_find_min()
        self.len -= 1
        return node_to_return.data
    
    def find_min(self):
        assert(self.len > 0)
        return self.min

    
window = Queue()
for i in range(k):
    window.push_back(sequence[i])
print(window.find_min())

for i in range(k, n):
    window.pop_first()
    window.push_back(sequence[i])
    print(window.find_min())

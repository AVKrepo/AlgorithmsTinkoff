class GoblinQueue:
    class Node:
        def __init__(self, number):
            self.number = number
            self.next = None
            self.prev = None
    
    def __init__(self):
        self.begin = self.middle = self.end = None
        self.len = 0
        
    def __add_to_empty(self, node):
        self.begin = node
        self.middle = node
        self.end = node
        self.len += 1
        
    def add_usual_goblin(self, node):
        if self.len == 0:
            self.__add_to_empty(node)
        else:
            self.end.next = node
            node.prev = self.end
            self.end = node
            if self.len % 2 == 0:
                self.middle = self.middle.next
            self.len += 1
        
    def add_vip_goblin(self, node):
        if self.len <= 1:
            self.add_usual_goblin(node)
        else:
            node.prev = self.middle
            node.next = self.middle.next
            self.middle.next = node
            node.next.prev = node
            if self.len % 2 == 0:
                self.middle = node
            self.len += 1
    
    def pop_goblin(self):
        assert(self.len > 0)
        goblin_to_go = self.begin
        if self.len == 1:
            self.begin = self.middle = self.end = None
        else:
            self.begin = self.begin.next
            if self.len % 2 == 0:
                self.middle = self.middle.next

        self.len -= 1
        return goblin_to_go


queue = GoblinQueue()
num_requests = int(input())
for _ in range(num_requests):
    request = input()
    if len(request) == 1:
        goblin_to_go = queue.pop_goblin()
        print(goblin_to_go.number)
    else:
        action, number = request.strip().split()
        new_goblin = queue.Node(number)
        if action == "+":
            queue.add_usual_goblin(new_goblin)
        else:
            queue.add_vip_goblin(new_goblin)

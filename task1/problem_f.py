num_clients = int(input())
coming_time = []
impatience = []
for i in range(num_clients):
    hours, minutes, imp = [int(x) for x in input().strip().split()]
    coming_time.append((hours, minutes))
    impatience.append((imp))


class Clocks:
    def __init__(self):
        self.time = (0, -1)
        
    def increment(self):
        minutes = self.time[1] + 1
        if minutes == 60:
            self.time = (self.time[0] + 1, 0)
        else:
            self.time = (self.time[0], minutes)


out_time = [None for i in range(num_clients)]
next_coming_client = 0
queue = []
working_time_remain = 0
current_sitting_client = None

clocks = Clocks()
while clocks.time < (24, 0):
    clocks.increment()
    
    if current_sitting_client is not None:
        working_time_remain -= 1
        if working_time_remain == 0:
            out_time[current_sitting_client] = clocks.time
            queue.pop(0)
            current_sitting_client = None

    if next_coming_client < num_clients and clocks.time == coming_time[next_coming_client]:
        if len(queue) > impatience[next_coming_client]:
            out_time[next_coming_client] = clocks.time
        else:
            queue.append(next_coming_client)
        next_coming_client += 1

    if current_sitting_client is None and len(queue) > 0:
        current_sitting_client = queue[0]
        working_time_remain = 20

for i in range(num_clients):
    hours, minutes = out_time[i]
    print(hours, minutes)

from collections import deque

# create queue
queue = deque()

# add elements
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# print contents
print(queue)

# taking the item from the front of the queue
x = queue.popleft()
print(x)
print(queue)

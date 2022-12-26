from collections import deque
queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print("큐 구조 : ", queue)
data = queue.popleft()
print("큐 구조 : ",queue)
print("큐에서 꺼낸 값 ",data)
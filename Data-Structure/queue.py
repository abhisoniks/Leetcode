#Enqueue: Add an element to the end of the queue
#Dequeue: Remove an element from the front of the queue
#IsEmpty: Check if the queue is empty
#IsFull: Check if the queue is full
#Peek: Get the value of the front of the queue without removing it


Class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def deque(self):
        del self.queue[0]    

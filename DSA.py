class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, data):
        self.queue.append(data)
        print("Data is enqueued to the Queue")
        
    def dequeue(self):
        if self.queue:
            self.queue.pop()
            print("Data is dequeued from the queue")
        else:
            print("Queue is empty")
            
            
    def display(self):
        print("Queue elements are:", self.queue)
        
a = Queue()

a.enqueue(3)
a.enqueue(2)
a.enqueue(5)
a.display()

a.dequeue()
a.display()
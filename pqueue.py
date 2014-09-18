import heapq

# This is a python priority queue.
class pqueue():
    
    # Initial creation. We use a min heap to track the highest priority.
    # Whenever we dequeue, we return the largest element.
    def __init__(self):
        self.heap = []

    # Put an item in the priority queue.
    def enqueue(self, item):
        heapq.heappush(self.heap, item)
    
    # Pop an item.
    def dequeue(self):
        return heapq.nlargest(1, self.heap)

    # Show items.
    def items(self):
        return self.heap

        

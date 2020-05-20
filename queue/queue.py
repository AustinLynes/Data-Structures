"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
   [ X ]
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
   [ ]
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# FIFO

from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        # self.storage = []
        # self.size = len(self.storage)
        self.storage = DoublyLinkedList()
        self.size = self.storage.length

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_head(value)
        # what if the queue is empty?
        # self.size += 1
        # if not self.size > 0:
        #      self.storage.insert(0, value)
        # else:
        #     self.storage.append(value)
        # what if the queue is NOT empty?

    def dequeue(self):

        # what if the queue is empty?
        if not self.size > 0:
            return
        else:
            # decrement the size
            self.size -= 1
            # remove the head
            value = self.storage.tail.value
            self.storage.remove_from_tail()
            return value
        # if not self.size > 0:
        #     return
        # else:
        #     self.size -= 1
        #     value = self.storage[0]
        #     self.storage.pop(0)
        #     return value

        # what if the queue is NOT empty?

"""

█─▄▄▄▄█─▄─▄─██▀▄─██─▄▄▄─█▄─█─▄█
█▄▄▄▄─███─████─▀─██─███▀██─▄▀██
▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀

A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

    ** LIFO **
        Last
        In
        First
        Out

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
   [X]

2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
   [X]

3. What is the difference between using an array vs. a linked list when
   implementing a Stack?

    using the array method for a storage i was able to use built in methods for
    appending to and popping from the array, while using my DLL i was able to
    use it built in methods and length to manipulate the stack.
    i realized this early on when i was psuedo-coding
    the push method ended up being comprised of the add_to_tail method and 
    adding to the total size of the stack.
    and the pop method just ended up being the remove_from_tail method
    that we had built in the DLL file saving the value like in the DLL 
    and returning it


"""
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        # self.storage = ?
        # self.storage = []
        self.storage = DoublyLinkedList()
        self.size = self.storage.length

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)
        # self.storage.append(value)

    def pop(self):
        # what if the stack is empty?
        if self.size > 0:
            self.size -= 1
            val = self.storage.tail.value
            self.storage.remove_from_tail()
            return val

        # what if the stack is NOT empty?
        # if len(self.storage) > 0:
        #     # the item we are looking at is the last item in the stack
        #     ind = len(self) - 1
        #     # save the value we are deleting so we can return it
        #     val = self.peek()
        #     # pop the last item
        #     self.storage.pop(ind)
        #     # return the item we deleted
        #     return val

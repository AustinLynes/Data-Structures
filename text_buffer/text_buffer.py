# what is a text buffer datastructure
# file I/O
# add to back, front, middle, anywhere
# delete to back, front, middle, anywhere
# join text buffers together


# array vs DLL
# -------------------

# ARRAY
# -------------------
#
# add to the back:
#                        O(1)
# add to front:
#                        O(n)
# delete from back:
#                        O(1)
# delete from front:
#                        O(n)
# join together:
#                        0(n)
#  __str__ :
#                        O(n)

# DLL (DOUBLY LINKED LIST)
# -------------------
#
# add to back:
#                        O(1)
#
# add to front:
#                        O(1)
#
# delete to back:
#                        O(1)
#
# delete to front:
#                        O(1)
#
# join together:
#                        O(1)
#  __str__ :
#                        O(n)

from doubly_linked_list import DoublyLinkedList


class TextBuffer:
    def __init__(self):
        self.storage = DoublyLinkedList()
        self.length = len(self.storage)

    def __str__(self):
        # while next.is not None
        current = self.storage.head
        _str = ""
        while current.next is not None:
            _str += current.value
            current = current.next
        return _str

    # add to end
    def append(self, _chars):
        for char in _chars:
            self.storage.add_to_tail(char)

    # add to front
    def prepent(self, _chars):
        for char in _chars:
            self.storage.add_to_head(char)

    # delete from front
    def delete_from_front(self, remove):
        for _ in range(remove):
            self.storage.remove_from_head()

    # delete from back
    def delete_from_back(self, remove):
        for _ in range(remove):
            self.storage.remove_from_tail()

    def join(self, buffer):
        # buffer a tail is now buffer b head
        self.storage.tail.next = buffer.storage.head
        buffer.storage.head.prev = self.storage.tail

        # point our tail to new tail
        self.storage.tail = buffer.storage.tail
    def find_text(self, text):
        pass

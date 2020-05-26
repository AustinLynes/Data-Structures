from doubly_linked_list import DoublyLinkedList, ListNode
"""

    Normal Double Linked Listed
    ----------------------------------------------
     node a     node b       node c     node d
    |------|   |------|     |------|    |------|
        <--------    <--------   <--------
        a --------> b  --------> c --------> d  -----> NONE
    |------|   |------|     |------|    |------|


    Least Recently Used  Cache
    ----------------------------------------------
     added order A -> B -> C -> D
     node d     node c       node b     node a
    |------|   |------|     |------|    |------|
        <--------    <--------   <--------
        d --------> c  --------> b --------> a  -----> NONE
    |------|   |------|     |------|    |------|

    ----------------------------------------------



    GET
    -------------------------------------------

    # needs to be moved to the <--- of the DLL because this value is the most recently used
    # MOST RECENTLY USED
    # say i have 7 cards sitting in front of me
    #
    # and i was allowed to pick up only 1 card but if i did i HAD to put it at the left

    # [A]->[2]->[3]->[4]->[5]->[6]->[7]->None

    # say i pic up the [4] card

    # when i put it down it the cards will now look like this
    # [4]->[A]->[2]->[3]->[5]->[6]->[7]->None

    # to do this

    # [3]->[5]
    #   :: [3] which is [4]s previous needs to now point to [5]

    # [4]<-[A]
    #  :: [4] next node needs to be [A]

    # <-[4]
    #  :: [4]s previous needs to be empty

    # [4]->[A]
    #  :: [4]s next needs to point at [A] (old head)

    # tell the list [4] is new head

    # what if the dict is empty?


    SET
    -------------------------------------------
       # add to the cache --> LRU
        # set the dll
        # update the size, if the size is greater than our limit.
        # remove the least recently used entry and add this one to the end
        # if the key is present, just overwite the value, and move this to the end ---> MRU

        # what if the cache is empty
        # we can go ahead and just add this node to the cache as is.
        # this node would be the head, tail, MRU and LRU all at the same time

        # the cache is not empty
        # what if the cache is NOT at its limit

        # what if the cache is at it limit?

    """

# debugging
END = "\033[1;31;0m"
RED = "\033[1;31;40m"
GRN = "\033[1;32;40m"
WHT = "\033[1;29;1m"


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.dll = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        print('GET ->', self.size)

        # if the current size is greater than 0
        if self.size > 0:
            # create a walker
            current_node = self.dll.head
            # the node we are looking for
            found_node = None
            # walk forward while the next node is not empty
            while current_node.next is not None:
                # take a step forward
                current_node = current_node.next
                # look at the key inside the current nodes value {key, value}
                for (_key, _value) in current_node.value.items():
                    # if the key matches the key we are looking for we found a match

                    if _key == key:
                        # add the current_node to the found list
                        found_node = current_node
                        self.dll.move_to_front(found_node)
                        return _value
                # print(current_node.value)
            print('\n')
            # # if we have found a node
            # if found_node is not None:
            #     v = ""

            #     for (key, value) in found_node.value.items():
            #         v = value

            #     (found_node)
            #     return v
        # if the size is zero then return None
        else:
            print('something wrong')
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):

        entry = {}
        entry[key] = value

        # print(entry)
        if self.size > self.limit:
            return
        elif self.size == self.limit:
            print(f"{RED}cache overload{END}")

            # print(self.storage[key])

            # print(f'keys==>{keys}')
            # self.add_entry(key, value)
            # set the storage to this value
            # add an item to the linked list as the MRU
            # self.storage[key] = value

            # print(self.storage[key])
            self.dll.add_to_head(entry)
            if key not in self.storage:
                self.storage[key] = value
                self.dll.remove_from_tail()

            # if self.size > 1:
            #     self.size -= 1
            # self.add_entry(key, value)
            # if self.dll.head is not self.dll.tail and self.dll.tail is not None:
            # we have hit our limit
            # the LRU entry needs to be removed
            # this entry needs to be set as the MRU y
        else:
            self.dll.add_to_head(entry)
            self.storage[key] = value
            self.size += 1
            print('adding')



            # print(current.value)
        # this entry needs to be added as the MRU entry
        # increment the size upward upon a successful add to the Cache
        # self.add_entry(key, value)

        # create the entry with key : value pair


# cache = LRUCache(3)
# # add 3 items
# print(f'{GRN}adding items 1{END}\n')
# cache.set('item1', 'a')
# print(f'{GRN}adding items 2{END}\n')
# cache.set('item2', 'b')
# print(f'{GRN}adding items 3{END}\n')
# cache.set('item3', 'c')
# print(f'{GRN}adding items 4{END}\n')
# cache.set('item4', 'd')

# # get one
# print(f'{GRN}checking items 1{END}\n')
# print(cache.get('item1') == "a")
# print(f'{GRN}checking order{END}\n')
# cur = cache.dll.head

# while cur is not None:
#     print(cur.value)
#     cur = cur.next

# print(f'{GRN}checking items 2{END}\n')
# print(cache.get('item2') == "b")

# print(f'{GRN}checking order{END}\n')
# cur = cache.dll.head
# while cur is not None:
#     print(cur.value)
#     cur = cur.next

# print(f'{GRN}checking items 3{END}\n')
# print(cache.get('item3') == "c")


# print(f'{GRN}checking order{END}\n')
# cur = cache.dll.head
# while cur is not None:
#     print(cur.value)
#     cur = cur.next

# print(f'{GRN}adding a duplicate item2 order{END}\n')
# cache.set('item2', 'z')

# print(f'{GRN}checking order{END}\n')
# cur = cache.dll.head
# while cur is not None:
#     print(cur.value)
#     cur = cur.next

# print(f"{GRN}Final Dict {END}\n")
# print(cache.storage)

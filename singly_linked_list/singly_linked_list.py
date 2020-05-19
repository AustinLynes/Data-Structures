"""


███████████████████████████████████████████████████████████████████
█▄─▄███▄─▄█▄─▀█▄─▄█▄─█─▄█▄─▄▄─█▄─▄▄▀███▄─▄███▄─▄█─▄▄▄▄█─▄─▄─█─▄▄▄▄█
██─██▀██─███─█▄▀─███─▄▀███─▄█▀██─██─████─██▀██─██▄▄▄▄─███─███▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▀▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀

Nodes :
    value:
        get
    next:
        get

Linked List
    head:
    Tail:

#########################################################
########################################################

    EXAMPLE --------------------------------------------
        A {
            value : 0
            next_node : B
        }
        B {
            value : 1,
            next_node : C
        }
        C {
            value : 2
            next_node: None
        }
    -----------------------------------------------------
    List == [ 0, 1, 2, ]
#############################################################
#############################################################
 """


class Node:
    # initialize with a value and the next node
    def __init__(self, value=None, next_node=None):
        # the value of this node
        self.value = value
        # the value of the next node in the list
        self.next_node = next_node

    # get this nodes value
    def get_value(self): # o(1)
        return self.value

    # get the next node in the list
    def get_next(self): # o(1)
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def __str__(self):
        return "{:}".format(self.get_value())


class LinkedList:
    def __init__(self):
        # first node in the list
        self.head = None
        # last node in the list
        self.tail = None

    # add to the end of the list
    # if the list is empty then the head needs to be set to the tail
    # if the list is not empty then the head becomes the last number in
    # the list

    def add_to_tail(self, val):
        # what if the list is empty?
        # create a new node so we can use it later
        new_node = Node(val)
        # if there isnt a head then the list is empty
        if not self.head:
            self.head = new_node
            self.tail = self.head
        # what if the list isn't empty?
        else:
            # start at the head
            current = self.head
            # as long as we haven't reached the end of the list keep updating
            # by traversing the linked list we get the end of the list..
            while current.get_next() is not None:
                current = current.get_next()

            #  [A, B, C, D ,E,NONE]
            # current will be the last node.
            # so we can add to it
            current.set_next(new_node)
            self.tail = current.get_next()
            # self.tail = current

    def set_head(self, new_node):
        self.head = new_node

    # list contains a value
    # node a == value
    # node b == value
    def contains(self, value):
        # to see if the list contains a certian value
        # we need to start at the head and look til the end
        # if any of our values match. then we return true

        val = False
        # what if the list is empty?
        if not self.head:
            val = False
        # what if the list isn't empty?
        else:
            current = self.head
            # while the current nodes next node does not equal None
            while current.get_next() is not None:
                # the current node is now the next node in the list
                # if the current nodes value is the value we are looking for the set the
                current = current.get_next()
                # watch value to true
                if current.get_value() == value:
                    val = True


        # return our watcher value
        return val

    def remove_head(self):
        # what if the list is empty
        if not self.head:
            return None
        else:
            # what if the list isn't empty
            val = self.head.get_value()
            self.head = self.head.get_next()
            self.tail = None
            return val

    def get_max(self):
        # start at the head..
        # what if the list is empty?
        if not self.head:
            return None
        else:
            current = self.head
            high = current.get_value()
            # what if the list isn't empty?
            # look through all the nodes
            while current.get_next() is not None:
                # update the current node
                current = current.get_next()
                print(current.get_value())
                # if the current node we are looking at contains a value greater than
                # our saved high value the set the high value to the HIGHER current value
                if current.get_value() > high:
                    high = current.get_value()

            # return the highest value found
            return high



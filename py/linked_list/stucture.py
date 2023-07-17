# Basic implementation of linked list

class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self, head=None):
        self.head = head


    def count(self, head):
        current = head
        element_count = 0

        while current is not None:
            element_count += 1
            current = current.next

        return element_count


    def print_list(self):
        current = self.head

        while current is not None:
            print(f"{current.value}")
            current = current.next


    def append(self, value):
        current = self.head
        node = Node(value)

        if current is None:
            self.head = node
        else:
            while current.next != None:
                current = current.next
            current.next = node


    def prepend(self, value):
        current = self.head
        node = Node(value)

        self.head = node
        node.next = current


    def insert(self, value, index):
        pass


    def pop(self, index = 0):
        pass


    def pop_start(self):
        pass


    def update(self, value, index):
        pass


    def search(self, value):
        pass


    def merge(self, head1, head2):
        pass



newlist = LinkedList()

newlist.append(11)
newlist.append(22)
newlist.append(55)
newlist.prepend(33)
newlist.prepend(44)

newlist.print_list()
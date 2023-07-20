# Basic implementation of linked list

class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self, head=None):
        self.head = head


    def count(self):
        current = self.head
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

        return self.head


    def append(self, value):
        current = self.head
        node = Node(value)

        if current is None:
            self.head = node
        else:
            while current.next != None:
                current = current.next
            current.next = node

        return self.head


    def prepend(self, value):
        current = self.head
        node = Node(value)

        self.head = node
        node.next = current

        return self.head


    def insert(self, value, idx):
        current = self.head
        node = Node(value)
        counter = 1

        if current is None:
            self.head = node
        else:
            while current != None:
                if counter == idx:
                    node.next = current.next
                    current.next = node
                    break

                counter += 1
                current = current.next

        return self.head


    def pop(self, index=0):
        pass


    def pop_start(self):
        pass


    def update(self, value, idx):
        current = self.head
        counter = 0

        while current != None:
            if counter == idx:
                current.value = value
                break

            counter += 1
            current = current.next

        return self.head


    def search(self, value):
        current = self.head
        counter = 0

        while current != None:
            if current.value == value:
                return counter

            counter += 1
            current = current.next

        return -1



    def merge(self, head1, head2):
        pass



newlist = LinkedList()

newlist.append(44)
newlist.append(33)
newlist.prepend(22)
newlist.prepend(11)
newlist.prepend(0)
newlist.update(222, 5)
# newlist.insert(11, 4)

newlist.print_list()

print("search", newlist.search(222))
print("count", newlist.count())
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'<{self.data}>'


class TermCls:
    def __init__(self, coefficient, power):
        self.coefficient = coefficient
        self.power = power
        self.next = None

    def __str__(self):
        return f'{self.coefficient}x**{self.power}'


class LinkedListCls:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def traversal(self):
        current = self.head
        while current:
            print(current)
            current = current.next

    def add_to_head(self, node):
        if self.tail is None:
            self.tail = node
        node.next = self.head
        self.head = node
        self.length += 1

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1

    def search(self, target):
        current = self.head
        while current:
            if target == current.data:
                return current
            current = current.next
        return None

    def get_item_index(self, i):
        current = self.head
        j = 0
        while current and j < i:
            j += 1
            current = current.next
        return current

    def get_length(self):
        current = self.head
        i = 0
        while current:
            i += 1
            current = current.next
        return i

    def remove_to_head(self):
        if self.get_length() == 0:
            return
        elif self.get_length() == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            self.head = self.head.next
            self.length -= 1

    def pop(self):
        if self.get_length() == 0:
            return
        elif self.get_length() == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return
        else:
            prev = None
            current = self.head
            while current.next:
                prev = current
                current = current.next
            prev.next = None
            self.tail = prev
            self.length -= 1

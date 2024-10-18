from src.linked_list_node import LinkedListNode


class DoublyLinkedList:
    def __init__(self):
        self._head: LinkedListNode = None
        self._tail: LinkedListNode = None
        self._count = 0

    @property
    def count(self):
        count = 0
        current = self._head

        while current is not None:
            current = current.next
            count += 1

        return count

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def add_first(self, value):
        new_node = LinkedListNode(value)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self._count += 1

    def add_last(self, value):
        new_node = LinkedListNode(value)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._count += 1

    def insert_after(self, node, value):
        new_node = LinkedListNode(value)
        if node is None:
            raise ValueError("Given node is not found.")

        new_node.next = node.next
        new_node.prev = node

        if node.next is not None:
            node.next.prev = new_node
        node.next = new_node

        if node == self._tail:
            self._tail = new_node  # Update tail if inserted at the end

        self._count += 1

        print(f"New node inserted. List count: {self._count}")
        print(f"List values after insert: {self.values()}")

    def insert_before(self, node, value):
        new_node = LinkedListNode(value)

        if node is None:
            raise ValueError('Node does not exist')

        new_node.prev = node.prev
        new_node.next = node

        if node.prev is not None:
            node.prev.next = new_node

        node.prev = new_node

        if node == self._head:
            self._head = new_node

        self._count += 1

    def remove_first(self):
        if self._head is None:
            raise ValueError('List is empty!')

        value = self._head.value

        if self._head == self._tail:  # If there's only one node
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None

        self._count -= 1
        return value

    def remove_last(self):
        if self._head is None:
            raise ValueError('Empty')

        value = self._tail.value
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            self._tail = self._tail.prev
            self.tail.next = None

        self._count -= 1

        return value

    def find(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return current
            current = current.next
            
        if current is None:
            return None

        raise ValueError("Value not found in the list")

    def values(self):
        current = self.head
        values = []
        if self.head is None:
            return tuple(values)

        while current is not None:
            values.append(current.value)
            current = current.next

        return tuple(values)

    def _insert_before_head(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def _insert_after_tail(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node

        new_node.prev = self.tail
        self.tail = new_node


node = DoublyLinkedList()
# node.add_first(2)
# node.add_last(4)
# node_to_insert_after = node.find(2)
# node.insert_after(node_to_insert_after, 3)
# node.remove_first()
# node.remove_last()
# print(node.count)
print(node.values())

from LinkedListNode import LinkedListNode
from OutOfBoundsException import OutOfBoundsException

class LinkedList(object):
    def __init__(self):
        """
        Construtor de lista ligada. A lista sempre começa vazia
        """
        self._head = None  # Apontador para o nó cabeça (primeiro)
        self._tail = None  # Apontador para o nó filho (ultimo)
        self._len = 0  # contador

    def __len__(self):
        return self._len

    @property
    def head(self):
        return self._head.value if self._head is not None else None

    @property
    def tail(self):
        return self._tail.value if self._tail is not None else None

    def append(self, value):

        if self._len == 0:
            self._head = LinkedListNode(value)
            self._tail = self._head
        else:
            self._tail.next = LinkedListNode(value)
            self._tail = self._tail.next
        self._len += 1

    def insert(self, value):

        if self._len == 0:
            self._head = LinkedListNode(value)
            self._tail = self._head
        else:
            node = LinkedListNode(value,self._head)
            self._head = node
        self._len += 1

    def removeFirst(self):

        value = self._head.value
        self._head = self._head.next
        self._len -= 1
        return value

    def getValueAt(self, index):
        if index > self._len:
            raise OutOfBoundsException
        node = self._head
        for i in range(self._len):
            if i == index:
                return node.value()
            node = node.next()
        
    def toList(self):
        if self._len == 0:
            return []
        node = self._head
        list = [self._head.value]
        while node.hasNext():
            node = node.next
            list.append(node.value)
        return list
        
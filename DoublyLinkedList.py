class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedist:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.value)
            curr = curr.next

    def append(self, value):
        '''adds a node at the end of the linked list'''
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        '''remove a node from the end of the linked list'''
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -=1
        return temp

    def prepend(self, value):
        '''adds a node to the beginning of the linked list'''
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True


doubly_linked_list = DoublyLinkedist(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)
doubly_linked_list.append(4)
doubly_linked_list.print_list()
print('\n')
print(doubly_linked_list.pop())
print(doubly_linked_list.pop())
print(doubly_linked_list.pop())
print(doubly_linked_list.pop())
doubly_linked_list.prepend(8)
print('\n')
doubly_linked_list.print_list()
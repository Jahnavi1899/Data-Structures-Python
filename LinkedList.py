class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.value)
            curr_node = curr_node.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None: # or self.length == 0
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0: # when the linked list is empty
            return None
        prev, temp = self.head, self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0: # when the linked list has only 1 node
            self.head, self.tail = None, None
        return temp.value #return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head, self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_front(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value #return temp
    
    def get(self, index): # return the node at the given index
        if index < 0 or index >= self.length:
            return None
        count = 0
        temp = self.head
        while count != index:
            temp = temp.next
            count += 1
        return temp
        




    # def insert(self, index, value):
linked_list = LinkedList(2)
linked_list.append(4)
linked_list.print_list()
linked_list.pop_front()
linked_list.print_list()

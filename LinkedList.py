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
        '''Prints all the node values in the linked list'''
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.value)
            curr_node = curr_node.next

    def append(self, value):
        '''Adds a node at the end of the linked list'''
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
        '''Removes the node at the end of the linked list'''
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
        return temp #return temp.value

    def prepend(self, value):
        '''Adds a node at the beginning of the linked list'''
        new_node = Node(value)
        if self.length == 0:
            self.head, self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_front(self):
        '''Removes the first element of the linked list'''
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp #return temp.value
    
    def get(self, index): 
        '''return the node at the given index'''
        if index < 0 or index >= self.length:
            return None
        # count = 0
        temp = self.head
        # while count != index:
        #     temp = temp.next
        #     count += 1
        for _ in range(index):
            temp = temp.next
        return temp #temp.value
        
    def set_value(self, index, value):
        '''set the value at the given index'''
        # approach 1
        # if index < 0 or index >= self.length:
        #     return None
        # temp = self.head
        # for _ in range(index):
        #     temp = temp.next
        # temp.value = value
        # return temp.value #return temp.value
        # aproach 2
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        '''insert a node at the given position'''
        if index < 0 and index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp = self.get(index-1)
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        '''remove the node at the given index'''
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_front()
        if index == self.length-1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next # because self.get method is O(n)
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        '''reverses the linked list'''
        temp = self.head
        self.head = self.tail
        self.tail = temp
        prev = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = prev
            prev = temp
            temp = after
        
        
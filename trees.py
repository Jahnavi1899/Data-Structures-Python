class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# tree traversal techniques
# DFS - preorder, inorder, postorder

# preorder traversal - (root, left, right)
def preorder_recursive(tree_node):
    '''time complexity : O(N)
       space complexity : O(H) where H is the height of the tree
    '''
    if tree_node:
        print(tree_node.val)
        preorder_recursive(tree_node.left)
        preorder_recursive(tree_node.right)

#preorder(root)
    
# inorder traversal - (left, root, right)
def inorder_recursive(tree_node):
    '''time complexity : O(N)
       space complexity : O(H) where H is the height of the tree
    '''
    if tree_node:
        inorder_recursive(tree_node.left)
        print(tree_node.val)
        inorder_recursive(tree_node.right)

#inorder(root)

# postorder traversal - (left, right, root)
def postorder_recursive(tree_node):
    '''time complexity : O(N)
       space complexity : O(H) where H is the height of the tree
    '''
    if tree_node:
        postorder_recursive(tree_node.left)
        postorder_recursive(tree_node.right)
        print(tree_node.val)
    
#postorder(root) 
        
def preorder_iterative(tree_node):
    '''
        Time complexity : O(N)
        Space complexity : O(N)
    '''
    stack = []
    if tree_node:
        stack.append(tree_node)
        while len(stack) > 0:
            node = stack.pop()
            print(node.val)
            
            if node.right is not None:
                stack.append(node.right)
            
            if node.left is not None:
                stack.append(node.left)

#preorder_iterative(root)

def inorder_iterative(tree_node):
    stack = []
    inorder_traversal = []

    node = tree_node
    while True:
        if node:
            stack.append(node)
            node = node.left
        else:
            if len(stack) == 0:
                break
            node = stack.pop()
            inorder_traversal.append(node.val)
            node = node.right

    return inorder_traversal

#print(inorder_iterative(root))

def postorder_iterative(tree_node):
    stack1 = []
    stack2 = []
    postorder_traversal = []
    root = tree_node
    if root is None:
        return postorder_traversal
    
    stack1.append(root)
    while len(stack1) > 0:
        root = stack1.pop()
        stack2.append(root)
        if root.left is not None:
            stack1.append(root.left)
        if root.right is not None:
            stack1.append(root.right)
    
    while len(stack2) > 0:
        postorder_traversal.append(stack2.pop().val)
    
    return postorder_traversal

print(postorder_iterative(root))

# BFS traversal - level wise tree traversal
# queue implementation
def BFS(tree_node):
    '''time complexity : O(N)
       space complexity : O(N)
    '''
    if tree_node:
        queue = []
        queue.append(tree_node)

        while len(queue) > 0:
            node = queue[0]
            print(node.val, end=" ")

            queue.pop(0)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

#BFS(root)
from slist import Queue, Stack
import random


class Node:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.paths = []
    

    def random_insert(self, top, node): #Randomize construction of a tree
        if top is None:
            return node
        if random.random() < 0.5:
            top.left = self.random_insert(top.left, node)
        else:
            top.right = self.random_insert(top.right, node)
        return top
 

    def traverse_queue(self, top):
        nodes_visited = []
        if top is None:
            return
        queue = Queue()
        queue.add(top)
        while not queue.is_empty:
            node = queue.pop()
            nodes_visited.append(node.data)
            if node.left:
                queue.add(node.left)
            if node.right:
                queue.add(node.right)
        return nodes_visited

    
    def traverse_stack(self, top):
        nodes_visited = []
        if top is None:
            return
        stack = Stack()
        stack.push(top)
        while not stack.is_empty:
            node = stack.pop()
            nodes_visited.append(node.data)
            if node.right:
                stack.push(node.right)
            if node.left:
                stack.push(node.left)

        return nodes_visited


    def btree_print(self, top, level=0):
        if top is None:
            return 
        self.btree_print(top.right, level+1)
        print("{}* {}".format('   '*level, top.data))
        self.btree_print(top.left, level+1)

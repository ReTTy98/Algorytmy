from btree import Node


root = Node(0)
for i in range(7):
    root.random_insert(root, Node(i+1))


print("=========================================================")
print("Printing tree")
print("=========================================================")
root.btree_print(root) 
print("=========================================================")

print("Printing all visited nodes with BFS")
print(root.traverse_queue(root))

print("=========================================================")

print("Printing all visited nodes with DFS")
print(root.traverse_stack(root))

print("=========================================================")





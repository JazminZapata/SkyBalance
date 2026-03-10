from node import Node
from bst import BST
from loader import loadTree

# crear árbol
tree = BST()
tree2 = BST()


loadTree(tree2, "Backend/json/ModoInserción.json")
print("LOADING TREES . . .")
print(tree2.root.getValue().codigo)
print(tree2.root.getLeftChild().getValue().codigo)
print(tree2.root.getRightChild().getValue().codigo)




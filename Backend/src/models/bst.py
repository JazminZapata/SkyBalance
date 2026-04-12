from models.tree import Tree

class BST(Tree):

    def __init__(self):
        super().__init__()

    def insert(self, node):
        # Verify if the tree is empty, if it is, the new node becomes the root
        if self.root is None:
            self.root = node
        else:
            self.__insert(self.root, node)

    # Recursive method for inserting a node when the tree has a root
    def __insert(self, currentRoot, node):
        if node.getValue().getCodigoComp() == currentRoot.getValue().getCodigoComp():
            print(f"El valor del nodo {node.getValue()} ya existe en el árbol.")
        else:
            # verify if the value to insert is greater than the current root (code)
            if node.getValue().getCodigoComp() > currentRoot.getValue().getCodigoComp():
                # verify if there is a right child
                if currentRoot.getRightChild() is None:
                    # if it doesn't have a right child, assign the node as the right child
                    currentRoot.setRightChild(node)
                    # and the new node will have the current root as its parent
                    node.setParent(currentRoot)
                else:
                    # it already has a right child, so we need to process the insertion from the right child
                    # by making a recursive call with that child
                    self.__insert(currentRoot.getRightChild(), node)
            else:
                # the value of the node to insert is less than the value of the current root
                # verify if it has a left child
                if currentRoot.getLeftChild() is None:
                    # if it doesn't have a left child, assign the node as the left child
                    currentRoot.setLeftChild(node)
                    # and the new node will have the current root as its parent
                    node.setParent(currentRoot)
                else:
                    # it already has a left child, so we need to process the insertion from the left child
                    # by making a recursive call with that child
                    self.__insert(currentRoot.getLeftChild(), node)

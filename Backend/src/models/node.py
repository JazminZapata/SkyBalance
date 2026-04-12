# clase que permite instanciar nuevos nodos con sus atributo
class Node:

    # Constructor of the Node class, which initializes the node with a flight object and sets the left and right children to None
    # We define the attributes (balaceFactor, finalPrice and height as specific attributes of the node)

    def __init__(self, flight):
        self.value = flight
        self.parent = None
        self.leftChild = None
        self.rightChild = None
        self.balanceFactor = None
        self.height = None
        self.finalPrice = None
        self.isCritical = False  # NodoCritico

    # Getters and setters for the node's attributes
    def setRightChild(self, node):
        self.rightChild = node

    def getRightChild(self):
        return self.rightChild

    def setLeftChild(self, node):
        self.leftChild = node

    def getLeftChild(self):
        return self.leftChild

    def setParent(self, node):
        self.parent = node

    def getParent(self):
        return self.parent

    def getValue(self):
        return self.value

    def setBalanceFactor(self, balanceFactor):
        self.balanceFactor = balanceFactor
    
    def getBalanceFactor(self):
        return self.balanceFactor
    
    def setHeight(self, height):
        self.height = height
        
    def getHeight(self):
        return self.height
    
    def setFinalPrice(self, finalPrice):
        self.finalPrice = finalPrice
        
    def getFinalPrice(self, tree=None):
        # Always return the cached finalPrice calculated by recalculatePrices
        if self.finalPrice is not None:
            return self.finalPrice
        # Fallback if no price has been calculated yet
        return self.getValue().getPrecioBase()

    def setIsCritical(self, value: bool):
        # Sets whether this node is flagged as critical due to exceeding depth limit
        self.isCritical = value

    def getIsCritical(self):
        # Returns True if this node exceeds the tree's depth limit
        return self.isCritical
        

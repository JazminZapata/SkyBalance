#This import is the properly python.
import copy


class actionHistory:
    
    
    # Constructor
    def __init__(self):
        self.stack = []
        
        
    # Add an action to the stack. Add before insert, edit or cancel an action
    def save(self, tree):
        # deep.copy create a only copy the object with everything, not only the reference or value because it's can change
        capture = copy.deepcopy(tree)
        self.stack.append(capture)
        
        
    # Clt+y
    def undo(self, tree):
        if len(self.stack) == 0:
            print("No actions to undo")
            return
        previousTree = self.stack.pop()
        tree.root = previousTree.root
    
    
        
    
    
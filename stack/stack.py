class Stack:
    def __init__(self):
        self.container = list() # ADT Object (Representation) : Dynamic Array
    
    def empty(self): # ADT Operation 1. empty()
        if not self.container:
            return True
        else:
            return False
    
    def push(self, data): # ADT Operation 2. push()
        self.container.append(data)
    
    def pop(self): # ADT Operation 3. pop()
        if self.empty():
            return None
        else:
            return self.container.pop()
            

    def peek(self): # ADT Operation 4. peek()
        if self.empty():
            return None
        else:
            return self.container[-1]
        
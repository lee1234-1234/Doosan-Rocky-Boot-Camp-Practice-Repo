class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return -1
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        return -1
    
    def status_stack(self):
        return self.stack
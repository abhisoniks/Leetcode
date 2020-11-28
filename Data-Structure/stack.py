# Creating a stack
class stack:
    def __init__(self):
        self.stack = []

    # Adding items into the stack
    def push(self, item):
        self.stack.append(item)
        print("pushed item: " + item)

    # Removing an element from the stack
    def pop(self):
        if (self.check_empty()):
            return "stack is empty"
        return self.stack.pop()

    def check_empty(self):
        return True if len(self.stack)==0 else return False

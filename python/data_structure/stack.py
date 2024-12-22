class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self, item):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty, no top element to peek."

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return self.stack[-1]

    def count(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)






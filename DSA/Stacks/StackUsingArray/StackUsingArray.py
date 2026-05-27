class Stack:
    def __init__(self):
        self.data = []

    def push(self,item):
        self.data.append(item)

    def pop(self):
        if self.isEmpty():
            print("Hey Stack is Empty")
            return None
        return self.data.pop()

    def top(self):
        if self.isEmpty():
            return None
        return self.data[-1]

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0

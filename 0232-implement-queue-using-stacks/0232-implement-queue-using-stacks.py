class MyQueue(object):

    def __init__(self):
        self.input_s = []
        self.output_s = []

    def push(self, x):
        self.input_s.append(x)
        

    def pop(self):
        self.peek()
        return self.output_s.pop()
        

    def peek(self):
        if not self.output_s:
            while self.input_s:
                self.output_s.append(self.input_s.pop())
        return self.output_s[-1]
        

    def empty(self):
        return not self.input_s and not self.output_s
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
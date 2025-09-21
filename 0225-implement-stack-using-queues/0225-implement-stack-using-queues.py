class MyStack(object):

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1
        

    def pop(self):
        return self.q1.pop(0)
        

    def top(self):
        return self.q1[0]
        

    def empty(self):
        return not self.q1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
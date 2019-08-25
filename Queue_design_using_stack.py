class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.x=x
        self.stack.append(self.x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        a=self.stack[0]
        self.stack.remove(a)
        return a

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack) >= 1:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

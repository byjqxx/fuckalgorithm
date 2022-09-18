class Stack():
    """
    栈的实现：用列表作为栈，列表末尾为栈顶。
    isEmpty: 判断栈是否为空
    push: 入栈
    pop: 返回并删除栈顶元素
    peek: 返回栈顶元素，不删除
    size: 返回栈长度
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push('a')
    s.push(2)
    s.push('b')
    print(s.items)
    print(s.pop())
    print(s.size())
    print(s.items)
    print(s.peek())
    print(s.items)
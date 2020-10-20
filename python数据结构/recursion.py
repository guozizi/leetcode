from double_link_list import Deque

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

# print(fact(10))

def print_num(n):
    if n > 0:
        print_num(n-1)
        print(n)

print_num(10)



class Stack(object):
    def __init__(self):
        self.deque = Deque()

    def push(self, value):
        return self.deque.append(value)

    def pop(self):
        return self.deque.pop()

    def __len__(self):
        return len(self.deque)

    def is_empty(self):
        return len(self) == 0

def print_num_use_stack(n):
    s = Stack()
    while n > 0:
        s.push(n)
        n -= 1

    while not s.is_empty():
        print(s.pop())

print_num_use_stack(10)

# 递归用栈实现，会有栈溢出的问题
# 尾递归


def hanoi_move(n, source, dest, intermediate):
    if n >= 1:
        hanoi_move(n-1, source, intermediate, dest)
        print("Move %s -> %s" % (source, dest))
        hanoi_move(n - 1, intermediate, dest, source)

hanoi_move(4, 'A', 'C', 'B')
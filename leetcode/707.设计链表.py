class MyLinkedList:
    class Node:
        def __init__(self, val, next):
            self.val = val
            self.next = next

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 定义首结点
        self.head = None
        # 链表大小
        self.count = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        p = self.head
        if self.count == 0 or index > self.count - 1:
            return -1
        else:
            i = 1
            while i <= index:
                p = p.next
                i += 1
            return p.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = self.Node(val, self.head)
        self.head = node
        self.count += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = self.Node(val, None)
        if self.count == 0:
            self.head = node
            self.count += 1
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = node
            self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        p = self.head
        post = self.head
        if index == self.count:
            self.addAtTail(val)
        elif index > self.count:
            return
        else:
            i = 1
            while i <= index:
                post = p
                p = p.next
                i += 1
            post.next = self.Node(val, p)
            self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        p = self.head
        post = self.head
        if self.count == 0 or index > (self.count - 1) or index < 0:
            return
        else:
            i = 1
            while i <= index:
                post = p
                p = p.next
                i += 1
            post.next = p.next
            self.count -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

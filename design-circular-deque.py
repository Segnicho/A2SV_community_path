class Node:
    def __init__(self,val, prev= None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.head = None
        self.tail = None
    def insertFront(self, value: int) -> bool:
        if self.size == self.k:
            return False
        elif self.size == 0:
            self.head = self.tail = Node(value)
        else:
            elmnt= Node(value)
            self.head.prev = elmnt
            elmnt.next =self.head
            self.head = elmnt
        self.size+=1
        return True
    def insertLast(self, value: int) -> bool:
        if self.size == self.k:
            return False
        if self.size == 0:
            self.head = self.tail = Node(value)
        else:
            elmnt= Node(value)
            self.tail.next = elmnt
            elmnt.prev =self.tail
            self.tail = elmnt
        self.size+=1
        return True
    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        self.head = self.head.next
        self.size -=1
        return True
    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        self.tail = self.tail.prev
        self.size -=1
        return True

    def getFront(self) -> int:
        if self.size == 0:
            return -1
        return self.head.val
        

    def getRear(self) -> int:
        if self.size == 0:
            return -1
        return self.tail.val
        

    def isEmpty(self) -> bool:
        return self.size == 0
    def isFull(self) -> bool:
        return self.size == self.k

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        dummy = self.head
        for _ in range(index):
            dummy = dummy.next
        return dummy.val
        
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        curr = self.head
        newNode = Node(val)
        if index <= 0:
            newNode.next = curr
            self.head = newNode
        else:
            for _ in range(index-1):
                curr = curr.next
            newNode.next = curr.next
            curr.next = newNode
        self.size+=1
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        dummy = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(index-1):
                dummy = dummy.next
            dummy.next = dummy.next.next
        self.size -=1
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)



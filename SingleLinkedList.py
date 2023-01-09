# 链表结点
class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.next = None

    def has_value(self, value):
        return self.data == value


# 单链表
class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head == None

    def length_singlelinklist(self):
        current_node = self.head
        current_id = 1

        while current_node is not None:
            current_node = current_node.next
            current_id += 1

        return current_id

    def output_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        
        return

node1 = Node("Mon")
node2 = Node("Tue")
node3 = Node("Wed")
node4 = Node("Thur")
node5 = Node("Fri")
node6 = Node("Sat")
node7 = Node("Sun")
Slist = SingleLinkedList()
Slist.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
Slist.output_list()
print(f"length of Slist: {Slist.length_singlelinklist()}")

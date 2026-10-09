class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None    
        self.count = 0


    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.count += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.count += 1


    def insert(self, index, value):
        if index < 0 or index > self.count:
            raise IndexError("Index out of range")

        if index == 0:
            self.prepend(value)
            return
        if index == self.count:
            self.append(value)
            return

        new_node = Node(value)
        current = self.head
        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.count += 1

    def get(self,index):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of bounds")
       
        current = self.head
        for _ in range(index):
            current = current.next

        return current.value

    def find(self, value):
        current = self.head
        index=0

        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __len__(self):
        def _count_nodes(node):
            if node is None:
                return 0
            return 1 + _count_nodes(node.next)

        return _count_nodes(self.head)

    def update(self, index, value):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of bounds")

        current = self.head
        for _ in range(index):
            current = current.next

        current.value = value
   

    def delete(self, value):
        if self.head is None:
            return False

        
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.count -= 1
            return True

        
        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        
        if current.next is not None:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            self.count -= 1
            return True

        return False
    
    def print_list(self):
        if self.head is None:
            print("(empty)")
            return

        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements))

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
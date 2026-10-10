class ArrayStack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def reverse(self):
        def _rec_swap(left, right):
            if left >= right:
                return
            self.items[left], self.items[right] = self.items[right], self.items[left]
            _rec_swap(left + 1, right - 1)

        _rec_swap(0, len(self.items) - 1)

    def __str__(self):
        
        return ", ".join(map(str, self.items))


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedListStack:
    def __init__(self):
        self.top_node = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        val = self.top_node.val
        self.top_node = self.top_node.next
        return val

    def peek(self):
        return self.top_node.val

    def is_empty(self):
        return self.top_node is None

    def reverse(self):
        def _rec_reverse(curr, prev):
            if curr is None:
                return prev
            nxt = curr.next
            curr.next = prev
            return _rec_reverse(nxt, curr)

        self.top_node = _rec_reverse(self.top_node, None)

    def __str__(self):
        def _to_list_rec(node):
            if node is None:
                return []
            return _to_list_rec(node.next) + [str(node.val)]

        return ", ".join(_to_list_rec(self.top_node))



class DNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedListStack:
    def __init__(self):
        self.top_node = None

    def push(self, val):
        new_node = DNode(val)
        new_node.next = self.top_node
        if self.top_node:
            self.top_node.prev = new_node
        self.top_node = new_node

    def pop(self):
        val = self.top_node.val
        self.top_node = self.top_node.next
        if self.top_node:
            self.top_node.prev = None
        return val

    def peek(self):
        return self.top_node.val

    def is_empty(self):
        return self.top_node is None

    def reverse(self):
        def _rec_reverse(curr):
            if curr is None:
                return None
            
            curr.prev, curr.next = curr.next, curr.prev
            if curr.prev is None:
                return curr
            return _rec_reverse(curr.prev)

        self.top_node = _rec_reverse(self.top_node)

    def __str__(self):
        def _to_list_rec(node):
            if node is None:
                return []
            return _to_list_rec(node.next) + [str(node.val)]

        return ", ".join(_to_list_rec(self.top_node))


def run_test(stack_class, name):
    print(f"=== {name} ===")
    stack = stack_class()
    
    
    for i in range(1, 11):
        stack.push(i)

    print("Before:", stack)
    stack.reverse()
    print("After :", stack)
    print()


if __name__ == "__main__":
    run_test(ArrayStack, "Array Stack")
    run_test(SinglyLinkedListStack, "Singly Linked List Stack")
    run_test(DoublyLinkedListStack, "Doubly Linked List Stack")
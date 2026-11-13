import sys
import ast

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class LinkedMinHeap:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def __len__(self):
        return self.size
        
    def is_empty(self):
        return self.size == 0
        
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty heap")
        return self.root.value
        
    def _get_node_at(self, position):
        if position <= 0: return None
        path = bin(position)[3:] 
        current = self.root
        for direction in path:
            if direction == '0':
                current = current.left
            else:
                current = current.right
        return current
        
    def insert(self, value):
        new_node = Node(value)
        self.size += 1
        
        if self.size == 1:
            self.root = new_node
            return
            
        parent_node = self._get_node_at(self.size // 2)
        new_node.parent = parent_node
        
        if self.size % 2 == 0:
            parent_node.left = new_node
        else:
            parent_node.right = new_node
            
        self._sift_up(new_node)
        
    def extract_min(self):
        if self.is_empty():
            raise IndexError("extract_min from empty heap")
            
        min_val = self.root.value
        
        if self.size == 1:
            self.root = None
            self.size -= 1
            return min_val
            
        last_node = self._get_node_at(self.size)
        self.root.value = last_node.value
        
        if last_node.parent.left == last_node:
            last_node.parent.left = None
        else:
            last_node.parent.right = None
        last_node.parent = None
        
        self.size -= 1
        if self.root:
            self._sift_down(self.root)
        
        return min_val

    def _sift_up(self, node):
        while node.parent is not None and node.value < node.parent.value:
            node.value, node.parent.value = node.parent.value, node.value
            node = node.parent
            
    def _sift_down(self, node):
        while node.left is not None:
            smallest_child = node.left
            if node.right is not None and node.right.value < node.left.value:
                smallest_child = node.right
                
            if node.value <= smallest_child.value:
                break
                
            node.value, smallest_child.value = smallest_child.value, node.value
            node = smallest_child

class RunningMedian:
    def __init__(self):
        self.left_heap = LinkedMinHeap()
        self.right_heap = LinkedMinHeap()
        
    def add_sale(self, amount):
        if self.left_heap.is_empty() or amount <= -self.left_heap.peek():
            self.left_heap.insert(-amount)
        else:
            self.right_heap.insert(amount)
            
        if len(self.left_heap) > len(self.right_heap) + 1:
            val = -self.left_heap.extract_min()
            self.right_heap.insert(val)
        elif len(self.right_heap) > len(self.left_heap):
            val = self.right_heap.extract_min()
            self.left_heap.insert(-val)
            
    def get_median(self):
        if len(self.left_heap) == 0 and len(self.right_heap) == 0:
            return None
        if len(self.left_heap) > len(self.right_heap):
            return float(-self.left_heap.peek())
        else:
            return (-self.left_heap.peek() + self.right_heap.peek()) / 2.0

if __name__ == '__main__':
    input_text = sys.stdin.read().strip()
    if input_text:
        sales = ast.literal_eval(input_text)
        rm = RunningMedian()
        medians = []
        for sale in sales:
            rm.add_sale(sale)
            medians.append(rm.get_median())
        print(medians)
    else:
        print([])
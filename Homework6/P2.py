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

    def delete(self, value):
        target_node = self._find_node_bfs(self.root, value)
        if not target_node:
            return False
            
        if self.size == 1:
            self.root = None
            self.size -= 1
            return True
            
        last_node = self._get_node_at(self.size)
        target_node.value = last_node.value
        
        if last_node.parent.left == last_node:
            last_node.parent.left = None
        else:
            last_node.parent.right = None
        last_node.parent = None
        self.size -= 1
        
        if target_node.parent and target_node.value < target_node.parent.value:
            self._sift_up(target_node)
        else:
            self._sift_down(target_node)
        return True

    def _find_node_bfs(self, node, value):
        if not node: return None
        queue = [node]
        while queue:
            curr = queue.pop(0)
            if curr.value == value: return curr
            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)
        return None

    def build(self, values):
        self.root = None
        self.size = 0
        for val in values:
            self.insert(val)

    def heap_sort(self):
        sorted_vals = []
        backup = []
        while not self.is_empty():
            val = self.extract_min()
            sorted_vals.append(val)
            backup.append(val)
        self.build(backup)
        return sorted_vals

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

    def print_heap(self):
        if self.is_empty(): return
        queue = [(self.root, 0, "")]
        lines = []
        while queue:
            node, level, prefix = queue.pop(0)
            if level == len(lines):
                lines.append([])
            if node != self.root:
                lines[level].append(f"{prefix}\n{node.value}")
            else:
                lines[level].append(str(node.value))
                
            if node.left: queue.append((node.left, level + 1, "/"))
            if node.right: queue.append((node.right, level + 1, "\\"))
            
        for level in lines:
            print("  ".join(level))

if __name__ == '__main__':
    input_text = sys.stdin.read().strip()
    if input_text:
        values = ast.literal_eval(input_text)
        print(f"Input values: {values}")
        heap = LinkedMinHeap()
        for val in values:
            heap.insert(val)
            print(f"After insert({val}):")
            heap.print_heap()
import sys
import ast

class ArrayMinHeap:
    def __init__(self):
        self.heap = []
        
    def push(self, item):
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)
        
    def pop(self):
        if not self.heap: return None
        if len(self.heap) == 1: return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root
        
    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        if idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            self._sift_up(parent)
            
    def _sift_down(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
            
        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._sift_down(smallest)

    def is_empty(self):
        return len(self.heap) == 0

def merge_logs(logs):
    pq = ArrayMinHeap()
    result = []
    
    for i in range(len(logs)):
        if logs[i]:  
            pq.push((logs[i][0], i + 1, 0))
            
    while not pq.is_empty():
        time, reg_id, idx = pq.pop()
        result.append((time, reg_id))
        
        if idx + 1 < len(logs[reg_id - 1]):
            pq.push((logs[reg_id - 1][idx + 1], reg_id, idx + 1))
            
    return result

if __name__ == '__main__':
    input_text = sys.stdin.read().strip()
    if input_text:
        lines = input_text.split('\n')
        logs = [ast.literal_eval(line.strip()) for line in lines if line.strip()]
        print(merge_logs(logs))
import sys
import ast
from problem2 import LinkedMinHeap

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
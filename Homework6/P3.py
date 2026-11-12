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

def process_sales(sales):
    rm = RunningMedian()
    medians = []
    for sale in sales:
        rm.add_sale(sale)
        medians.append(rm.get_median())
    return medians
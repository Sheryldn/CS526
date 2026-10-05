from problem4 import SortedDoublyLinkedList

sll = SortedDoublyLinkedList()


for val in [10, 4, 29, 8, 2, 15, 41]:
    sll.add(val)

print("Initial list:")
sll.print_list()  

print(f"total(): {sll.total()}")                     # 109
print(f"sum_middle_three(): {sll.sum_middle_three()}") # 33 (8 + 10 + 15)
print(f"median(): {sll.median()}")                     # 10.0

print("\nAfter deleting 41:")
sll.delete(41)
sll.print_list()  

print(f"sum_middle_three(): {sll.sum_middle_three()}") # 22 (4 + 8 + 10)
print(f"median(): {sll.median()}")                     # 9.0 ((8 + 10) / 2)

print("\nAfter adding 8:")
sll.add(8)
sll.print_list()  

print(f"count(8): {sll.count(8)}")     # 2
print(f"count(5): {sll.count(5)}")     # 0
print(f"exists(15): {sll.exists(15)}") # True
print(f"exists(5): {sll.exists(5)}")   # False
print(f"total(): {sll.total()}")       # 76
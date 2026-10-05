class Node:
    """双向链表节点类"""
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class SortedDoublyLinkedList:
    """有序双向链表类（保持升序排列）"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  # 节点数量（使用 size 命名避开 count 方法同名冲突）

    def add(self, value):
        """插入新节点并保持升序"""
        new_node = Node(value)
        self.size += 1

        # 1. 链表为空
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # 2. 插入最头部
        if value <= self.head.value:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return

        # 3. 插入最尾部
        if value >= self.tail.value:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            return

        # 4. 插入中间合适位置
        current = self.head
        while current and current.value < value:
            current = current.next

        prev_node = current.prev
        new_node.next = current
        new_node.prev = prev_node
        prev_node.next = new_node
        current.prev = new_node

    def delete(self, value):
        """删除一个等于 value 的节点；找到并删除返回 True，未找到返回 False"""
        current = self.head

        while current:
            # 有序性：当前节点值已超出目标值，提前终止
            if current.value > value:
                break

            if current.value == value:
                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None
                elif current == self.head:
                    self.head = current.next
                    self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                self.size -= 1
                return True

            current = current.next

        return False

    def exists(self, value):
        """递归检查是否存在（带早期终止）"""
        def _exists_helper(node):
            if node is None or node.value > value:
                return False
            if node.value == value:
                return True
            return _exists_helper(node.next)

        return _exists_helper(self.head)

    def count(self, value):
        """递归统计出现次数（带早期终止）"""
        def _count_helper(node):
            if node is None or node.value > value:
                return 0
            if node.value == value:
                return 1 + _count_helper(node.next)
            return _count_helper(node.next)

        return _count_helper(self.head)

    def total(self):
        """递归计算节点值之和"""
        def _total_helper(node):
            if node is None:
                return 0
            return node.value + _total_helper(node.next)

        return _total_helper(self.head)

    def print_list(self):
        """递归收集节点值并按 <-> 格式输出"""
        if self.head is None:
            print("(empty)")
            return

        def _get_values_helper(node):
            if node is None:
                return []
            return [str(node.value)] + _get_values_helper(node.next)

        values = _get_values_helper(self.head)
        print(" <-> ".join(values))

    def _get_node_at(self, index):
        """辅助函数：获取 0-based 索引处的节点"""
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def sum_middle_three(self):
        """计算中间 3 个节点的和"""
        if self.size < 3:
            raise ValueError("List has fewer than 3 nodes.")

        mid = self.size // 2

        # 奇数个节点：取 mid-1, mid, mid+1
        if self.size % 2 != 0:
            idx1, idx2, idx3 = mid - 1, mid, mid + 1
        # 偶数个节点：取 mid-2, mid-1, mid
        else:
            idx1, idx2, idx3 = mid - 2, mid - 1, mid

        v1 = self._get_node_at(idx1).value
        v2 = self._get_node_at(idx2).value
        v3 = self._get_node_at(idx3).value

        return v1 + v2 + v3

    def median(self):
        """计算中位数"""
        if self.size == 0:
            raise ValueError("List is empty.")

        mid = self.size // 2

        # 奇数个节点：取中间节点值
        if self.size % 2 != 0:
            return float(self._get_node_at(mid).value)
        # 偶数个节点：取中间两个节点值的平均值
        else:
            v1 = self._get_node_at(mid - 1).value
            v2 = self._get_node_at(mid).value
            return (v1 + v2) / 2.0
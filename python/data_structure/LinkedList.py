from typing import Optional, Any


class Node:
    def __init__(self, data: Optional[Any]):
        self.data = data
        self.next = None
    
class Single:
    def __init__(self):
        self.head = None

    def display(self):
        """ Hiển thị danh sách liên kết. """
        current_node = self.head
        while current_node:
            print(f"Data = {current_node.data}, Next = {current_node.next.data if current_node.next else None}")
            current_node = current_node.next

    def append(self, data):
        """ Tạo node mới.
            Trường hợp 1: Thêm node mới vào danh sách rỗng.
            Trường hợp 2: Thêm node mới vào danh sách đã có nodes.
                + B1: Xác định con trỏ ở node đầu tiên (head)
                + B2: Di chuyển con trỏ từ node đầu tiên đến node cuối cùng (con trỏ bằng null -> đang ở node cuối cùng)
                + B3: Tạo node mới sau node cuối cùng
            Ví dụ: Tạo node mới lần lượt 1,2,3,4
                + B1: Danh sách rỗng -> Next = None, node đầu tiên = 1, Thêm node(1) vào danh sách.
                + B2: Danh sách: 1 -> None, Từ node(1) --> đến node có next(null), tạo node(2) vào danh sách (sau node(1))
                + B3: Danh sách: 1 -> 2 -> None, Từ node(1) --> di chuyên đến node có next(null), tạo node(3) vào danh sách (sau node(2))
                + B4: Danh sách: 1 -> 2 -> 3 -> None, Từ node(1) --> di chuyển đến node có next(null), tạo node(4) vào danh sách (sau node(3))
                + Danh sách: 1 -> 2 -> 4 -> None.
        Args:
            data (_type_): Dữ liệu của node
        """
        new_node = Node(data)

        # Nếu danh sách rỗng -> Thêm node mới vào đầu danh sách.
        if not self.head:
            self.head = new_node
            return # Thoát hàm
        else:
            last_node = self.head
            while last_node.next: # Chạy cho đến khi con trỏ bằng null -> đã ở node cuối
                last_node = last_node.next
            last_node.next = new_node

    def from_list(self,iterable):
        for data in iterable:
            self.append(data)
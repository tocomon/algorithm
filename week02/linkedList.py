# 노드 정의
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# 연결 리스트 생성
class LinkedList:
    def __init__(self):
        self.head = None

    # 데이터 추가
    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

    # 데이터 검색
    def find_node(self, data):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == data:
                return True
            curr_node = curr_node.next
        return False

    # 연결 리스트 출력
    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next

# 연결 리스트 사용
my_list = LinkedList()
my_list.add_node(1)
my_list.add_node(2)
my_list.add_node(3)
my_list.add_node(4)
my_list.add_node(5)

# 데이터 검색
print(my_list.find_node(3))  # 출력: True
print(my_list.find_node(6))  # 출력: False

# 연결 리스트 출력
my_list.print_list()

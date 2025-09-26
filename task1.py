class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur =self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key:int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # ===== Реверсування списку =====
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    # ===== Сортування списку (сортування вставками) =====
    def sort(self):
        if self.head is None or self.head.next is None:
            return
        sorted_head =None
        current = self.head
        while current:
            next_node = current.next
            if sorted_head is None or current.data < sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                search = sorted_head
                while search.next and search.next.data < current.data:
                    search = search.next
                current.next = search.next
                search.next = current
            current = next_node
        self.head = sorted_head

    # ===== Об’єднання двох відсортованих списків =====
    @staticmethod
    def merge_sorted(list1, list2):
        dummy = Node()
        tail = dummy
        a = list1.head
        b = list2.head

        while a and b:
            if a.data < b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        if a:
            tail.next = a
        if b:
            tail.next = b

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list


# ===== Приклад використання =====
llist1 = LinkedList()
llist2 = LinkedList()

for val in [15, 10, 5]:
    llist1.insert_at_beginning(val)

for val in [20, 25, 30]:
    llist2.insert_at_end(val)

print("Перший список:")
llist1.print_list()

print("Другий список:")
llist2.print_list()

# Реверсування першого списку
llist1.reverse()
print("\nПерший список після реверсу:")
llist1.print_list()

# Сортування першого списку
llist1.sort()
print("\nПерший список після сортування:")
llist1.print_list()

# Об’єднання двох відсортованих списків
merged = LinkedList.merge_sorted(llist1, llist2)
print("\nОб’єднаний відсортований список:")
merged.print_list()

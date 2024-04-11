class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, self.head)
        self.head.next = self.tail
        self.size = 0
        self.dic = {}

    def __str__(self):
        lst = []
        cur = self.head

        while cur.data:
            lst.append((cur.data.id, cur.data.w))
            cur = cur.next

        return f'{lst}'

    def is_empty(self):
        if self.size:
            return False
        else:
            return True

    def popleft(self):
        if self.is_empty():
            return
        else:
            head = self.head
            if self.size == 1:
                self.head = Node(None, None, self.tail)
                self.tail.prev = self.head
            else:
                self.head = head.next
                self.head.prev = None
            self.dic.pop(head.data.id)
            self.size -= 1
            return head.data

    def append(self, data: Package):
        node = Node(data, None, self.tail)

        if self.is_empty():
            self.head = node
        else:
            last = self.tail.prev
            last.next = node
            node.prev = last

        self.tail.prev = node
        self.dic[data.id] = node
        self.size += 1
        return

    def remove_by_id(self, id):
        if self.is_empty():
            return False

        if id in self.dic.keys():  # 존재
            node = self.dic[id]
            if node == self.head:
                if self.size == 1:
                    self.head = Node(None, None, self.tail)
                    self.tail.prev = self.head
                else:
                    self.head = node.next
                    self.head.prev = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            self.size -= 1
            self.dic.pop(id)
            return True
        return False

    def find_by_id(self, id):
        if self.is_empty():
            return False
        if id in self.dic.keys():  # 존재
            node = self.dic[id]

            if self.head == node:
                return True

            head = self.head
            last = self.tail.prev

            node.prev.next = self.tail
            self.tail.prev = node.prev

            last.next = head
            head.prev = last

            node.prev = None
            self.head = node

            return True
        return False


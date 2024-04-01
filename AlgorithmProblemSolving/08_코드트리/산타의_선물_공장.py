from collections import defaultdict


class Package:
    def __init__(self, id, w):
        self.id = id
        self.w = w


class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Container:
    def __init__(self, status=1):
        self.head = Node(None)
        self.tail = Node(None, self.head)
        self.head.next = self.tail
        self.size = 0
        self.status = status  # 1 정상 0 고장
        self.id_to_package = defaultdict(Node)

    def is_empty(self):
        if self.size:
            return False
        else:
            return True

    def put_down(self, w_max):
        if self.is_empty():
            return 0

        if self.head.w == w_max:
            w = self.head.w
            self.popleft()
            return w
        else:
            self.append(self.popleft())
            return 0

    def popleft(self):
        if self.is_empty():
            return
        else:
            head = self.head
            self.head = head.next
            self.head.prev = None
            self.size -= 1
            return head

    def append(self, data: Package):

        if self.is_empty():
            self.head = Node(data)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
            self.id_to_package[data.id] = self.head
        else:
            last = self.tail.prev
            node = Node(data, last, self.tail)
            last.next = node
            self.tail.prev = node
            self.id_to_package[data.id] = node

        self.size += 1

        return

    def remove_by_id(self, id):
        if id in self.id_to_package.keys():  # 존재
            node = self.id_to_package[id]
            self.id_to_package.pop(id)
            node.prev.next = node.next
            node.next.prev = node.prev
            size -= 1
            return id
        return -1

    def find_by_id(self, id):
        if id in self.id_to_package.keys():  # 존재
            node = self.id_to_package[id]
            head = self.head
            last = self.tail.prev

            self.head = node
            self.head.prev.next = self.tail
            self.head.prev = None

            head.prev = last
            last.next = head
            return id
        return -1

    def is_disabled(self):
        if self.status:
            return False
        else:
            return True

    def be_disabled_and_get_remain(self):
        self.status = 0
        return self.id_to_package


Q = int(input())

for _ in range(Q):
    ipt = input().split()
    containers = [None]

    if ipt[0] == '100':
        N = int(ipt[1])
        M = int(ipt[2])
        id_lst = ipt[3:3 + N]
        w_lst = ipt[3 + N:]
        package_cnt = N / M
        for si in range(0, N, package_cnt):
            container = Container()
            for i in range(si, si + package_cnt):
                container.append(Package(id_lst[i], w_lst[i]))
            containers.append(container)

    elif ipt[0] == '200':
        pass
    elif ipt[0] == '300':
        pass
    elif ipt[0] == '400':
        pass
    else:
        pass

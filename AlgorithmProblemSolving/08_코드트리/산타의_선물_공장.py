import sys

input = sys.stdin.readline


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
        self.id_to_package = {}

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

    def put_down(self, w_max):
        if self.is_empty() or self.is_disabled():
            return 0

        if self.head.data.w <= w_max:
            w = self.head.data.w
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
            if self.size == 1:
                self.head = Node(None, None, self.tail)
                self.tail.prev = self.head
            else:
                self.head = head.next
                self.head.prev = None
            self.id_to_package.pop(head.data.id)
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
        self.id_to_package[data.id] = node
        self.size += 1
        return

    def remove_by_id(self, id):
        if self.is_empty():
            return False

        if id in self.id_to_package.keys():  # 존재
            node = self.id_to_package[id]
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
            self.id_to_package.pop(id)
            return True
        return False

    def find_by_id(self, id):
        if self.is_empty():
            return False
        if id in self.id_to_package.keys():  # 존재
            node = self.id_to_package[id]

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

    def is_disabled(self):
        if self.status:
            return False
        else:
            return True

    def be_disabled_and_get_remain(self):
        self.status = 0
        self.size = 0
        data_lst = []
        cur = self.head
        while cur.data:
            data_lst.append(cur.data)
            cur = cur.next

        return data_lst


Q = int(input())
containers = [None]
for _ in range(Q):
    ipt = input().split()

    if ipt[0] == '100':
        N = int(ipt[1])
        M = int(ipt[2])
        id_lst = list(map(int, ipt[3:3 + N]))
        w_lst = list(map(int, ipt[3 + N:]))
        package_cnt = N // M
        for si in range(0, N, package_cnt):
            container = Container()
            for i in range(si, si + package_cnt):
                container.append(Package(id_lst[i], w_lst[i]))
            containers.append(container)

    elif ipt[0] == '200':
        w_max = int(ipt[1])
        sm = 0
        for i in range(1, M + 1):
            sm += containers[i].put_down(w_max)
        print(sm)

    elif ipt[0] == '300':
        r_id = int(ipt[1])
        res = -1
        for i in range(1, M + 1):
            if containers[i].remove_by_id(r_id):
                res = r_id
                break
        print(res)

    elif ipt[0] == '400':
        f_id = int(ipt[1])
        num = -1
        for i in range(1, M + 1):
            if containers[i].find_by_id(f_id):
                num = i
                break
        print(num)
    else:
        b_num = int(ipt[1])
        if containers[b_num].is_disabled():
            print(-1)
        else:
            remain_data_lst = containers[b_num].be_disabled_and_get_remain()

            nxt = b_num + 1

            while nxt != b_num:
                if nxt > M:
                    nxt = 1
                if not containers[nxt].is_disabled():
                    break
                else:
                    nxt += 1

            for data in remain_data_lst:
                containers[nxt].append(data)
            print(b_num)

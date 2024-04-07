a = 1000  # A~z : 65~122
M = 10000003  # 보통 input 크기의 2배
EMPTY = -1
OCCUPY = 0
DUMMY = 1


class HashTable:  # key: 이름(str) / val: 전화번호(str)

    def __init__(self, size):
        self.size = size
        self.status = [EMPTY] * self.size
        self.key = [None] * self.size
        self.val = [None] * self.size

    def my_hash(self, data):  # data의 해시 값 얻기
        hash = 0
        for d in data:
            hash = (hash * a + ord(d)) % self.size
        return hash

    def find(self, k: str):
        idx = self.my_hash(k)
        while self.status[idx] != EMPTY:
            if self.status[idx] == OCCUPY and self.key[idx] == k:
                return idx
            idx = (idx + 1) % self.size
        return -1

    def insert(self, k: str, v: str):  # k를 key로 v를 value로 저장
        idx = self.find(k)
        if idx != -1:  # 위치 발견
            self.val[idx] = v
            return
        idx = self.my_hash(k)
        while self.status[idx] == OCCUPY:
            idx = (idx + 1) % self.size
        self.key[idx] = k
        self.val[idx] = v
        self.status[idx] = OCCUPY

    def delete(self, k: str):
        idx = self.find(k)
        if idx != -1:
            self.status[idx] = DUMMY


h_table = HashTable(10)
h_table.insert('Harry', '1-555-1234')
h_table.insert('John', '1-545-1224')
print(h_table.key)
print(h_table.val)
print(h_table.status)
print(h_table.find('Harry'))
h_table.delete('Harry')
print(h_table.key)
print(h_table.val)
print(h_table.status)
h_table.insert('Harry', '1-999-9994')
print(h_table.key)
print(h_table.val)
print(h_table.status)

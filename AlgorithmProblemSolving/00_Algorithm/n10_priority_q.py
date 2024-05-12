import heapq


class Student:
    def __init__(self, p1, p2, id):
        self.p1 = p1
        self.p2 = p2
        self.id = id

    def __lt__(self, other):
        if self.p1 != other.p1:
            return self.p1 > other.p1
        else:
            return self.p2 < other.p2


heap = []


def heap_init():
    global heap
    heap = []


index_map = {}


def up(index):
    cur = index
    parent = (cur >> 1)

    while parent > 0 and heap[cur] < heap[parent]:
        heap[cur], heap[parent] = heap[parent], heap[cur]
        index_map[heap[cur].id], index_map[heap[parent].id] = cur, parent
        cur = parent
        parent = (cur >> 1)


def down(index):
    cur = index
    child = (cur << 1)

    while child <= len(heap):
        if child + 1 <= len(heap) and heap[child] > heap[child + 1]:
            child += 1
        if heap[cur] < heap[child]:
            break
        heap[cur], heap[child] = heap[child], heap[cur]
        index_map[heap[cur].id], index_map[heap[child].id] = cur, child
        cur = child
        child = (cur << 1)


def push(data):
    global heap
    heap.append(data)
    index_map[data.id] = len(heap)
    up(len(heap))


def pop():
    global heap
    if not heap:
        return None
    ret = heap[0]
    del index_map[ret.id]
    if len(heap) == 1:
        heap = []
    else:
        heap[0] = heap.pop()
        index_map[heap[0].id] = 1
        down(1)
    return ret


def remove(id):
    if id not in index_map:
        return
    index = index_map[id]
    heap[index - 1].p1 = 99999
    heap[index - 1].p2 = -1
    up(index)
    pop()


def update(id, new_p1, new_p2):
    if id not in index_map:
        return
    index = index_map[id]
    heap[index - 1].p1 = new_p1
    heap[index - 1].p2 = new_p2
    up(index)
    down(index)


def main():
    heap_init()
    p1, p2, id = 1, 2, 10

    for _ in range(10):
        student = Student(p1, p2, id)
        push(student)
        if id & 1:
            p1 += 1
        if p2 == 1:
            p2 = 2
        else:
            p2 -= 1
        id -= 1

    print("Before removing student with id 6:")
    while heap:
        ret = pop()
        print(f"p1: {ret.p1}, p2: {ret.p2}, id: {ret.id}")

    remove(6)
    print("\nAfter removing student with id 6:")
    while heap:
        ret = pop()
        print(f"p1: {ret.p1}, p2: {ret.p2}, id: {ret.id}")

    update(5, 10, 1)
    print("\nAfter updating student with id 5:")
    while heap:
        ret = pop()
        print(f"p1: {ret.p1}, p2: {ret.p2}, id: {ret.id}")


if __name__ == "__main__":
    main()
from datetime import date
import calendar

month_len = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
key_arr = (
    'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')
days_in_month = {'Янваарь': 31, 'Февраль': 28, 'Март': 31,
                 'Апрель': 30, 'Май': 31, 'Июнь': 30,
                 'Июль': 31, 'Август': 31, 'Сентябрь': 30,
                 'Октябрь': 31, 'Ноябрь': 30, 'Декабрь': 31}


def print_month(month: str, year: int):
    idx = key_arr.index(month)
    wd = date(year, idx + 1, 1).weekday()
    days = month_len[idx]
    if calendar.isleap(year) and idx == 1:
        days += 1
    print(f"{month} {year}".center(20))
    print("Пн Вт Ср Чт Пт Сб Вс")
    print('   ' * wd, end='')
    for day in range(days):
        wd = (wd + 1) % 7
        eow = " " if wd % 7 else "\n"
        print(f"{day + 1:2}", end=eow)
    print()


def print_year(year: int):
    for month in key_arr:
        print_month(month, year)


def base32(w: str):
    val = 0
    for ch in w.lower():
        next_digit = ord(ch) - ord('а')
        val = 32 * val + next_digit
    return val


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.N = 0

    def __len__(self):
        return self.N

    def __getitem__(self, item):
        hc = hash(item) % self.size
        for entry in self.table[hc]:
            if entry.key == item:
                return entry.value

    def __str__(self):
        border = "+-" + "-" * (self.size // 50) + "-+"
        rows = [border]
        rows.append("| key | value |")
        rows.append(border)
        for bucket in self.table:
            if len(bucket) == 0:
                continue
            else:
                for entry in bucket:
                    row = f"| {entry.key} | {entry.value} "
                    rows.append(row)
            rows[-1] += "|"
            rows.append(border)
        return "\n".join(rows)

    def get(self, k):
        hc = hash(k) % self.size
        for entry in self.table[hc]:
            if entry.key == k:
                return entry.value
        return None

    def put(self, k, v):
        hc = hash(k) % self.size
        for entry in self.table[hc]:
            if entry.key == k:
                entry.value = v
                return
        self.table[hc].append(Entry(k, v))
        self.N += 1

    def remove(self, k):
        hc = hash(k) % self.size
        for i, entry in enumerate(self.table[hc]):
            if entry.key == k:
                del self.table[hc][i]
                self.N -= 1
                return entry.value
        return None

    def __iter__(self):
        for chain in self.table:
            for entry in chain:
                yield entry.key, entry.value


class DynamicHashTable:
    def __init__(self, size: int):
        self.table = [[] for _ in range(size)]
        if size < 0:
            raise ValueError("Hashtable storage must Ье at least 1")
        self.size = size
        self.N = 0

        self.load_factor = 0.75
        self.threshold = min(self.size * self.load_factor, size - 1)

    def __getitem__(self, item):
        hc = hash(item) % self.size
        for entry in self.table[hc]:
            if entry.key == item:
                return entry.value
        return None

    def __len__(self):
        return self.N

    def get(self, k):
        hc = hash(k) % self.size
        for entry in self.table[hc]:
            if entry.key == k:
                return entry.value
        return None

    def put(self, k, v):
        hc = hash(k) % self.size
        for entry in self.table[hc]:
            if entry.key == k:
                entry.value = v
                return
        self.table[hc].append(Entry(k, v))
        self.N += 1

        if self.N >= self.threshold:
            self.resize(2 * self.size)

    def resize(self, new_size):
        temp = DynamicHashTable(new_size)
        for bucket in self.table:
            for key, value in bucket:
                temp.put(key, value)
        self.table, self.size = temp.table, new_size
        self.threshold = self.size * self.load_factor

    def __str__(self):
        border = "+-" + "-" * (len(self.table) // 50) + "-+"
        rows = [border]
        rows.append("| key | value |")
        rows.append(border)
        for bucket in self.table:
            if len(bucket) == 0:
                continue
            else:
                row = "|"
                for entry in bucket:
                    row += f" {entry.key} | {entry.value}"
                row += " _ |" * (len(bucket) - 1)
                rows.append(row)
                rows.append(border)
        return "\n".join(rows)

    def remove(self, k):
        hc = hash(k) % self.size
        for i, entry in enumerate(self.table[hc]):
            if entry.key == k:
                del self.table[hc][i]
                self.N -= 1
                return entry.value
        return None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, val):
        end: Node = Node(val)
        n = self
        while n.next:
            n: Node = n.next
        n.next: Node = end

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __str__(self):
        return ' -> '.join(str(o) for o in self)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f"Node with data {target_node_data} not found")

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f"Node with data {target_node_data} not found")

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception(f"Node with data {target_node_data} not found")


def test_hashtable():
    table = HashTable(1000)
    table.put('Апрель', 30)
    print(table)
    table.put('Май', 31)
    table.put('Сентябрь', 30)
    print(table)
    print(table.get('Апрель'))
    print(table.get('Август'))


def test_linked_list():
    ll = LinkedList([1, 2, 3])
    print(ll)
    ll.add_first(Node(4))
    print(ll)
    ll.add_last(Node(5))
    print(ll)
    ll.add_after(3, Node(6))
    print(ll)
    ll.add_before(1, Node(7))
    print(ll)
    ll.remove_node(3)
    print(ll)


def test_dynamic_hashtable():
    table = DynamicHashTable(1000)
    table.put('Апрель', 30)
    print(table)
    table.put('Май', 31)
    table.put('Сентябрь', 30)
    table.remove('Апрель')
    print(table)


if __name__ == '__main__':
    # print_year(2023)
    # test_hashtable()
    # test_linked_list()
    test_dynamic_hashtable()

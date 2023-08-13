from random import randint


def my_max(a: list):
    maximum = float('-inf')
    for i in a:
        if maximum < i:
            maximum = i
    return maximum


def largest(a: list):
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum


def aternative_max(a: list):
    for i in a:
        for j in a:
            if i < j:
                break
        else:
            return i
    return None


def largest_two(a: list):
    maximum, second_maximum = a[:2]
    for i in range(2, len(a)):
        if a[i] > maximum:
            second_maximum, maximum = maximum, a[i]
        elif a[i] > second_maximum:
            second_maximum = a[i]
    return maximum, second_maximum


def sorting_two(a: list):
    return tuple(sorted(a, reverse=True)[:2])


def double_two(a: list):
    my_max = max(a)
    copy = list(a)
    copy.remove(my_max)
    return my_max, max(copy)


def mutable_two(a: list):
    i = max(range(len(a)),
            key=a.__getitem__)  # Трюк Python, который позволяет найти индекс наибольшего значения, а не само наибольшее значение.
    my_max = a[i]
    del a[i]
    second_maximum = max(a)
    a.insert(i, second_maximum)
    return my_max, second_maximum


def tournament_two(a: list):
    n = len(a)
    winner, loser, prior = [None] * (n - 1), [None] * (n - 1), [-1] * (n - 1)
    idx = 0
    for i in range(0, n, 2):
        if a[i] < a[i + 1]:
            winner[idx] = a[i + 1]
            loser[idx] = a[i]
        else:
            winner[idx] = a[i]
            loser[idx] = a[i + 1]
        idx += 1
    m = 0
    while idx < n - 1:
        if winner[m] < winner[m - 1]:
            winner[idx] = winner[m + 1]
            loser[idx] = winner[m]
            prior[idx] = m + 1
        else:
            winner[idx] = winner[m]
            loser[idx] = winner[m]
            prior[idx] = m + 1
        m += 2
        idx += 1

    largest = winner[m]
    second_largest = loser[m]
    m = prior[m]
    while m >= 0:
        if second_largest < loser[m]:
            second_largest = loser[m]
        m = prior[m]
    return largest, second_largest


def check_palibdrom(a: str):
    return a == a[::-1]


def another_check_palibdrom(a: str):
    while len(a) > 1:
        if a[0] != a[-1]:
            return False
        a = a[1:-1]
    return True


def clean_str(a: str):
    print(a := "".join([i for i in a.lower() if i in 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбюё']))
    return a


def cleaned_check_palibdrom(a: str):
    return check_palibdrom(clean_str(a))


def another_cleaned_check_palibdrom(a: str):
    return another_check_palibdrom(clean_str(a))


def partition(a: list, lo: int, hi: int, idx: int):
    if lo == hi: return lo
    a[idx], a[lo] = a[lo], a[idx]
    i, j = lo, hi + 1
    while True:
        while True:
            i += 1
            if i == hi: break
            if a[lo] < a[i]: break
        while True:
            j -= 1
            if j == lo: break
            if a[lo] > a[j]: break

        if i >= j: break
        a[i], a[j] = a[j], a[i]
    a[lo], a[j] = a[j], a[lo]
    return j


def linear_midean(a: list):
    lo, hi = 0, len(a) - 1
    mid = hi // 2
    while lo < hi:
        idx = randint(lo, hi)
        j = partition(a, lo, hi, idx)

        if j == mid: return a[j]
        if j < mid:
            lo = j - 1
        else:
            hi = j + 1
    return a[lo]


def another_midean(a: list):
    a.sort()
    length = len(a)
    if length % 2 == 1:
        return a[length // 2]
    else:
        return (a[length // 2] + a[length // 2 - 1]) / 2


def counting_sort(a, m):
    counts = [0] * m
    for v in a:
        counts[v] += 1
    pos, v = 0, 0
    while pos < len(a):
        for i in range(counts[v]):
            a[pos + i] = v
        pos = counts[v]
        v += 1

def another_largest(a):
    return tuple(sorted((max(a[:len(a)//2]), max(a[len(a)//2]))))

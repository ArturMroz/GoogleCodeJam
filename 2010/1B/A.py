# File Fix-it
# https://code.google.com/codejam/contest/635101/dashboard#s=p0


class Node(object):

    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, value):
        c = Node(value)
        self.children.append(c)
        return c

    def get_child(self, value):
        for c in self.children:
            if c.data == value:
                return c
        return None


def add_children(h, n):
    added = 0
    for j in range(n):
        curr = h
        D = input()[1:-1].split('/')
        for d in D:
            child = curr.get_child(d)
            if not child:
                child = curr.add_child(d)
                added += 1
            curr = child
    return added


for tc in range(int(input())):
    n, m = map(int, input().split())
    added = 0

    h = Node('/')
    add_children(h, n)
    added = add_children(h, m)

    print('Case #{}: {}'.format(tc + 1, added))

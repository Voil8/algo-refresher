from bst_print import _display_aux as bstp
class Node:
    def __init__(self, key=None):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.height = 1

    def get_height(self):
        height = 1
        if self.left is None and self.right is None:
            return height
        elif self.left is not None and self.right is None:
            return height + self.left.get_height()

        elif self.right is not None and self.left is None:
            return height + self.right.get_height()

        else:
            return height + max(self.right.get_height(), self.left.get_height())

    def __repr__(self):
        lines, *_ = bstp(self)
        return '\n'.join(lines)
        # for line in lines:
            # print(line)


def height(bst_):
    if bst_ is None:
        return 0
    return 1 + max(height(bst_.left), height(bst_.right))


def add(bst, node):
    '''bst:Node is a bst root'''
    if bst is None:
        bst = node
    else:
        node.parent = bst
        if node.key < bst.key:
            bst.left = add(bst.left, node)
            bst.height = max(bst.height, 1+bst.left.height)
        else:
            bst.right = add(bst.right, node)
            bst.height = max(bst.height, 1+bst.right.height)
    return bst


def del_(bst_n):
    if bst_n.right is None:
        par = bst_n.parent
        if bst_n.key < par.key:
            par.left = bst_n.left
        else:
            par.right = bst_n.left
        # bst_n = bst_n.left
        # if bst_n is not None:
        #     bst_n.parent = par
        return

    ld = ldes(bst_n.right)
    rt = ld.right

    key = ld.key

    par = ld.parent
    if ld.key < par.key:
        par.left = rt
    else:
        par.right = rt

    bst_n.key = key

def find(bst, key):
    if bst is None:
        return
    if bst.key == key:
        return bst
    if key < bst.key:
        return find(bst.left, key)
    return find(bst.right, key)

def md_find(bst, key):
    if bst.key == key:
        return bst
    elif bst.key < key:
        if bst.right is not None:
            return md_find(bst.right, key)
        return bst
    elif bst.left is not None:
        return md_find(bst.left, key)
    return bst

def next_elem(bst_n):
    """given a node find node in the tree with
    next largest key"""
    if bst_n.right is not None:
        return ldes(bst_n.right)
    return ranc(bst_n)


def ldes(bst_n):
    if bst_n.left is None:
        return bst_n
    return ldes(bst_n.left)

def rdes(bst_n):
    if bst_n.right is None:
        return bst_n
    return rdes(bst_n.right)

def ranc(bst_n):
    if bst_n.parent is None:
        return
    if bst_n.key < bst_n.parent.key:
        return bst_n.parent
    return ranc(bst_n.parent)

def lanc(bst_n):
    if bst_n.parent is None:
        return
    if bst_n.key >= bst_n.parent.key:
        return bst_n.parent
    return lanc(bst_n.parent)

def prev_elem(bst_n):
    if bst_n.left is not None:
        return rdes(bst_n.left)
    return lanc(bst_n)

def range_search(bst_n, f, t):
    l = []
    node = md_find(bst_n, f)
    while node is not None and node.key < t:
        l.append(node)
        node = next_elem(node)
    return l

def dfs_pre(bst):
    if bst is None:
        return None
    print(bst.key, end=' ')
    dfs_pre(bst.left)
    dfs_pre(bst.right)


def dfs_in(bst):
    if bst is None:
        return None
    dfs_in(bst.left)
    print(bst.key, end=' ')
    dfs_in(bst.right)


def dfs_post(bst, a=None):
    if bst is None:
        return a
    dfs_post(bst.left)
    dfs_post(bst.right)
    print(bst.key, end=' ')




if __name__ == '__main__':
    test()

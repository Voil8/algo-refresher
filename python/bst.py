import pdb

class Node:
    def __init__(self, key=None):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        lines, *_ = self._display_aux()
        return '\n'.join(lines)
        # for line in lines:
            # print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2               

def add(bst, node):
    '''bst:Node is a bst root'''    
    if bst is None:
        bst = node
    else:
        node.parent = bst
        if node.key < bst.key:
            bst.left = add(bst.left, node)    
        else:
            bst.right = add(bst.right, node)    
    return bst



def find(bst, key):
    if bst is None:
        return
    if bst.key == key:
        return bst
    if key < bst.key:
        return find(bst.left, key)
    return find(bst.right, key)


    

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


def test():
    import random
    # arr = random.choices(range(300), k=10)
    arr = [131, 179, 198, 72, 22, 108, 111, 163, 272, 46]
    bst = Node(arr[0])
    for i in arr[1:]:
        add(bst, Node(i))
    # check add
    print(arr)
    print(bst)
    
    # for i in [dfs_pre, dfs_in, dfs_post]:
    #     i(bst)
    #     print()

    print('Check find')
    # print(bst)
    print(find(bst, 46))

    # pdb.set_trace()


if __name__ == '__main__':
    test()

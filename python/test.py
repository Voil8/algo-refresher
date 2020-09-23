import pdb
def test_bst():
    import bst as B
    import random, pdb
    # arr = random.choices(range(300), k=10)
    arr = [131, 179, 198, 72, 22, 108, 111, 163, 272, 46]
    bst_ = B.Node(arr[0])
    for i in arr[1:]:
        B.add(bst_, B.Node(i))
    # check add
    print(arr)
    print(bst_)

    # for i in [B.dfs_pre, B.dfs_in, B.dfs_post]:
    #     i(bst_)
    #     print()

    # print('Check find')
    # print(bst_)
    # print(B.find(bst_, 46))

    # print('\n\nChecking modified find')
    # print(B.md_find(bst_, 72))
    # print(B.md_find(bst_, 132))
    # print(B.md_find(bst_, 21))
    # print(B.md_find(bst_, 191))

    # print('\n\nNext elem testing')
    # for i in [72, 131, 21, 163, 111, 272]:
    #     a_node = B.md_find(bst_, i)
    #     print(f'found node: \n{a_node}\n')
    #     n_node = B.next_elem(a_node)
    #     print(f'Next node: \n{n_node}\n')

    # print('\n\nPrev elem testing')
    # for i in [72, 131, 21, 163, 111, 272]:
    #     a_node = B.md_find(bst_, i)
    #     print(f'found node: \n{a_node}\n')
    #     n_node = B.prev_elem(a_node)
    #     print(f'Prev node: \n{n_node}\n')

    # print('\n\nChecking range_search')
    # for f, t in [(72, 131), (108, 198), (272, 275), (19, 21)]:
    #     node_l = B.range_search(bst_, f, t)
    #     print(f'printing result for f={f}; t={t}\n')
    #     for node in node_l:
    #         print(node)
    #     print()


    print('\n\nChecking del_')
    for i in [72, 131, 21, 163, 111, 272, 46]:
        a_node = B.md_find(bst_, i)
        print(f'found node for {i}: \n{a_node}\n')
        B.del_(a_node)
        print(f'Tree now: \n{bst_}\n')

    # pdb.set_trace()

def more_bst_test():
    import more_bst as MB
    import bst as B

    arr = [131, 179, 198, 72, 22, 108, 111, 163, 272, 46]
    bst_ = B.Node(arr[0])
    for i in arr[1:]:
        B.add(bst_, B.Node(i))
    # check add
    print(arr)
    print(bst_)

    while(1):
        num = int(input('Enter node key to right rotate '))
        if num == -1: break
        node = B.md_find(bst_, num)
        print('Rotation of:')
        print(node)
        if node.parent is None:
            bst_ = MB.rotate_right(node)
        else:
            MB.rotate_right(node)
        print('Now tree')
        print(bst_)

    pdb.set_trace()




if __name__ == '__main__':
    # test_bst()
    more_bst_test()

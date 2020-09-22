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

    # for i in [dfs_pre, dfs_in, dfs_post]:
    #     i(bst)
    #     print()

    # print('Check find')
    # print(bst)
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

    print('\n\nPrev elem testing')
    for i in [72, 131, 21, 163, 111, 272]:
        a_node = B.md_find(bst_, i)
        print(f'found node: \n{a_node}\n')
        n_node = B.prev_elem(a_node)
        print(f'Prev node: \n{n_node}\n')

    pdb.set_trace()



if __name__ == '__main__':
    test_bst()

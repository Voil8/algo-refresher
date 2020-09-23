import bst as BST

def which_par(child):
    par = child.parent
    if par is None:
        return
    if child.key < par.key:
        return 'left'
    return 'right'

def rotate_right(x):
    par = x.parent

    y = x.left
    if y is None:
        return
    B = y.right

    wp = which_par(x)

    if wp == 'right':
        par.right = y
    elif wp == 'left':
        par.left = y

    y.parent = par

    y.right = x
    x.parent = y

    x.left = B
    if B is not None:
        B.parent = x

    return y

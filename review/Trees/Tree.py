def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)



def func_paths(t,n,end):
    paths = []
    if is_leaf(t) and label(t)(n) == end:
        return [[label(t)]]
    for b in branches(t):
        paths.extend([[label(t)]+path for path in func_paths(b,label(t)(n),end)])
    return paths

def lowest(t):
    def lowest_pair(t):
        if is_leaf(t):
            return (label(t),0)
        max_pair = max([lowest_pair(b) for b in branches(t)],key= lambda x:x[2])
        max_pair[1] += 1
        return max_pair
    return lowest_pair(t)[0]





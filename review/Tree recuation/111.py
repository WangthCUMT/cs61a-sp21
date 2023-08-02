def sum_larger(n,k):
    if n == 0 or k == 0:
        return 0
    else:
        a = n % 10 + sum_larger(n // 10, k-1)
        b = sum_larger(n//10, k)
        return max(a,b)

def collect_candy(grid,row,col):
    if row < 0 or col < 0:
        return 0
    a = grid[row][col] + collect_candy(grid,row-1, col)
    b = grid[row][col] + collect_candy(grid,row,col-1)
    return max(a,b)

def count_sequence(lst,seq):
    if seq == []:
        return 1
    elif lst == []:
        return 0
    elif lst[0] != seq[0]:
        return count_sequence(lst[1:],seq)
    else:
        with_first = count_sequence(lst[2:],seq[1:])
        without_first = count_sequence(lst[1:],seq)
        return without_first + with_first

def quick_sort(lst):
    if lst == [] or len(lst) == 1:
        return lst
    else:
        pivot = lst[0]
        left = quick_sort([i for i in lst if i < pivot])
        right = quick_sort([i for i in lst if i > pivot])
        return left + [pivot] + right

print(quick_sort([2,3,4,1,5,9]))
import random

# l is a list in ascending order, and target is something that we're looking for
# Return -1 if not found

# naive search: scan entire list and ask if its equal to the target
# if yes, return the index
# if no, then return -1

def naive_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# binary search uses divide and conquer! a fact that our list is SORTED

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    # If high is less than low, the search range is invalid (we've narrowed down to an empty range).
    # In this case, the target value is not in the list, so the function returns -1.    
    if high < low:
        return -1

    # example l = [1, 3, 5, 10, 12]  # should return 3
    midpoint = (low + high) // 2  # 2

    # we'll check if l[midpoint] == target, and if not, we can find out if
    # target will be to the left or right of midpoint
    # we know everything to the left of midpoint is smaller than the midpoint
    # and everything to the right is larger
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)

if __name__=='__main__':
    l = [1, 3, 5, 10, 12]
    # target = 7 wil return -1
    target = 10
    print(naive_search(l, target))
    print(binary_search(l, target))

def merge_sort(list):
    """
    sorts a list in ascending order. returns a new sorted list.
    divides: to find midpoint, then divides again into sublists
    conquer: recursively sorts the sublists created in previous list.
    combine: merge sorted sublists back into ordered list
    
    takes overall O(n log n) time complexity if you don't use the slice
    """
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

def split(list):
    '''
    divide unsorted list at midpoint into sublists, returns two sublists-left and right. runs in O(n) time but slice is k (much more expensive)
    '''
    #variables
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    
    return left, right

def merge(left, right):
    '''
    merges two lists, sorting them in the process. returns a new merged list. 
    '''
    l = []
    i = 0 #indexes at left list
    j = 0 #indexes at right list
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
            
        else:
            l.append(right[j])
            j += 1
            
            
    while i < len(left):
        l.append(left[i])
        i += 1 
        
    while j < len(right):
        l.append(right[j])
        j += 1
    return l
    

# alist = [54, 72, 12, 199]
# l = merge_sort(alist)
# print(l)

def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])

alist = [54, 72, 12, 199]
l = merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))

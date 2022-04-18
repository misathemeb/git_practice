
def linear_search(list, target):
    '''
    returns the index position of the target if found, else returns None
    '''
    
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")
        
numbers = [x for x in range(10)]

result = linear_search(numbers, 6)
verify(result)
           
    
        
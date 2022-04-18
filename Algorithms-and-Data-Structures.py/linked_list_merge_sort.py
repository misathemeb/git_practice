

from linked_lists import LinkedList

def merge_sort(linked_list):
    '''
    this fx sorts a linked list in ascending order
    -recursively divide the linked list into sublists containing a single node.
    -repeatedly merge sublists to produce sorted sublists until one remains
    -returns a sorted linked list *overall runs in O(kn log n)
    '''
    
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

def split(linked_list):
    '''
    divide unsorted list at midpoint into sublists. takes O(k log n)
    '''
    
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2
        
        mid_node = linked_list.node_at_index(mid-1)
        
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None
        
        return left_half, right_half
    
def merge(left, right):
    '''
    merges two linked lists, sorting by data in nodes
    returns a new merged list. runs in linear time O(n)
    '''
    #create a new linked list that contains nodes from merging left and right
    merged = LinkedList()
    
    #add a fake head that is discarded later
    merged.add(0)
    current = merged.head
    
    #obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head
    
    #iterate over left and right until we reach tail node of either
    while left_head or right_head:
        if left_head == None:
            current.next_node = right_head
            #call next on right to set loop condition to False
            right_head = right_head.next_node
        elif right_head == None:
            current.next_node = left_head
            #call next on left to set loop condition to False
            left_head = left_head.next_node
            
        else:
            left_data = left_head.data
            right_data = right_head.data
            #if data on left is < than right set current to left node.
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
                
            #if data on left > than right set current to left node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        #move current to next node
        current = current.next_node
        
        #discard fake head and set first merged node as head
        head = merged.head.next_node
        merged.head = head
        
        return merged
    
l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)

print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)
                
    
    
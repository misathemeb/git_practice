
new_list = [1, 2, 3]
result = new_list[0] #reference to base memory bc it is contiguous so access is a constant time operation

#linear search
if 1 in new_list: print(True)

for n in new_list:
    if n ==1:
        print(True)
        break
    
    
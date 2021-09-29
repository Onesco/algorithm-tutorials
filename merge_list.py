def merge_sort(the_list):
    
    if len(the_list) <=1:
        return the_list
    
    left, right = split(the_list)
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def split(the_list):
    
    mid = len(the_list)//2
    return the_list[:mid], the_list[mid:]

def merge( left, right):

    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i +=1
        else:
            l.append(right[j])
            j +=1

    while i < len(left):
        l.append(left[i])
        i +=1
    while j < len(right):
        l.append(right[j])
        j +=1
       
    return l



    

 
l =[1,10, 31, 14]

merge_sort(l)
def binary_search(value, integers_list):
    
    first = 0
    last = len(integers_list) - 1
    
    while first <= last:
        middle = (first + last) // 2
        
        if integers_list[middle] == value:
            return middle
        elif integers_list[middle] < value:
            first = middle + 1
        else: 
            last = middle - 1
        
    return {'error':'Valor não encontrado!'}
        
print(binary_search(42, [40, 41, 42, 43, 44, 46]))
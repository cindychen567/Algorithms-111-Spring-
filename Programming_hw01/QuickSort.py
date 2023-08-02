def qsort(x , type):
    if type == 0:
        p = 0
    else: p = 1
    
    n = len(x)
    if n < 2:
        return x
    
    pivot = x[n-1]
    i = -1
    j = 0
    while j < n-1:
        if x[j][p] < pivot[p]:
            i += 1
            x[i] , x[j] = x[j] , x[i]
        j += 1
    
    right = x[:i+1]
    left = x[i+1:j]
    arr = qsort(right , type) + [pivot] + qsort(left , type)
    return arr
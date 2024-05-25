def selection_sort(l):
    n=len(l)
    for i in range(n-1):
        min_idx=i
        for j in range(i+1,n):
            if l[min_idx]>l[j]:
                min_idx=j
        l[i],l[min_idx]=l[min_idx],l[i]
    return l
l=list(map(int,input().split()))
print(selection_sort(l))
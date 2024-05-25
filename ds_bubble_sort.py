def bubble_sort(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1-i): #we are reducing i as i elements are sorted and 
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
l=list(map(int,input().split()))
print(bubble_sort(l))
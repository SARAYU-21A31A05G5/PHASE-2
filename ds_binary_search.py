def binary_search(l,key):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]==key:
            return 1
        elif l[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return 0
l=list(map(int,input().split()))
l.sort()
key=int(input("Enter the element to be searched :"))
if binary_search(l,key):
    print(f"{key} is found successfully")
else:
    print(f"{key} is not found in the list")
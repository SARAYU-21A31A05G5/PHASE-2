def linear_search(l,target):
    for i in l:
        if i==target:
            return 1
    return -1
l=list(map(int,input().split()))
target=int(input("Enter the element to be searched:"))
result=linear_search(l,target)
if result==1:
    print(f"{target} is found")
else:
    print(f"{target} is not found")

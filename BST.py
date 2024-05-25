class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
class Bst:
    def __init__(self):
        self.root=None
    def insert(self,key):
        self.root=self._insert_recursive(self.root,key)
    def _insert_recursive(self,root,key):
        if root is None:
            return Node(key)
        if key<root.key:
            root.left=self._insert_recursive(root.left,key)
        elif key>root.key:
            root.right=self._insert_recursive(root.right,key)
        return root
    def delete(self,val):
        self.root=self._delete_recursive(self.root,val)
    def _delete_Recursive(self,node,value):

        if value<node.value:
            node.left=self._delete_recursive(node.left,value)
        elif value>node.value:
            node.right=self._delete_recursive(node.right,value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp=self._min_value_node(node.right)
            node.value=temp.value
            node.right=self._delete_recursive(node.right,temp.value)
        return node


    # def search(self,val):
    #     curr=self.root
    #     found=0
    #     while curr:
    #         if curr.key==val:
    #             found=True
    #             break
    #         elif val<curr.key:
    #             curr=curr.left
    #         elif val>curr.key:
    #             curr=curr.right
    #     if found:
    #         print(f"{val} is found successfully")
    #     else:
    #         print("Element is not in tree")
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.key,end=" /")
            self.inorder(root.right)
    def search(self,val):
        return self._search_recursive(self.root,val)
    def _search_recursive(self,node,val):
        if not node or node.key==val:
            return node
        if val<node.key:
            return self._search_recursive(node.left,val)
        return self._search_recursive(node.right,val)
    def height(self,root): #The **address of node from which the height must be measured is root
        if not root:
            return -1
        return 1+max(self.height(root.left),self.height(root.right))
    def level_max(self):
        temp,res=[],[]
        temp.append(self.root)
        while len(temp)>0:
            maxi=0
            for i in range(len(temp)):
                if temp[0].left is not None:
                    temp.append(temp[0].left)
                if temp[0].right is not None:
                    temp.append(temp[0].right)
                maxi=max(temp[0].key,maxi)
                temp.pop()
            res.append(maxi)
        print(res)
    def min(self):
        current=self.root
        while current.left:
            current=current.left
        return current.key
    def max(self):
        current=self.root
        while current.right:
            current=current.right
        return current.key
tree=Bst()
tree.insert(9)
tree.insert(8)
tree.insert(5)
tree.insert(11)
tree.insert(14)
tree.insert(12)
tree.inorder(tree.root)
print()
r=tree.search(20)
if r:
    print("Element found in tree")
else:
    print("No element in tree")
# tree.level_max()
print(f"The height of tree is :{tree.height(tree.root)}")
# print(tree.min())
# print(tree.max())
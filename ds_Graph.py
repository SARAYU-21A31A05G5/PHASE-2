class Graph:
    def __init__(self):
        self.graph={} #dictionary
    def addEdge(self,a,b):
        if a not in self.graph:
            self.graph[a]=[] #list in dictionary {a:[]}
            self.graph[a].append(b) #{a:[b]}
        else:
            self.graph[a].append(b)
    def transitive_closure(self,graph):
        v=len(graph)
        reach=[]
        for i in range(v):          #To create a copy(clone) of the graph matrix in form of reach
            row=[]
            for j in range(v):
                row.append(graph[i][j])
            reach.append(row)
        print("reach:",reach)
                    #OR
        # reach=[[graph[i][j] for j in range(v)]for i in range(v)]
        for k in range(v):
            for i in range(v):
                for j in range(v):
                    reach[i][j]=(reach[i][j] or reach[i][k] and reach[k][j])
        return reach
    def print_matrix(self,matrix):
        for row in matrix:
            print(''.join(map(str,row)))
        graph=[[1,1,0,1],
               [0,1,1,1],
               [0,0,1,0],
               [0,0,0,1]]
    r=transitive_closure(graph)
    print_matrix(r)
    print(r)
    def num_islands(grid):
        if not grid:
            return 0
        def dfs(grid,i,j):
            if(i<0 or i>=len(grid)or j>0 or j>=len(grid[0]) or grid[i][j]=='0'):
                return
            grid[i][j]='0'
            dfs(grid,i+1,j)
            dfs(grid,i-1,j)
            dfs(grid,i,j+1)
            dfs(grid,i,j-1)
        island_count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    dfs(grid,i,j)
                    island_count+=1
            return island_count
        grid=[['1','1','1','1'],
              ['1','1','0','0'],
              ['0','0','0','1'],
              ['0','1','0','1']]
        print(num_island(grid))
    def bfs(self):
        a=self.graph
        queue=[1] #As in the first place we are already there we put queue=1
        visited=set()
        visited.add(1)
        while queue:
            curr=queue.pop(0)
            print(curr)
            for i in a[curr]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
    def dfs(self):
        queue=[1] #just variabe name is queue but for dfs we use a stack in python we use lists
        visited=set()
        visited.add(1)
        while queue:
            curr=queue.pop()
            print(curr)
            for i in a[curr]:
                if i not in a:
                    queue.append(i)
                    visited.add(i)
obj=Graph()
n=int(input("enter the no.of edges :"))
for i in range(n):
    a,b=map(int,input().split())
    obj.addEdge(a,b)   #or obj.addEdge(int(input()),int(input()))
print(obj.graph)  #{1: [2, 3], 2: [1, 4], 3: [1, 7], 4: [2], 7: [3]} Refer diagram in notes     #this is of form 1 have edge with 2 and 3. 2 have edge with 1 and 4. 3 have edge with 1 and 7
obj.bfs()
obj.dfs()
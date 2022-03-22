#!/usr/bin/env python
# coding: utf-8

# In[159]:


'''
General Idea:
    determine whether clicked a mine
    if yes, done.
    if not, search all the neighbour grids of the click and obtain the number of neighbouring mines
    repeat the searching step above for all the safe neighbours
'''

class Coordinate:
    
    def __init__(self, r, c, n, m): # n is num of rows, m is num of cols, 1<=r<=n, 1<=c<=m
        self.r = int(r)
        self.c = int(c)
        self.n = int(n)
        self.m = int(m)
        
    def neighbours(self):
        neighbours  = []
        if (self.r-1) >= 1:
            neighbours.append(Coordinate(self.r-1,self.c,self.n,self.m))
            if (self.c-1) >= 1:
                neighbours.append(Coordinate(self.r-1,self.c-1,self.n,self.m))
            if (self.c+1) <= self.m:
                neighbours.append(Coordinate(self.r-1,self.c+1,self.n,self.m))
        if (self.c-1) >= 1:
            neighbours.append(Coordinate(self.r,self.c-1,self.n,self.m))
        if (self.r+1) <= self.n:
            neighbours.append(Coordinate(self.r+1,self.c,self.n,self.m))
            if (self.c-1) >= 1:
                neighbours.append(Coordinate(self.r+1,self.c-1,self.n,self.m))
            if (self.c+1) <= self.m:
                neighbours.append(Coordinate(self.r+1,self.c+1,self.n,self.m))
        if (self.c+1) <= self.m:
            neighbours.append(Coordinate(self.r,self.c+1,self.n,self.m))
        return neighbours
    
def read():
    mines = []
    n, m, k = input().split()
    n = int(n)
    m = int(m)
    k = int(k)

    i = 0
    while i < k:
        s = input()
        if s != "":
            temp = [i for i in s.split()]
            mine = Coordinate(temp[0],temp[1],n,m)
            mines.append(mine)
            i += 1
        else:
            break
    s = input()
    temp = [i for i in s.split()]
    target = Coordinate(temp[0],temp[1],n,m)
        
    return n, m, k, mines, target

visited_coordinates = {}
mine_coordinates = set()
unvisited_neighbours = []



def visit(n,m,k,mines,target): #check whethere there are mine neighbours, if so, where are they 

    global visited_coordinates
    global mine_coordinates
    global unvisited_neighbours 
    
#     print("unvisited neighbours:")
#     for i in unvisited_neighbours:
#         print((i.r,i.c))
#     print("now visiting {}".format((target.r,target.c)))
    
    count = 0
    for neighbour in target.neighbours(): # check all the neighbours one by one
#         print("checking neighbour: {}".format((neighbour.r,neighbour.c)))
        for mine in mines: # determine whether there is a mine here
            if (neighbour.r,neighbour.c) == (mine.r,mine.c): # found a mine neighbour
                mine_coordinates.add((neighbour.r,neighbour.c)) # mines already scanned
#                 print('found a mine here!!!')
                count += 1
#     print("finished visiting {}".format((target.r,target.c)))
#     print("count is {}".format(count))
    
#     print("visited_coordinates before appending: {}".format(visited_coordinates))
    unvisited_neighbours.remove(target) # finished visiting, remove from unvisited list
    visited_coordinates[(target.r,target.c)] = count # mark the coordinate as visited
#     print("visited_coordinates after appending: {}".format(visited_coordinates))
    return count


def main():
    n, m, k, mines, target = read()
    for mine in mines:
        count = 0
        
        if (mine.r,mine.c) == (target.r,target.c):
            for row in range(1,n+1):
                for col in range(1,m+1):
                    if (row,col) != (mine.r,mine.c):
                        print("#", end = "")
                    else:
                        print("*", end = "")
                print("\n", end="")
        
            return 0 # finished program
            
 
    unvisited_neighbours.append(target)
    while len(unvisited_neighbours) != 0:

        temp = unvisited_neighbours[0]
        count = visit(n,m,k,mines,unvisited_neighbours[0])

#         print("visited_coordinates keys {}".format(visited_coordinates.keys()))
        if count == 0:
            for neighbour in temp.neighbours(): # determine where to visit 
#                 print("current neighbout {}".format((neighbour.r,neighbour.c)))

                if (neighbour.r,neighbour.c) not in visited_coordinates.keys(): 
                    if (neighbour.r,neighbour.c) not in mine_coordinates:
                        ## this neighbour should not have already been in the list
                        flag = 1
                        for element in unvisited_neighbours:
                            if (element.r,element.c) == (neighbour.r,neighbour.c):
                                flag = 0
                        if flag == 1:
#                             print('appended!!!')
                            unvisited_neighbours.append(neighbour)
                            
    for row in range(1,n+1):
        for col in range(1,m+1):
            if (row,col) in visited_coordinates.keys():
                if visited_coordinates[(row,col)] == 0:
                    print(".", end="")
                else:
                    print("{}".format(visited_coordinates[(row,col)]), end="")
            
            else:
                print("#", end="")
                
        print("\n", end="")
    
    return 0


# In[160]:


main()


# 

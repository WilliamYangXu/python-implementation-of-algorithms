#!/usr/bin/env python
# coding: utf-8

# In[162]:


'''     
General Idea: 

    among all reachable rooms, are there any belonging to rooms with switches
        if so, do theres switches rooms belong to neighbours to any reachable rooms
          if yes, then all such swich rooms the reachable rooms
              expand reachable rooms
          if no, break
        if no, break
    end
    
        
    start from (1,1),determine whether pointers area connected
    expand the group
    continue until no more pointers area are connected
'''

class Grid:
    
    def __init__(self, x, y, N): # 2<=N<=100, 1<=x<=N, 1<=y<=N
        self.x = int(x)
        self.y = int(y)
        self.N = int(N)
        
    def neighbours(self):
        neighbours  = []
        if self.x != 1:
            neighbours.append(Grid(self.x-1,self.y,N))
        if self.y != 1:
            neighbours.append(Grid(self.x,self.y-1,N))
        if self.x != self.N:
            neighbours.append(Grid(self.x+1,self.y,N))
        if self.y != self.N:
            neighbours.append(Grid(self.x,self.y+1,N))
        return neighbours
    

class Room(grid):
    
    def __init__(self, x1, y1, x2, y2, N):
        super().__init__(int(x1), int(y1), int(N))
        self.switch = Grid(int(x2), int(y2), int(N))



def read():
    rooms_with_switches = []
    N, M = input().split()
    N = int(N)
    M = int(M)

    n = 0
    while n < M:
        s = input()
        if s != "":
            temp = [i for i in s.split()]
            room = Room(temp[0],temp[1],temp[2],temp[3],N)
            rooms_with_switches.append(room)
            n = n + 1
        else:
            break
    return N, M, rooms_with_switches


def main():
    
    N, M, rooms_with_switches = read() # obtain all the lit rooms with corresponding pointers
    reachable_rooms = [Grid(1,1,N)] # initialize all reached rooms starting from (1,1)
    neighbours_of_reachable_rooms = {Grid(1,1,N)} 
    
    while True:

            expanded = 0
            for reached_room in reachable_rooms:
                for neighbour in reached_room.neighbours():
                    neighbours_of_reachable_rooms.add(neighbour)

            for reached_room in reachable_rooms:
                for room in rooms_with_switches:
                    if reached_room.x == room.x and reached_room.y == room.y: # found a  

                        for element in neighbours_of_reachable_rooms:
                            if room.switch.x == element.x and room.switch.y == element.y:
                                expand = 1
                        for element in reachable_rooms:
                            if room.switch.x == element.x and room.switch.y == element.y:
                                expand = 0
                        if expand == 1: 

                            reachable_rooms.append(room.switch)
                            expanded = 1

            if expanded == 0:
                break
                
    print (len(reachable_rooms))


# In[161]:


main()


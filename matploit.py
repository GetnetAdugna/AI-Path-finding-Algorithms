import matplotlib.pyplot as plt
import numpy as np
from Graph import *
from Evaluation import *
import random
import string
chars = string.ascii_letters + string.punctuation
size = 10
x=20

time_for_bfs=0
astar_len=0
dij_len=0
dfs_len=0
bfs_len=0

time_for_dij=0
time_for_ast=0
time_for_dfs=0
Atarr=[]
Djtarr=[]
Dtarr=[]


Btarr=[]
Alarr=[]
Dlarr=[]
Djlarr=[]

Blarr=[]


def string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))
Random_Nodes_List=[]
Random_Nodes_List.extend(Nodes_list)
list_he=[]

# if we want to change the number of nodes that are needed to be generated we can change the value of n
# minimum value of x must be of 100
def Random_Node_Gene(x,Node_List):
    while(len(Node_List)<(x+20)):
        val=Node(string_generator(size,chars))
        g.addNode(val)
        Node_List.append(val)
def Random_Edge_Gene(Nodes_list,x):
    for elements in Nodes_list:
        for i in range( random.randint (random.randint(0,2), random.randint(2,4) ) ):
            m=random.randint(0,100)
            g.addEdge(elements,Nodes_list[i],m)

def Write_on_Text():
    for keys in g.adjacencyList:
            if keys not in list_he:
                list_he.append(keys)
    with  open("Random_Heur.txt", "w") as file:
            file.write('\n'.join(list_he))
            file.close()







for i in range(4):
    Random_Node_Gene(x*(i),Random_Nodes_List)
    Random_Edge_Gene(Random_Nodes_List,x)
    Write_on_Text()
    
    time_for_ast=timeTest_two_args(g.A_star,time_for_ast,Random_Nodes_List)
    Atarr.append(time_for_ast)
    time_for_bfs=timeTest_two_args(g.BFS,time_for_bfs,Random_Nodes_List)
    Btarr.append(time_for_bfs)
    time_for_dfs=timeTest_two_args(g.DFS,time_for_dfs,Random_Nodes_List)
    Dtarr.append(time_for_dfs)
    time_for_dij=timeTest_two_args(g.Dijkstra,time_for_dij,Random_Nodes_List)
    Djtarr.append(time_for_dij) 
    astar_len=len_test(g.A_star,astar_len,Random_Nodes_List)
    Alarr.append(astar_len)
    dij_len=len_test(g.Dijkstra,dij_len,Random_Nodes_List)
    Djlarr.append(dij_len)
    bfs_len=len_test(g.BFS,bfs_len,Random_Nodes_List)  
    Blarr.append(bfs_len)
    dfs_len=len_test(g.DFS,dfs_len,Random_Nodes_List)
    Dlarr.append(dfs_len)




print("-----------------------------Time--------------------------------")
print('--------A*---------------------------')
print(time_for_ast)
print("---------------------bfs---------------------------")
print(time_for_bfs)
print("-------------------------------dije-----------")
print(time_for_dij)
print("--------------------Length----------------------------")
print('--------A*---------------------------')
print(astar_len)
print("---------------------bfs---------------------------")
print(bfs_len)
print("-------------------------------dije-----------")
print(dij_len)




print(Atarr)
print(Btarr)
print(Dtarr)

xpoints=np.array(Atarr)
x2points=np.array(Djtarr)
x3points=np.array(Btarr)
X9points=np.array(Dtarr)
yval=[]
# yval=[2,4]
for i in range(4):
 yval.append(20*(i+1))
ypoints=np.array(yval)
plt.plot(ypoints,xpoints,label="A*")
plt.plot(ypoints,x2points,label="DFS")
plt.plot(ypoints,x3points,label="BFS")

plt.plot(ypoints,X9points,label="Dijkstra")

# plt.plot([2,3,4,4],[4,56,7],label="dfs")
plt.xlabel("Nodes computed")
plt.ylabel(" Time in Second")
plt.title("Average time shower")
leg = plt.legend(loc='upper center')
plt.show()

xmpoints=np.array(Alarr)
x4points=np.array(Djlarr)
x5points=np.array(Blarr)
x6points=np.array(Dlarr)
# for i in range(10):
#     yval.append(2*(i+1))
# ypoints=np.array(yval)
plt.plot(ypoints,xmpoints,label="A*")
plt.plot(ypoints,x4points,label="Dijkstra")
plt.plot(ypoints,x5points,label="BFS")
plt.plot(ypoints,x6points,label="DFS")

# plt.plot([2,3,4,4],[4,56,7],label="dfs")
plt.xlabel("Nodes computed")
plt.ylabel(" length in Number of nodes")
plt.title("Average lENGTH shower")
leg = plt.legend(loc='upper center')
plt.show()






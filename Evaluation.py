from platform import node
from Graph import *
import time

val_holder=[]
g=Graph()
st_name=[]
Nodes_list=[]
time_list=[]
time_spent=0
len_list=[]
astar_time=0
dij_time=0
bfs_time=0
dfs_time=0
astar_len=0
dij_len=0
bfs_len=0
dfs_len=0
def Create_Node():
        with open("city connection.txt",'r') as data_file:
            for line in data_file:
                data = line.split(",")
                val_holder.append(data)
        
        for i in range(len(val_holder)):
            for j in range(len(val_holder[i])-1):
                if(val_holder[i][j] not in st_name):
                    st_name.append(val_holder[i][j])
        for i in range(len(st_name)):
            Node_1=Node(st_name[i])
            g.addNode(Node_1)

           
            Nodes_list.append(Node_1)
            
        for i  in range(len(val_holder)):
            for j in range(len(val_holder[i])-2):
                if(val_holder[i][j] in st_name and val_holder[i][j+1] in st_name):
                    for k in range(len(Nodes_list)):
                        if (val_holder[i][j]==Nodes_list[k].Val):
                            for m in range(len(Nodes_list)):
                                if(val_holder[i][j+1]==Nodes_list[m].Val):
                                    g.addEdge(Nodes_list[k],Nodes_list[m],int(val_holder[i][j+2].replace("/n",'')))


def timeTest_two_args(fun,time_spent,Nodes_li):
    for i in range(len(Nodes_li)):
        for j in range(len(Nodes_li)):
            if(Nodes_li[i]!=Nodes_li[j]):
                t1=time.time() 
                fun(Nodes_li[i],Nodes_li[j])
               
                t2=time.time()
                # print(fun(Nodes_list[i],Nodes_list[j]))
                time_list.append({'from':Nodes_li[i].Val,'to':Nodes_li[j].Val,'time':t2-t1})
                time_spent=time_spent+(t2-t1)
    print("me---------------------------------------------")
    print(time_list)
    return time_spent/len(time_list)
def len_test(fun,lengt,Nodes_list):
    for i in range(len(Nodes_list)):
        for j in range(len(Nodes_list)):
            if(Nodes_list[i]!=Nodes_list[j]):
                leng=fun(Nodes_list[i],Nodes_list[j])
                lengt=lengt+len(leng)
              
  
    
    return lengt/((len(Nodes_list)*len(Nodes_list)-20))
                
       
Create_Node()


astar_time=timeTest_two_args(g.A_star,astar_time,Nodes_list)

bfs_time=timeTest_two_args(g.BFS,bfs_time,Nodes_list)

dij_time=timeTest_two_args(g.Dijkstra,dij_time,Nodes_list)
dfs_time=timeTest_two_args(g.DFS,dfs_time,Nodes_list)

astar_len=len_test(g.A_star,astar_len,Nodes_list)

bfs_len=len_test(g.BFS,bfs_len,Nodes_list)

dij_len=len_test(g.Dijkstra,dij_len,Nodes_list)
dfs_len=len_test(g.DFS,dfs_len,Nodes_list)


print("-----------------------TIME-------------------------")
print("----------------------Astar time-------------------")
print(astar_time)
print("----------------------Dijkstra time-------------------")

print(dij_time)
print("--------------------BFS time-------------------")

print(bfs_time)
print("--------------------DFS time-------------------")

print(dfs_time)

print("----------------------LENGHT-------------------")
print("-----------------------------Astar length-----------------")

print(astar_len)
print("-----------------------------Dijkstra length-----------------")

print(dij_len)
print("-----------------------------BFS length-----------------")

print(bfs_len)
print("-----------------------------DFS length-----------------")

print(dfs_len)









import math

import numpy as np
import random


list_l=[]
val_holder=[]

Heriusti_list=[]
new_val=[]
Heriustic = {}


def get_huristic_value(location_one,location_two):
    RADIUS=6373.0
    latitude_one = math.radians(location_one[0])
    longitude_one = math.radians(location_one[1])
    latitude_two = math.radians(location_two[0])
    longitude_two = math.radians(location_two[1])

    diffrence_in_longitude = longitude_two-longitude_one
    diffrence_in_latitude = latitude_two -latitude_one

    a = math.pow((math.sin(diffrence_in_latitude/2)),2) + math.cos(latitude_one)*math.cos(latitude_two)*math.pow((math.sin(diffrence_in_longitude/2)),2)
    c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))

    distance_between = RADIUS * c
    return distance_between

with open("city_lati_long.txt",'r') as data_file:
        for line in data_file:
            data = line.split(",")
            val_holder.append(data)
for i in range(len(val_holder)):
        Heriusti_list.append([val_holder[i][0],(float(val_holder[i][1].replace(" ",''))-float(val_holder[i][2].replace("\n",'')))])  
                
for i in range(len(Heriusti_list)):
        Heriustic [Heriusti_list[i][0]]=Heriusti_list[i][1]

class priorityQueue():
     
      def __init__(self):
          self.values=[]
      def enqueue(self,val,priority):
          self.values.append({'value':val,'priority':priority})
          self.sort()
      def dequeue(self):
          return self.values.pop(0)

      def sort(self):
         self.values=sorted(self.values,key=lambda x:x['priority'])
class Node():
    def __init__(self,val):
        self.Val=val;
    


class Graph:
    def __init__(self):
        self.adjacencyList={}
        self.val=None
        # self.weight={}
    def addNode(self,Node):
            if not(Node.Val in self.adjacencyList):
                 self.adjacencyList[Node.Val]=[]
    def addEdge(self,v1,v2,weight=0,val='u'):
        self.val=val
        if(self.val.lower()=='u'):
            self.adjacencyList[v1.Val].append({'node':v2.Val,'weight':weight}) 
            self.adjacencyList[v2.Val].append({'node':v1.Val,'weight':weight})
        elif(self.val.lower()=='d'):      
            self.adjacencyList[v1.Val].append({'node':v2.Val,'weight':weight})
    def h(self, n):
        if n in Heriustic:
          
            return Heriustic[n]
        else:
          
            return random.randint(1,15)
 
   
    def isEdge(self,node1,node2):
        co_new=self.adjacencyList[node2]
        NodeHolder=[]
        if(len(co_new)!=0):
           for i in range(len(co_new)):
               NodeHolder.append(co_new[i]['node'])
           if(node1 in NodeHolder):
               return 1;     
                
           else:
            return 0;
        return 0;
    def DFS(self,start,end):
       stack=[start.Val]
       result=[]
       visited={}
       current_vertex=0
       visited[start.Val]=True
       while(len(stack)>0):
           current_vertex=stack.pop()
           result.append(current_vertex)
           if current_vertex==end.Val:
               break
     
           print(self.adjacencyList[current_vertex])
           for neigh in self.adjacencyList[current_vertex]:
               print(neigh['node'])
               print("----------------")
               if not (neigh['node'] in visited):
                   stack.append(neigh['node'])
                   visited[neigh['node']]=True
  
       return result
    def BFS(self,start,end):
        queue=[start.Val];
        result=[];
        visited={};
        current_vertex=0;
        visited[start.Val]=True
        while(len(queue)):
            current_vertex=queue.pop(0)
            result.append(current_vertex)
            if current_vertex==end.Val:
                break
           
            for elements in self.adjacencyList[current_vertex]:
                if(not (elements['node']in visited)):
                    visited[elements['node']]=True
                    queue.append(elements['node'])
        return result
    def Adjacency_matrix_represenataion(self,graph):
        for elements in graph.adjacencyList:
          
            for elem in graph.adjacencyList:
                list_l.append(graph.isEdge(elements,elem));
                if(graph.isEdge(elements,elem)==1 and graph.isEdge(elem,elements)==1):
                    print(f' {elements} <=> {elem}',graph.isEdge(elements,elem))
                else:
                    print(f' {elements} => {elem}',graph.isEdge(elements,elem))
    
        print(graph.adjacencyList)
        print(list_l)
        val=np.reshape(list_l,(len(graph.adjacencyList),len(graph.adjacencyList)))
        print(val)
    
    def Dijkstra(self,start,finish): 
        nodes=priorityQueue()
        distances={}
        previous={}
        smallest=0
        path_val=[]
        reversed_path_val=[]
        for vertex in self.adjacencyList:
            if vertex==start.Val: 
                distances[vertex]=0;
                nodes.enqueue(vertex,0)
            else:
                distances[vertex]=float('inf')
                nodes.enqueue(vertex,float('inf'))
            previous[vertex]=None
        while(len(nodes.values)):
            smallest=nodes.dequeue()['value']
            if(smallest==finish.Val):
                while(previous[smallest]):   
                    path_val.append(smallest)
                    smallest=previous[smallest]
                break
            if(smallest or distances[smallest]!=float('inf')):
                for neigbor in range (len(self.adjacencyList[smallest])):
                    nextNode=self.adjacencyList[smallest][neigbor]
                    neig_cand=distances[smallest]+nextNode['weight']
                    next_neig=nextNode['node']
                    if(neig_cand<distances[next_neig]):
                        distances[next_neig]=neig_cand
                        previous[next_neig]=smallest;
                        nodes.enqueue(next_neig,neig_cand)
        for i in range(len(path_val)): 
            reversed_path_val.insert(0,path_val[i])
        reversed_path_val.insert(0,start.Val)    
        return reversed_path_val
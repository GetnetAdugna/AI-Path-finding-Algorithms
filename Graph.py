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
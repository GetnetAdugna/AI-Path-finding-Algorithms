# a module to test the graph by creating different nodes and edge connections
# an example is given using A B C D E AND F


from Graph import *  
g=Graph()     
A=Node('A') 

B=Node('B') 
C=Node('C') 
D=Node('D') 
E=Node('E') 
F=Node('F') 

g.addNode(A)



g.addNode(B)
g.addNode(C)
g.addNode(D)
g.addNode(E)
g.addNode(F)



g.addEdge(A,B, 4);
g.addEdge(A,C, 2);
g.addEdge(B,E, 3);
g.addEdge(C,D, 2);
g.addEdge(C,F, 4);
g.addEdge(D,E, 3);
g.addEdge(D,F, 1);
g.addEdge(E,F, 1);


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 14:19:46 2022

@author: juliennakache
"""

import networkx as nx
import csv
import matplotlib.pyplot as plt
import numpy as np

#Import the file
mydata = csv.reader( open(r"/Users/juliennakache/Desktop/red4_adjacency.csv", "r"), delimiter =",")
mydata
Red = np.genfromtxt(open(r"/Users/juliennakache/Desktop/red4_adjacency.csv", "r"), delimiter=",")

Graph1 = nx.Graph()
#Adding the nodes to the graph

n = len(Red)
for i in range(n):
    Graph1.add_node(i)
    for j in range(i,n):
        if Red[i][j] == 1:
            Graph1.add_edge(i,j)
            
plt.figure()
nx.draw(Graph1)
plt.show()
        
#Pregunta 2 : Numero de nodos
print("Pregunta 2 : La red 1 tiene ", len(Graph1.nodes()), " nodos")

#Pregunta 3 : Numero de enlaces
print("Pregunta 3 : La red 1 tiene ",len(Graph1.edges()), " enlaces")

#Pregunta 4 : Grado medio
degrees=[]
s=0
for n in Graph1.nodes():
    a=Graph1.degree(n)
    degrees.append(a)
    s=s+a
Av_degree = s/len(degrees)
print("Pregunta 4 : El grado medio de la red 1 es ",round(Av_degree, 4))

#Pregunta 5 : Import the other file

Graph2 = nx.read_edgelist("/Users/juliennakache/Desktop/red3.txt",create_using=nx.Graph(), nodetype = int)
plt.figure()
nx.draw(Graph2)
plt.show()
#Pregunta 6 : Numero de nodos
print("Pregunta 6 : La red 2 tiene ",len(Graph2.nodes()), " nodos")
#Pregunta 7 : Numero de enlaces
print("Pregunta 7 : La red 2 tiene ", len(Graph2.edges()), " enlaces")

#Pregunta 8 : Gradio Medio
A=dict(Graph2.degree())
b=len(Graph2.nodes())
Av_deg =sum(A.values())/b #Otra metoda que en la pregunta 4
print("Pregunta 8 : El grado medio de la red 2 es ",round(Av_deg, 4))

#Pregunta 9 : Densidad de la red 
Dens=nx.density(Graph2)
print ("Pregunta 9 : La densidad de la red 2 es ", round(Dens, 4))

#Pregunta 10 : Distancia Media
print("Pregunta 10 : La distancia media de la red 2 es ",nx.average_shortest_path_length(Graph2))

#Pregunta 11 : Number of components 
Comp = nx.number_connected_components(Graph2)
print("Pregunta 11 : El nombre de componentes de la red 2 es ",Comp)

#Pregunta 12 : Clustering
Clus = nx.clustering(Graph2) #Creando el dictionnary con las valores de clustering
Clusrounded = dict()
for key in Clus: #Redondeando las valores y poniendolas en un nuevo dict
    Clusrounded[key]=round(Clus[key],4)
print("Pregunta 12 : Aqui son las valores de Clustering de todo los nodos: ", Clusrounded)

#Pregunta 13 : Max Clustering
nodes=set()
Max_Clus = max(list(Clus.values())) #Tomando la mayor valor de Clustering (no redondea)
for k, v in Clus.items(): #Mirando a todos los nodos para ver si tienen la mayor valor de clustering
    if v ==Max_Clus:
        nodes.add(k) #Si un nodo tiene esta valor, lo añado a mi lista
print("Pregunta 13 : Los nodos con la mayor valor de Clustering que es ", Max_Clus, " son los nodos ", nodes)
        
#Pregunta 14 : Distribucion de grado de la red
def plot_degree_dist(G):
    degrees = [G.degree(n) for n in G.nodes()] #creando la lista de grados de los nodos
    plt.hist(degrees)
    plt.show()

plot_degree_dist(Graph2)

#Pregunta 15 : G(n,m) random graph
Graphnm=nx.dense_gnm_random_graph(50,100)
plt.figure()
nx.draw(Graphnm)
plt.show()

#Pregunta 16 : G(n,p) random graph y sus enlaces
Graphnp = nx.fast_gnp_random_graph(50, 0.25)
plt.figure()
nx.draw(Graphnp)
plt.show()
print("Pregunta 16 : Este G(n,p) red tiene ", len(list(Graphnp.edges())), "enlaces")

#Pregunta 17 : Barabasi-Albert Graph y su grado medio
GraphBA= nx.barabasi_albert_graph(50,3)
plt.figure()
nx.draw(Graphnp)
plt.show()
A=dict(GraphBA.degree())
b=len(GraphBA.nodes())
Av_deg =sum(A.values())/b #Misma metoda que en la pregunta 4
print("Pregunta 17 : El grado medio de la red BA es ",round(Av_deg, 4))

#Pregunta 18 : Grado Medio theorico
print( "Pregunta 18 : El grado medio theorico de este red seria 2m (6)")

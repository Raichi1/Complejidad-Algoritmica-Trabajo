import osmnx as ox
import networkx as nx
import pandas as pd
import numpy as np
import openpyxl
'''
DS = pd.read_csv('Datasets_csv.csv', index_col=None)
Datos=[]
for e in range(len(DS)):
    Datos.append(DS['Distrito'][e]+', Perú')
    print(Datos[e])

print(type(Datos[0]))
'''
#Grafico = ox.graph_from_place(Datos, network_type="drive")
#fig, ax = ox.plot_graph(Grafico, node_color="r") 

place_name = ['San Luis, Lima, Perú', 'San Borja, Lima, Perú', 'La Victoria, Lima, Perú'] 
# //Información de los distritos(nodos y aristas)
graph = ox.graph_from_place(place_name, network_type="drive")
#for e in graph.edges():
    #print(e)
#for e in graph.nodes():
    #print(type(e))
#nodes, edges = ox.graph_to_gdfs(graph)  //obtención de datos de los nodos y aristas
#//edges = pd.read_excel("aristas_distritos.xlsx")
#//nodes = pd.read_excel("nodos_distritos.xlsx")
auxiliar = pd.read_csv("auxiliar.csv")
nulo=auxiliar.at[3, "u"]
auxiliar= auxiliar.drop(columns= ['Unnamed: 0'])
for i in auxiliar:
    print(i)

print(auxiliar)
#print(edges.loc[:,["u","v"]])
 #aux = pd.DataFrame(data=edges)
 #print(type(aux))
#print(type(nulo))
#for i in range(len(aux)):
#    if aux.at[i,"u"] == np.NaN:
#        print("Hola")
#        ax = aux.at[i-1, "u"]
#        aux.at[i, "u"] = ax

#print(aux)

#aux = float(edges.iloc[0]["geometry"])
#def validar(dataframe_arcos):
#    for 
'''
def nose(fila):
    for e in nodes[0]:
        if 
for i in edges[:2]:
    nose(edges[i])
'''
#print(edges[edges['u']])
'''
for i in nodes.columns:
    print(nodes[i].tolist())

for i in nodes.columns:
    print(nodes[i].values)
    '''
#nodes.to_excel('C:/Users/HP/Downloads/DATABASE/nodos_distritos.xlsx', sheet_name = 'pag', engine = 'openpyxl')
#edges.to_excel('C:/Users/HP/Downloads/DATABASE/aristas_distritos.xlsx', sheet_name = 'pag', engine = 'openpyxl')
'''
for e in range(len(nodes)):
    for i in nodes:
        print(nodes[i][e],end='-')
    print('')
'''
#ox.io.save_graph_shapefile(graph, filepath=None, encoding='UTF-8') //Descarga de nodos y aristas para obtener gráfica
#fig, ax = ox.plot_graph(graph, node_color="r") //Mapa con los nodos y aristas

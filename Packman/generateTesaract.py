import itertools
import numpy as np

def generateVertextTesaract(n=2,m=2,p=2,r=2):
    vertex=[]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                for l in range(r):
                    x=-30*i
                    y=-30*j
                    z=-30*k
                    w=-30*l
                    vertex.append((x,y,z,w))
    return vertex


def generateIndexTesaract(vertices):
    edges = []
    num_vertices = len(vertices)

    for pair in itertools.combinations(range(num_vertices), 2):
        point1=np.array(vertices[pair[0]])
        point2=np.array(vertices[pair[1]])
        vector=point2-point1
        vectorNorm=vector/np.linalg.norm(vector)
        if (np.array_equal(vectorNorm, np.array([-1, 0, 0, 0])) or
                np.array_equal(vectorNorm, np.array([1, 0, 0, 0])) or
                np.array_equal(vectorNorm, np.array([0, -1, 0, 0])) or
                np.array_equal(vectorNorm, np.array([0, 1, 0, 0])) or
                np.array_equal(vectorNorm, np.array([0, 0, -1, 0])) or
                np.array_equal(vectorNorm, np.array([0, 0, 1, 0])) or
                np.array_equal(vectorNorm, np.array([0, 0, 0, -1])) or
                np.array_equal(vectorNorm, np.array([0, 0, 0, 1]))):
            edges.append(pair)

    return edges

def genreateTesaract(n,m,p,r):
    vertex=generateVertextTesaract(n,m,p,r)
    edges=generateIndexTesaract(vertex)
    return [vertex, edges]
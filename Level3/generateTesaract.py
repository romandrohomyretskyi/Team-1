import itertools
import numpy as np

def generateVertextTesaract(n):
    vertex=[]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
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

def genreateTesaract(n):
    vertex=generateVertextTesaract(n)
    edges=generateIndexTesaract(vertex)
    return [vertex, edges]
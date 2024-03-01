from RoadSystem import*
from ObjectGame import*
from numpy import array
from Road import*

class Map:
    __points=[]

    def __init__(self,vertexes,indexes,step,position,size):
        self.position=position
        self.size=size
        self.step=step
        self.__vertexes=array(vertexes)
        self.__indexes=array(indexes)
        self.__init()

    def __generateVertexRoad(self,index,i):
        return Vec4(self.position[0]+self.__vertexes[index[i]][0],self.position[1]+self.__vertexes[index[i]][1],
                    self.position[2]+self.__vertexes[index[i]][2],self.position[3]+self.__vertexes[index[i]][3])
    def __generateRoad(self,index):
        road=Road(start=self.__generateVertexRoad(index,0),
                  end=self.__generateVertexRoad(index,1))
        self.__points.extend(road.draw(self.size,self.step))
        return road
    def __init(self):
        self.arrayRoad=list(map(self.__generateRoad,self.__indexes))
        self.__road=RoadSystem(self.arrayRoad,self.step)

    def ifIsInRoad(self,object,then):
        self.__road.ifIsInRoad(object,then)

    def update(self,camera):
        for point in self.__points:
            point.update(camera)
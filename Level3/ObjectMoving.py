from ObjectGame import*
from ursina import Vec4
from numpy import array

class ObjectMoving(ObjectGame):
    __currentStrategyMove=None

    def __init__(self,position,size,entity,road):
        super().__init__(position,size,entity)
        self.__road=road
        self.step=road.step

    def changeVectorMove(self,vector):
        self.__currentStrategyMove=vector

    def translate(self,x,y,z,w):
        self.position=Vec4(self.position[0]+x,self.position[1]+y,self.position[2]+z,self.position[3]+w)
    def __clearCurrentStrategyMove(self,can):
        if(self.__currentStrategyMove not in can):
            self.__currentStrategyMove=None

    def stopVectorsMove(self):
        self.__road.ifIsInRoad(self, self.__clearCurrentStrategyMove)

    def move(self):
        if(self.__currentStrategyMove):
            self.__currentStrategyMove.move(self)
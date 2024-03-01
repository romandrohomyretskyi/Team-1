from ursina import Vec4
from StrategyMove import*
from Road import*

class RoadSystem:
    def __init__(self,arrayRoad,step):
        self.__arrayRoad=arrayRoad
        self.step=step
        for road in self.__arrayRoad:
            road.start*=step
            road.end*=step

    def __arrayCan(self,vector):
        if vector==Vec4(1,0,0,0) or vector==Vec4(-1,0,0,0):
            return [MoveLeft,MoveRight]
        if vector==Vec4(0,1,0,0) or vector==Vec4(0,-1,0,0):
            return [MoveTop,MoveDown]
        if vector==Vec4(0,0,1,0) or vector==Vec4(0,0,-1,0):
            return [MoveBackward,MoveForward]
        if vector==Vec4(0,0,0,1) or vector==Vec4(0,0,0,-1):
            return [MoveW1,MoveW2]
        return [0,1]


    def ifIsInRoad(self,object,then):
        can=[]
        for road in self.__arrayRoad:
            canMove=self.__arrayCan(road.getDirectionVector())
            if (road.isInRoad(object)):
                if(road.isInVertex(object,road.start)):
                    can.append(canMove[1])
                elif(road.isInVertex(object,road.end)):
                    can.append(canMove[0])
                else:
                    can.extend(canMove)
        then(can)
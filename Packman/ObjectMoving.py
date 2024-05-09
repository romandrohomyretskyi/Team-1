from Packman.ObjectGame import*
from ursina import Vec4,DirectionalLight,PointLight

class ObjectMoving(ObjectGame):

    def __init__(self,position,size,entity,road):
        super().__init__(position,size,entity)
        self.__road=road
        self.step=road.step
        self.__currentStrategyMove=None
        self.entity.shader="unlit"
        DirectionalLight(parent=self.entity, color=Vec4(0.7,0.7,0.7,1))
        PointLight(parent=self.entity, color=entity.color)
        self.entity.cast_shadows=False

    def changeVectorMove(self,vector):
        self.__currentStrategyMove=vector

    def translate(self,x,y,z,w):
        self.position=Vec4(self.position[0]+x,self.position[1]+y,self.position[2]+z,self.position[3]+w)
    def getCurrentStarategyMove(self):
        return self.__currentStrategyMove
    def _clearCurrentStrategyMove(self,can,callback=None):
        if(callback):callback(can)
        if(self.__currentStrategyMove not in can):self.__currentStrategyMove=None
    def stopVectorsMove(self):
        return self.__road.ifIsInRoad(self, self._clearCurrentStrategyMove)

    def move(self):
        if(self.__currentStrategyMove):
            self.__currentStrategyMove.move(self)

    def run(self):
        self.stopVectorsMove()
        self.move()
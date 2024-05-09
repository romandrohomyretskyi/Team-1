from Packman.ObjectMoving import*
from Packman.StrategyMove import*
from ursina import Ursina,PointLight,time
import math

class Privid(ObjectMoving):
    def __init__(self,position,size,entity,road,map,player,gameController,strategyControll):
        super().__init__(position,size,entity,road)
        self.__moveVectors=[MoveLeft,MoveRight,MoveTop,MoveDown]
        self.__map=map
        self.__player=player
        self.__gameController=gameController
        self.__strategyControll=strategyControll
        self.step=2
        self.changeVectorMove(MoveLeft)

    def controll(self,can):
        self.__strategyControll.controll(self,can,self.__player)
        if(self.getCurrentStarategyMove()==MoveLeft or self.getCurrentStarategyMove()==MoveForward  or self.getCurrentStarategyMove()==MoveW1):
            self.entity.rotation_y=180
            self.entity.rotation_z=180
        if(self.getCurrentStarategyMove()==MoveRight or self.getCurrentStarategyMove()==MoveBackward or self.getCurrentStarategyMove()==MoveW2):
            self.entity.rotation_y=0
            self.entity.rotation_z=180
        if(self.getCurrentStarategyMove()==MoveDown):
            self.entity.rotation_y=0
            self.entity.rotation_z=-90
        if(self.getCurrentStarategyMove()==MoveTop):
            self.entity.rotation_y=0
            self.entity.rotation_z=90


    def _clearCurrentStrategyMove(self,can):
        super()._clearCurrentStrategyMove(can,self.controll)

    def doIfCollision(self,pacmen):
        return lambda scene: scene.remove(self) if pacmen.isSuperPower else self.__gameController.gameOver()
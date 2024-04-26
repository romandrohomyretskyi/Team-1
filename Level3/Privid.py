from ObjectMoving import*
from StrategyMove import*
from ursina import Ursina

class Privid(ObjectMoving):
    def __init__(self,position,size,entity,road,map,player,window,text):
        super().__init__(position,size,entity,road)
        self.__moveVectors=[MoveLeft,MoveRight,MoveTop,MoveDown]
        self.__map=map
        self.__player=player
        self.__window=window
        self.__text=text
        self.step=1

    def controll(self,can):
        if(self.__player.position[0]>self.position[0] and MoveLeft in can):
            self.changeVectorMove(MoveLeft)
        elif(self.__player.position[0]<self.position[0] and MoveRight in can):
            self.changeVectorMove(MoveRight)

        if(self.__player.position[1]>self.position[1] and MoveDown in can):
            self.changeVectorMove(MoveDown)
        elif(self.__player.position[1]<self.position[1] and MoveTop in can):
            self.changeVectorMove(MoveTop)

    def _clearCurrentStrategyMove(self,can):
        super()._clearCurrentStrategyMove(can,self.controll)

    def doIfCollision(self,pacmen):
        def worck(scene):
            self.__window.gameRun=False
            self.__text.text="game over"
            self.__text.position=(-0.1,0.1)
            self.__text.color=(1,0.5,0,1)
        return worck
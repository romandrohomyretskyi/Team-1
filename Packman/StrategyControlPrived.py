from Packman.StrategyMove import*
from random import choice
from Packman.StrategyMove import MoveTop,MoveDown,MoveLeft,MoveRight

class MoveToPlayer:
    @staticmethod
    def controll(self,can,player):
        if(player.position[0]>self.position[0] and MoveLeft in can):
            self.changeVectorMove(MoveLeft)
        elif(player.position[0]<self.position[0] and MoveRight in can):
            self.changeVectorMove(MoveRight)

        if(player.position[1]>self.position[1] and MoveDown in can):
            self.changeVectorMove(MoveDown)
        elif(player.position[1]<self.position[1] and MoveTop in can):
            self.changeVectorMove(MoveTop)

        if(player.position[2]>self.position[2] and MoveBackward in can):
            self.changeVectorMove(MoveBackward)
        elif(player.position[2]<self.position[2] and MoveForward in can):
            self.changeVectorMove(MoveForward)

        if(player.position[3]>self.position[3] and MoveW2 in can):
            self.changeVectorMove(MoveW2)
        elif(player.position[3]<self.position[3] and MoveW1 in can):
            self.changeVectorMove(MoveW1)

class MoveRandom:
    @staticmethod
    def controll(self,can,player):
        if(len(can)==4):
            self.changeVectorMove(choice(can))
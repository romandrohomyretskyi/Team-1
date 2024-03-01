from ObjectMoving import*
from ursina import held_keys
from StrategyMove import*
from math import pi

class Pacman(ObjectMoving):
    __rotations=[0]*6
    __moveX={"left":MoveLeft,"right":MoveRight}
    def controll(self,camera,key):
        print(key)
        if(key=="1"):
            camera.rotation(xoz=pi/2)
            #camera.translate(800,0,1000,0)
            self.__moveX={"left":MoveForward,"right":MoveBackward}

        if(key=="2"):
            #camera.translate(-800,0,-1000,0)
            camera.rotation(xoz=-(pi/2))
            self.__moveX={"left":MoveLeft,"right":MoveRight}


        if(key=="5"):
            camera.rotation(yow=pi/2)
            #camera.translate(0,1000,1000,0)

        if(key=="6"):
            camera.rotation(zow=pi/2)

        if(held_keys["w"]):
            self.changeVectorMove(MoveTop)
        if(held_keys["s"]):
            self.changeVectorMove(MoveDown)
        if(held_keys["a"]):
            self.changeVectorMove(self.__moveX["left"])
        if(held_keys["d"]):
            self.changeVectorMove(self.__moveX["right"])

    def eat(self):
        pass
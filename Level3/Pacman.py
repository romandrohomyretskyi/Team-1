from ObjectMoving import*
from ursina import held_keys,Texture
from StrategyMove import*
from math import pi
from Timeout import*

class Pacman(ObjectMoving):
    __canRotationZ=True
    __canRotationW=True
    __moveX={"left":MoveLeft,"right":MoveRight}

    def __init__(self,position=Vec4(0,0,0,0),size=Vec3(10,10,10),road=None,entity=None,camera=None):
        super().__init__(position=position,size=size,entity=entity,road=road)
        self.__numberTablets=0
        self.__camera=camera
        self.__textures=[Texture("./Texture/pacmen.png"),Texture("./Texture/pacmen2.png")]
        self.__cadr=0
        self.step=3
        self.__timeout=Timeout()

    @property
    def numberTablets(self):
        return self.__numberTablets

    def displayTablets(self,text):
        text.text=f"Tablets {self.__numberTablets}"

    def acamulateNumberTablets(self):
        self.__numberTablets+=1

    def getIndexDisableCoords(self):
        if(self.__camera.xoz==0 and self.__camera.xow==0):
            return [2,3]
        if(self.__camera.xoz==pi/2 and self.__camera.xow==0):
            return [0,3]
        if(self.__camera.xow==pi/2 and self.__camera.xoz==0):
            return [0,2]

    def __changeTexture(self):
        self.entity.texture=self.__textures[self.__cadr]
        self.__cadr+=1
        if(self.__cadr>1):
            self.__cadr=0
    def animation(self):
        self.__timeout.start(self.__changeTexture,10)

    def controll(self):
        if(held_keys["1"]):
            self.__camera.xoz=pi/2
            self.__camera.xow=0
            self.__canRotationW=False
            self.__moveX["left"]=MoveForward
            self.__moveX["right"]=MoveBackward
        if(held_keys["2"]):
            self.__camera.xoz=0
            self.__camera.xow=0
            self.__moveX["left"]=MoveLeft
            self.__moveX["right"]=MoveRight
        if(held_keys["3"]):
            self.__camera.xow=pi/2
            self.__camera.xoz=0
            self.__moveX["left"]=MoveW1
            self.__moveX["right"]=MoveW2
        if(held_keys["w"]):
            self.changeVectorMove(MoveTop)
            self.entity.rotation_z=90
            self.entity.rotation_y=-3
            self.entity.rotation_x=-20
        if(held_keys["s"]):
            self.changeVectorMove(MoveDown)
            self.entity.rotation_z=-90
            self.entity.rotation_y=-3
            self.entity.rotation_x=20
        if(held_keys["a"]):
            self.changeVectorMove(self.__moveX["left"])
            self.entity.rotation_z=180
            self.entity.rotation_y=-210
            self.entity.rotation_x=0
        if(held_keys["d"]):
            self.changeVectorMove(self.__moveX["right"])
            self.entity.rotation_z=180
            self.entity.rotation_y=30
            self.entity.rotation_x=0

    def run(self):
        super().run()
        self.controll()
        self.animation()

from Packman.ObjectMoving import*
from ursina import held_keys,Texture,Audio
from Packman.StrategyMove import*
from math import pi
from Packman.Timeout import*

class Pacman(ObjectMoving):
    __canRotationZ=True
    __canRotationW=True
    __moveX={"left":MoveLeft,"right":MoveRight}

    def __init__(self,gameController,position=Vec4(0,0,0,0),size=Vec3(10,10,10),road=None,entity=None,camera=None):
        super().__init__(position=position,size=size,entity=entity,road=road)
        self.__numberTablets=0
        self.__camera=camera
        self.__textures=[Texture("./Packman/Texture/pacmen.png"),Texture("./Packman/Texture/pacmen2.png")]
        self.__superPowerTextures=[Texture("./Packman/Texture/pacmen4.png"),Texture("./Packman/Texture/pacmen5.png")]
        self.__cadr=0
        self.__timeoutAnimation=Timeout().initLoop()
        self.__timeout2=Timeout()
        self.__gameController=gameController
        self.step=3
        self.__superPower=False
        self.__translationSound=Audio("./Packman/Sounds/transition-explosion-121425.mp3")
        self.__disaybalSound=Audio("./Packman/Sounds/multi-pop-1-188165.mp3")

    @property
    def numberTablets(self):
        return self.__numberTablets

    def displayTablets(self,gameController):
        gameController.text=f"Tablets {self.__numberTablets}"

    def acamulateNumberTablets(self):
        self.__numberTablets+=1

    def getIndexDisableCoords(self):
        if(self.__camera.xoz==0 and self.__camera.xow==0):
            return [2,3]
        if(self.__camera.xoz==pi/2 and self.__camera.xow==0):
            return [0,3]
        if(self.__camera.xow==pi/2 and self.__camera.xoz==0):
            return [0,2]
    def animation(self):
        def changeTexture(time):
            self.entity.texture=self.__textures[time] if not self.__superPower else self.__superPowerTextures[time]
        self.__timeoutAnimation.start(1).loop(changeTexture, 6)

    def controll(self):
        if(held_keys["1"] or held_keys["2"] or held_keys["3"]):
            self.__translationSound.play()
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

    def ifIsWinner(self,maxTablets):
        print(maxTablets)
        if(self.__numberTablets==maxTablets):
            self.__gameController.winner()

    def disaybelSuperPower(self):
        def disaybel():
            self.__superPower=False
            self.__disaybalSound.play()
        self.__timeout2.start(500, disaybel)

    def activationSuperPower(self):
        self.__superPower=True

    @property
    def isSuperPower(self):
        return self.__superPower
    def run(self):
        super().run()
        self.controll()
        self.animation()
        self.disaybelSuperPower()

from ursina import Entity,Sky,AmbientLight,Texture,Audio,invoke
from Packman.Camera import*
from Packman.Scene import*
from Packman.Pacman import*
from Packman.Privid import*
from Packman.World import*
from Packman.Collision import*
from Packman.generateTesaract import genreateTesaract
from Packman.GameController import*
from Packman.StrategyControlPrived import*
import math

class Window(Entity):
    def __init__(self):
        self.start()

    def start(self):
        Audio("./Packman/Sounds/Carefree(chosic.com).mp3",loop=True).play()
        Sky(color=Vec4(0,0,0.1,1))

        self.__gameController=GameController()

        self.__camera=Camera(position=Vec4(0,0,1000,0))

        self.__texture=Texture("./Packman/Texture/privid.png")

        self.__map=Map(*genreateTesaract(2,2,2,2), 10,position=Vec4(0,0,0,0),size=Vec3(5,5,5))
        self.__pacman=Pacman(camera=self.__camera,
                             position=Vec4(0,0,0,0),size=Vec3(10,10,10),
                             road=self.__map, entity=Entity(model='sphere',rotation_z=180,rotation_y=30),
                             gameController=self.__gameController)
        self.__prividParams={
            "size":Vec3(30,30,30),
            "road":self.__map,
            "map":self.__map,
            "player":self.__pacman,
            "gameController":self.__gameController
        }
        self.__privid=Privid(position=Vec4(-300,0,0,0),strategyControll=MoveToPlayer,entity=Entity(model='sphere',color=Vec4(1,1,1,1),texture=self.__texture,rotation_z=180),**self.__prividParams)
        self.__privid2=Privid(position=Vec4(-300,-300,0,0),strategyControll=MoveRandom,entity=Entity(model='sphere',color=Vec4(1,0.3,0.3,1),texture=self.__texture,rotation_z=180),**self.__prividParams)
        self.__privid3=Privid(position=Vec4(-300,-300,-300,0),strategyControll=MoveRandom,entity=Entity(model='sphere',color=Vec4(1,1,0,1),texture=self.__texture,rotation_z=180),**self.__prividParams)
        self.__privid4=Privid(position=Vec4(-300,0,-300,-300),strategyControll=MoveRandom,entity=Entity(model='sphere',color=Vec4(0,1,0,1),texture=self.__texture,rotation_z=180),**self.__prividParams)
        self.__scene=Scene(self.__pacman)
        self.__camera.translate(position=Vec4(0,1,0,0))

        self.__collisionController=CollisionController(self.__scene)

        self.__scene.add(self.__pacman)
        self.__scene.add(self.__privid)
        self.__scene.add(self.__privid2)
        self.__scene.add(self.__privid3)
        self.__scene.add(self.__privid4)
        self.__scene.addArray([*self.__map.tablets,*self.__map.decorations])
        AmbientLight(color=Vec4(0.5,0.5,0.5,1))


    def update(self):
        if self.__gameController.isGame:
            self.__pacman.displayTablets(self.__gameController)
            self.__scene.collision(self.__collisionController,self.__pacman)
            self.__pacman.ifIsWinner(self.__map.tabletsNumber)
            self.__pacman.run()
            self.__privid.run()
            self.__privid2.run()
            self.__privid3.run()
            self.__privid4.run()
        self.__camera.connect(self.__pacman)
        self.__scene.update(self.__camera)
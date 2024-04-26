from ursina import Entity,Sky,DirectionalLight,Ursina,Text
from Camera import*
from Scene import*
from Pacman import*
from Privid import*
from World import*
from Collision import*
from generateTesaract import genreateTesaract
import math


class Window(Entity):
    def __init__(self):
        self.start()

    def start(self):
        self.gameRun=True
        self.__app=Ursina()
        Sky(color=Vec4(0.5,0.5,0.9,1))
        self.__text=Text("Tablets:",position=(-0.8,0.4),scale=2,color=(0,0,0,1))

        self.__camera=Camera(position=Vec4(0,0,1000,0))


        self.__map=Map(*genreateTesaract(2), 10,position=Vec4(0,0,0,0),size=Vec3(5,5,5))
        self.__pacman=Pacman(camera=self.__camera,position=Vec4(0,0,0,0),size=Vec3(10,10,10), road=self.__map, entity=Entity(model='sphere',rotation_z=180,rotation_y=30))
        self.__privid=Privid(position=Vec4(-300,0,0,0),size=Vec3(10,20,10),entity=Entity(model='cube',color=Vec4(0,0,1,1)),road=self.__map,map=self.__map,player=self.__pacman,window=self,text=self.__text)

        self.__scene=Scene(self.__pacman)
        self.__camera.translate(position=Vec4(0,1,0,0))

        self.__map.setPackman(self.__pacman)

        self.__collisionController=CollisionController(self.__scene)

        self.__scene.add(self.__pacman)
        self.__scene.add(self.__privid)
        self.__scene.addArray([*self.__map.tablets,*self.__map.decorations])



        DirectionalLight().rotation_x=141
        DirectionalLight().rotation_x=-141
        DirectionalLight().rotation_x=50
        DirectionalLight().rotation_x=-50



    def update(self):
        if self.gameRun:
            self.__scene.collision(self.__collisionController,self.__pacman)
            self.__pacman.displayTablets(self.__text)
            self.__scene.collision(self.__collisionController,self.__pacman)
            self.__pacman.run()
            self.__privid.run()
        self.__camera.connect(self.__pacman)
        self.__scene.update(self.__camera)

    def run(self):
        self.__app.run()


window=Window()
def update():
    window.update()
window.run()

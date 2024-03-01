from ursina import*
from Camera import*
from Scene import*
from Pacman import*
from World import*
from math import pi


class Window(Entity):
    def __init__(self):
        self.start()

    def start(self):
        self.__app=Ursina()
        self.__camera=Camera()


        self.__map=Map([(0, 0, 0, 0), (-30, 0, 0, 0), (0, 30, 0, 0),(0,0,0,-30),(0,0,-30,0)], [(0, 1), (0, 2),(0,3),(0,4)], 10,position=Vec4(0,0,0,0),size=Vec3(5,5,5))

        self.__pacman=Pacman(position=Vec4(0,0,0,0),size=Vec3(10,10,10), road=self.__map, entity=Entity(model='sphere', color=color.yellow))
        self.__scene=Scene()
        self.__camera.translate(position=Vec4(0,1,0,0))

        self.__scene.add(self.__pacman)
        self.__scene.add(self.__map)



        self.__directional_light=DirectionalLight()

        self.__directional_light.rotation_x=141



    def input(self,key):
        self.__pacman.controll(self.__camera,key)

    def update(self):
        self.__pacman.stopVectorsMove()
        self.__pacman.move()
        self.__camera.connect(self.__pacman)
        self.__scene.update(self.__camera)

    def run(self):
        self.__app.run()


window=Window()
def update():
    window.update()

def input(key):
    window.input(key)

window.run()

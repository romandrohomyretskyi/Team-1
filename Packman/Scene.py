from ursina import destroy
from Packman.Collision import*
class Scene:

    def __init__(self,player):
        self.__objects=[]
        self.__player=player
    def add(self,object):
        self.__objects.append(object)


    def remove(self,object):
       destroy(object.entity)
       self.__objects=list(filter(lambda elem:elem!=object,self.__objects))

    def collision(self,collisionController,pacman):
        for object in self.__objects:
            if("doIfCollision" in object.__class__.__dict__):
                collisionController.collision(object, pacman, object.doIfCollision(pacman))

    def addArray(self,objects):
        for object in objects:
            self.add(object)

    def update(self,camera):
        for object in self.__objects:
           object.update(camera,self.__player)
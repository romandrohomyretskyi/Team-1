
class CollisionController:
    def __init__(self,scene):
        self.__scene = scene

    @staticmethod
    def isCollision(object1,object2,radius):
        return (object1.position[0]-object2.position[0])**2+(object1.position[1]-object2.position[1])**2+(object1.position[2]-object2.position[2])**2+(object1.position[3]-object2.position[3])**2<=radius

    def collision(self,object1,object2,then):
        if (CollisionController.isCollision(object1,object2,object1.size[0])):
            print(10)
            then(self.__scene)
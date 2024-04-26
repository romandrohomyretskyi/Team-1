from ursina import Vec3
from Collision import CollisionController

class ObjectGame:
    def __init__(self,position,size,entity):
        self.position=position
        self.size=size
        self.entity=entity

    def update(self,camera,player):
        self.entity.enabled=False
        i,j=player.getIndexDisableCoords()
        if CollisionController.isCollision(player,self,5000) and player.position[i]==self.position[i] and player.position[j]==self.position[j] and (player.position!=self.position if player!=self else True):
            position=camera.use(self)
            number=position[3]-20
            if(number<0):
                self.entity.enabled=True
                self.entity.position=Vec3(position[0],position[1],position[2])/number
                self.entity.scale=self.size/number

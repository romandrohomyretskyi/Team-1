from ursina import Vec3

class ObjectGame:
    def __init__(self,position,size,entity):
        self.position=position
        self.size=size
        self.entity=entity

    def update(self,camera):
        position= camera.use(self)
        number=position[3]-100
        self.entity.position=Vec3(position[0],position[1],position[2])/number
        self.entity.scale=self.size/number
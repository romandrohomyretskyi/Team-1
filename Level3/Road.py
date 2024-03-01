from ursina import Vec4,Entity
from ObjectGame import*
class Road:
    def __init__(self,start,end):
        self.start=start
        self.end=end

    def isInRoad(self,object):
        return ((self.start[0] <= object.position[0] <= self.end[0] or self.end[0] <= object.position[0] <= self.start[0]) and \
               (self.start[1] <= object.position[1] <= self.end[1] or self.end[1] <= object.position[1] <= self.start[1]) and \
               (self.start[2] <= object.position[2] <= self.end[2] or self.end[2] <= object.position[2] <= self.start[2]) and \
               (self.start[3] <= object.position[3] <= self.end[3] or self.end[3] <= object.position[3] <= self.start[3]))

    def isInVertex(self,object,pos):
        return object.position[0]==pos[0] and object.position[1]==pos[1] and object.position[2]==pos[2] and object.position[3]==pos[3]

    def getDirectionVector(self):
        return Vec4((self.end[0] - self.start[0]), (self.end[1] - self.start[1]), (self.end[2] - self.start[2]), (self.end[3] - self.start[3])).normalized()

    def draw(self,size,step):
        arrayPoint=[]

        vector=self.getDirectionVector()*step
        positionStart=self.start*step
        lineLength=vector[0]**2+vector[1]**2+vector[2]**2+vector[3]**2

        i=0
        while i<=lineLength:
            i+=step/3
            positionStart=Vec4(positionStart[0]+vector[0],positionStart[1]+vector[1],positionStart[2]+vector[2],positionStart[3]+vector[3])
            arrayPoint.append(ObjectGame(position=positionStart,size=size,entity=Entity(model="sphere",color=Vec4(1,1,1,1))))
        return arrayPoint

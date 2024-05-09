from numpy import array
from ursina import Vec4
from Packman.linearTransform import*

class Camera:
    def __init__(self,xoy=0,xoz=0,yoz=0,xow=0,yow=0,zow=0,position=Vec4(0,0,0,0)):
        self.__proection=array([[1,0,0,0,0],
                         [0,1,0,0,0],
                         [0,0,1,0,0],
                         [0,0,0,1,0],
                         [0,0,0,0,1]])
        self.xoy=xoy
        self.xoz=xoz
        self.yoz=yoz
        self.xow=xow
        self.yow=yow
        self.zow=zow
        self.__kash={}
        self.position=position
        self.__changePlanes=self.__createPlanes()
        self.__defaultPlanes=self.__createPlanes()
        self.__defaultPosition=self.position
        self.__init()
        self.i=0

    def __init(self):
        self.__proectionMatrix=self.__rotate(self.__changePosition(self.__proection,
                                                                   x=self.position[0], y=self.position[1],
                                                                   z=self.position[2], w=self.position[3])
                                             ,self.xoy,self.xoz,self.yoz,
                                             self.xow,self.yow,self.zow),

    def __createPlanes(self):
        return [self.xoy,self.xoz,self.yoz,self.xow,self.yow,self.zow]


    def __rotate(self,proectionMatrix,xoy=0,xoz=0,yoz=0,xow=0,yow=0,zow=0):
        self.__proectionMatrix=(proectionMatrix
                                @ rotateXOY(xoy)
                                @ rotateXOZ(xoz)
                                @ rotateYOZ(yoz)
                                @ rotateXOW(xow)
                                @ rotateYOW(yow)
                                @ rotateZOW(zow))
        return self.__proectionMatrix

    def __changePosition(self,proectionMatrix,x=0,y=0,z=0,w=0):
        self.__proectionMatrix=proectionMatrix @ translate(x,y,z,w)
        return self.__proectionMatrix


    def rotation(self,xoy=0,xoz=0,yoz=0,xow=0,yow=0,zow=0):
        self.xoy+=xoy
        self.xoz+=xoz
        self.yoz=yoz
        self.xow+=xow
        self.yow+=yow
        self.zow+=zow
        self.__changePlanes=self.__createPlanes()

    def translate(self,position):
        self.position=Vec4(self.position[0] + position[0],
                           self.position[1] + position[1],
                           self.position[2] + position[2],
                           self.position[3] + position[3])
        self.__defaultPosition=self.position

    def use(self,object):
        self.__update()
        position=array([object.position[0],object.position[1],object.position[2],object.position[3],1]) @ self.__proectionMatrix
        return Vec4(position[0][0],position[0][1],position[0][2],position[0][3])
    def __update(self):
        self.__changePlanes=self.__createPlanes()
        if(self.position!=self.__defaultPosition or self.__changePlanes!=self.__defaultPlanes):
            self.__init()
            self.__defaultPlanes=self.__changePlanes
            self.__defaultPosition=self.position

    def connect(self,object):
        self.position=-object.position
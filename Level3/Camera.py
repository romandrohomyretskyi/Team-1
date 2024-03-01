from numpy import array
from ursina import Vec4
from linearTransform import*

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
        self.__position=position
        self.__init()

    def __init(self):
        self.__proectionMatrix=self.__rotate(self.__changePosition(self.__proection,
                                              x=self.__position[0],y=self.__position[1],
                                              z=self.__position[2],w=self.__position[3])
                                             ,self.xoy,self.xoz,self.yoz,
                                             self.xow,self.yow,self.zow),


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

    def translate(self,position):
        self.__position=Vec4(self.__position[0]+position[0],
                             self.__position[1]+position[1],
                             self.__position[2]+position[2],
                             self.__position[3]+position[3])

    def use(self,object):
        self.__init()
        position=array([object.position[0],object.position[1],object.position[2],object.position[3],1]) @ self.__proectionMatrix
        print(position)
        return Vec4(position[0][0],position[0][1],position[0][2],position[0][3])

    def connect(self,object):
        self.__position=-object.position

class Move:
    def __init__(self,vector,direction):
        self.__vectors={
            "x":lambda obj:obj.translate(direction*obj.step,0,0,0),
            "y":lambda obj:obj.translate(0,direction*obj.step,0,0),
            "z":lambda obj:obj.translate(0,0,direction*obj.step,0),
            "w":lambda obj:obj.translate(0,0,0,direction*obj.step)
        }
        self.__vector=vector
    def move(self,obj):
        self.__vectors[self.__vector](obj)


MoveTop=Move("y",-1)
MoveDown=Move("y",1)
MoveLeft=Move("x",1)
MoveRight=Move("x",-1)
MoveForward=Move("z",-1)
MoveBackward=Move("z",1)
MoveW1=Move("w",-1)
MoveW2=Move("w",1)
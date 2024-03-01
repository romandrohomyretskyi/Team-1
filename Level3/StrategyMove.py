class MoveTop:
    @staticmethod
    def move(obj):
        obj.translate(0,-obj.step,0,0)

class MoveDown:
    @staticmethod
    def move(obj):
        obj.translate(0,obj.step,0,0)

class MoveLeft:
    @staticmethod
    def move(obj):
        obj.translate(obj.step,0,0,0)

class MoveRight:
    @staticmethod
    def move(obj):
        obj.translate(-obj.step,0,0,0)

class MoveForward:
    @staticmethod
    def move(obj):
        obj.translate(0,0,-obj.step,0)

class MoveBackward:
    @staticmethod
    def move(obj):
        obj.translate(0,0,obj.step,0)

class MoveW1:
    @staticmethod
    def move(obj):
        obj.translate(0,0,0,obj.step)

class MoveW2:
    @staticmethod
    def move(obj):
        obj.translate(0,0,0,-obj.step)
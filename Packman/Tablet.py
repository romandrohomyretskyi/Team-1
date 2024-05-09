from Packman.ObjectGame import*
from ursina import Audio


class Tablet(ObjectGame):

    def doIfCollision(self,pacman):
        def worck(scene):
            pacman.acamulateNumberTablets()
            scene.remove(self)
        return worck



class SuperTablet(Tablet):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.__tabletSounds=Audio("./Packman/Sounds/cute-level-up-3-189853.mp3")
    def doIfCollision(self,pacman):
        f=super().doIfCollision(pacman)
        def worck(scene):
            self.__tabletSounds.play()
            f(scene)
            pacman.activationSuperPower()
        return worck
from ObjectGame import*


class Tablet(ObjectGame):

    def doIfCollision(self,pacman):
        def worck(scene):
            pacman.acamulateNumberTablets()
            scene.remove(self)
        return worck
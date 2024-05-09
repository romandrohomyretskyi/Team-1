from ursina import Text,Audio

class GameController:
    def __init__(self):
        self.__text=Text("Tablets:",position=(-0.8,0.4),scale=2,color=(1,1,1,1))
        self.__isGame=True
        self.__audio=Audio("./Packman/Sounds/brass-fail-11-a-207140.mp3")

    @property
    def isGame(self):
        return self.__isGame

    @isGame.setter
    def text(self,text):
        self.__text.text=text

    def __gameEvent(self,text):
        self.__isGame=False
        self.__text.text=text
        self.__text.position=(-0.1,0.1)
        self.__text.color=(1,0.5,0,1)

    def gameOver(self):
        self.__gameEvent("game over")
        self.__audio.play()

    def winner(self):
        self.__gameEvent("winner")
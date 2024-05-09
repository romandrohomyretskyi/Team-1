class Timeout:
    def __init__(self):
        self.__time=0

    def start(self,duration,callback=None):
        if(self.__time==duration):
            callback and callback()
        self.__time+=1
        if(self.__time>duration):
            self.__time=0
        return self

    def initLoop(self):
        self.__timeout=Timeout()
        return self

    def loop(self,callback,duration):
        self.__timeout.start(duration, lambda: callback(self.__time))
        return self
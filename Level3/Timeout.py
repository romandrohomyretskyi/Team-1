class Timeout:
    def __init__(self):
        self.__time=0

    def start(self,callback,time):
        if(self.__time==time):
            callback()
        self.__time+=1
        if(self.__time>time):
            self.__time=0
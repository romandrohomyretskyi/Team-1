
class Scene:
    __objects=[]

    def add(self,object):
        self.__objects.append(object)


    def remove(self,object):
       object.entity.destroy()
       self.__objects=list(self.__objects.filter(lambda elem:elem!=object))

    def update(self,camera):
        for object in self.__objects:
            object.update(camera)

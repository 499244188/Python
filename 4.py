#类
class FooClass(object):
    version = 0.1
    def __init__(self,nm='John Doe'):
        self.name = nm
        print('Created a class instance for',nm)
    def showname(self):
        print('You Name is',self.name)
        print('My name is ',self.__class__.__name__)
    def shwcer(self):
        print(self.version)
    def addMe2Me(self,x):
        return x + x
foo = FooClass()

foo.showname()
print(foo.addMe2Me(45))
fbb = FooClass('Dou_Bi')
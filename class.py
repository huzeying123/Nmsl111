class Person:
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def greet(self):
        print("Hello,world!I'm {}".format(self.name))
foo = Person()
bar = Person()
foo.set_name('fuck')
bar.set_name('you')
foo.greet()
bar.greet()

class Secretive:
    def __inaccessible(self):
        print('Bet you can see me')
    def accessible(self):
        print('The secret message is:')
        self.__inaccessible()
s = Secretive()
s.accessible()#不报错
s.__inaccessible()#报错  私有属性不能从对象外部访问

#在类class里面有Secretive函数，调用时候我们对s属于Sec这一类，accessible和inaccessible是Secretive的两个的功能函数
#双下划线的区别：在s属于Sec这一类之后，没有双下划线的可以直接调用，为__main__函数调用accessible函数。
#但是有双下划线的只能用Sec这一类中的函数去调用，如ac可以调用inac  但是我不能直接调用inac
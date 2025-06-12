
from abc import ABC,abstractmethod

class Animal(ABC):
    def move(self):
        pass
class human(Animal):
    def move(self):
        print("i can walk and run")
class snake(Animal):
    def move(self):
        print("i can crawl")
class dog(Animal):
    def move(self):
        print("i can bark")
class lion(Animal):
    def move(self):
        print("i can roar")
r=human()
r.move()
k=snake()
k.move()
r=dog()
r.move()
k=lion()
k.move()

# Class: is the blueprint for creating an objects.
# Object: is an instance of class
# john (object) is an instance of Human (class)
# You should name class with Pascal naming conventoin (CustomerService,HumanBeing)
# Constructor(__init__) is one magic method which is being called as soon as object is created and it should return NONE
# Self:(pass the object as an argument inside the methods, so that we can refer to it with it's other methods and attributes )
# 1- All functions inside the classes should have at least one parameter |   this parameter refere to the current object
#   1.1 By convention, We called it self,-> def run(self)   it can be anything,and throuth the whole class we can use self as a reference to the object, self == object reference name
#   1.2 When calling the method of an object you don't have to pass the object as a parameter,it is passed by default. and we recieve it in the method in the first argument-> self .


class Point:
    #class attribute:
    default_x , default_y  = 0 , 0

    def __init__(self, x: int , y: int ) -> None:
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return 'osama'
    

    @staticmethod
    def hello():
        print('morsi')
    

    def draw(self):
        print(f"point ({self.x},{self.y})")
    
    # magic method:
    def __str__(self) -> str:
        return f"({self.x} , {self.y})"
    
    # you need to edit the behavior of ( == ), from checking the memory location to check the value and that what we edit using this magic method:
    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y
    # we need to edit the behavior of adding 2 classes (p1 + p2), so we return what should be done
    def __add__(self,othe):
        return Point(self.x + other.x,self.y + other.y)
    



point_1 = Point.zero() # -> Here no object is created as we can call the class method directly by the name of the class without creating an object 
point_1 = Point(y=5, x=4) #-> we call the class to create the object and refer to it's [ value - identity -type ] by reference name -> "point_1"
isinstance(point_1, Point)
Point(5,6) # here we create another object, but we don't have a refrence name to it, so python garpage collector will delete it

other = Point(4,5,)
print(point_1 == other)
print(point_1 + other)





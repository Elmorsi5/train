# it's not recommended to use multible inheritance [only in a special cases - keep it 2 layers not more ]
# ABC-> Abstract Base Classes:(interface) abstract class, prevent creating an object form this class  / search the difference between abtract class and interface
# abtractmethod: Classes with abstract method are  abstract class by default - it makea this method required to be implemented in the childclass. 


from abc import ABC,abstractmethod

class InvalidOperationError(Exception):
    pass
    
class Stream(ABC):
    def __init__(self) -> None:
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError
        self.opened = True
    
    def close(self):
        if not self.opened:
            raise InvalidOperationError
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class File(Stream):
    def read(self):
        print("we are reading from file")


class Network(Stream):
    def read(self):
        print("we are reading from Network")


dl = File()
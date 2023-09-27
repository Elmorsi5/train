# we use getter when we make the instance variables as private __ , so to get it's values outside the object we need a functions that access it and give us the return value
# and use getter if we want to make some constrains in the input vlaues form the user
# nore: to use @property you should set instance variable to private __
# each property should have a setter and getter
# the enhanced model is to use propery function, and more enhanced is to use @property decorator

class Product:
    def __init__(self,price) -> None:
        self.__price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def set_price(self,price):
        if price <0:
            raise ValueError("ther is no product with this price")
        self.__price = price

    # price = property(get_price,set_price) # this will return a property object that uses the functons that passed to it as arguments to set and get through price kw.
    

product = Product(10)
# product.price = 30
print(product.price)
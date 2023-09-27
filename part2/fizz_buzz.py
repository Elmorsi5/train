def fizz_buzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    return number
# "return" break the function, if it's executed it end the function 

y = int(input("Write the needednumber"))
x = fizz_buzz(y)
print(x)
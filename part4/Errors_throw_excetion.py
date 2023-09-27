# Handling expected errors by throwing an exceptoins that suitable to this to prevent our app from craching:
# Exception is the message that guide us to avoid this errors.
try:
    with open('mohamed.txt') as file, open('try.txt') as file2:
        print("filed is opened")
    a = int(input("write number:"))
except (ValueError):
    print("I am handling two type of errors that may appear,if somenew errors appears it will not be handeled")
except ZeroDivisionError:
    print("it will not be executed becaues we include it previously")
except FileNotFoundError:
    print("go and write the path of the file")
else:
    print("it will be executed only if we have an exception type that we don't include above") #like for else
    print('no exception were thro')
finally:
    print("it will be executed in all casea, in case of excepton or not")
    print("it's good in the case of releasing files and close connections and so on")

    # ----------------------
    # rsise EXCEPTION:
    # -we use it to raise exceptoin if a condition is true
    if 5<7:
        raise ValueError("incorrect")
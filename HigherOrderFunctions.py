# higher order functions = a function that either:
#                          1. accepts a function as an argument or
#                          2. returns a function (In python, functions are also treated as objects)

# Example 1 ---------------------

# def loud(text): # creating load function and setting variable "text" as parameter
#     return text.upper() # returning the variable text converted onto uppercase

# def quiet(text): 
#     return text.lower()

# def hello(func): # creating hello function and setting variable "func" as parameter. 
#                  # Function load is being called here as "func". hello() is the higher order function here
#     text = func("hello") # loud function called as "func" is being called as "text" npw
#     print(text)

# hello(loud) # calling hello function and passing loud function as argument
# hello(quiet)

# example 2 ---------------------

def divisor(x): # outer function divisor() accepting a number as argument, here called "x". This is the higher order function
    def dividend(y): # inner function dividend() accepting a number as argument, here called "y"
        return y/x
    return dividend # divisor() function is a higher order function bc it is a functions that returns another funtion, in this case dividend() function

divide = divisor(2)
print(divide(10))
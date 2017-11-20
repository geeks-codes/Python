from math import sin
##Decorator for sin function

def sin_decorator(func):
  def func_wrapper(x):
    print("Before calling decorator")
    return func(x)
    print("After calling decorator")
  return func_wrapper 
  
sin = sin_decorator(sin)

print("Hi",sin(1))

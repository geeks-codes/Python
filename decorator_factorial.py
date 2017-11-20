def our_decorator(func):
  def function_wrapper(x):
    print("Before calling funcion", func.__name__)
    if(x >= 0 and type(x)==int):
      return func(x)
    else:
      return "Not valid input"
    print("After calling function", func.__name__)
  return function_wrapper
  
@our_decorator
def factorial(n):
  fact = 1
  while n>0:
    fact = fact * n
    n = n - 1
  print(fact)
  return fact

print("The factorial is ",factorial(-5))

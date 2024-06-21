def greet(name):
    def magic_function(func):
        print("Hello, welcome to the function!")
        return func
    return magic_function(name)

@greet
def say_hello(name):
    print("Hello", name)

say_hello("Jerrin")

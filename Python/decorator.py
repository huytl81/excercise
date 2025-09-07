# NOTE: Dung higher-order-funtion thong thuong
# wrapped function va wrapper function

def decorator_func(func):
    def wrapper_func(name, age):
        print("Truoc khi say_hello duoc goi")
        func(name, age)
        print("Sau khi say_hello duoc goi")
    return wrapper_func

@decorator_func # say_hello = decorator_func(say_hello)
def say_hello(name, age):
    print(f"Hello {name}, you are {age} years old!")

# NOTE: Dung higher order function nguyen ban
# my_func = decorator_func(say_hello)
# my_func("Huy", "22")

# NOTE: Dung decorator
say_hello("Huy", "22") # Goi truc tiep ham duoc bao wrapped

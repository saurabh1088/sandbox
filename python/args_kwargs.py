# ----------------------------------------------
# Args and Kwargs

def my_function_with_args(*args):
    for arg in args:
        print(arg)

print("Using *args:")
my_function_with_args("Hello", "World", "my", "name", "is", "Batman", "and", "I", "am", "a", "superhero")


def my_function_with_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print("\nUsing **kwargs:")
my_function_with_kwargs(name="Bruce Wayne", alias="Batman", occupation="Superhero", city="Gotham")

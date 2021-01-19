class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class MyPrettyLittleSingleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        print(foo)

if __name__ == "__main__":
    s1 = MyPrettyLittleSingleton()
    s2 = MyPrettyLittleSingleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

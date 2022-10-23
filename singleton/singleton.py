class MetaclassSingleton(type):
    _instances = {}

    def __call__(cls):
        print()
        if cls not in cls._instances:
            instance = super().__call__()
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=MetaclassSingleton):

    def __init__(self):
        print("foo")


class Singleton2(metaclass=MetaclassSingleton):

    def __init__(self):
        print("foo_2")


if __name__ == "__main__":
    instance_1 = Singleton()
    instance_2 = Singleton()
    assert id(instance_1) == id(instance_2)

    instance2_1 = Singleton2()
    instance2_2 = Singleton2()
    assert id(instance2_1) == id(instance2_2)
    assert id(instance2_1) != id(instance_1)

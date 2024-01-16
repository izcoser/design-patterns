class SingletonMeta(type):
    """
    Singleton can be implemented in different ways, such as
    base class, decorator and metaclass. For this example,
    we're using a metaclass.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class Database(metaclass=SingletonMeta):
    def select(self):
        return "data"
    
if __name__ == "__main__":
    database_1 = Database()
    database_2 = Database()

    id_1 = id(database_1)
    id_2 = id(database_2)

    print(id_1)
    print(id_2)

    if id_1 == id_2:
        print("Singleton database working as expected.")
        print("Both variables have the same instance.")
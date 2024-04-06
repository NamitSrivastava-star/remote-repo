"""Singleton pattern using decorators
"""

def Singleton(class_):
    instances = {}
    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance

@Singleton
class Database:
    def __init__(self) -> None:
        print("Database instance is created")   

if __name__ == "__main__":
    database1 = Database()
    database2 = Database()
    print("Database1 = ", database1)
    print("Database2 =", database2)  
    print("Both Databases object is Equal", database1==database2)       
def instances_counter(cls):
    class InstanceCounter:
        _count = 0

        @classmethod
        def init_counter(cls):
            if "_count" not in cls.__dict__:
                cls._count = 0

        def __init__(self):
            self.init_counter()
            super(cls, cls).__new__(cls)
            self.__class__._count += 1

        @classmethod
        def get_created_instances(cls):
            cls.init_counter()
            return cls._count

        @classmethod
        def reset_instances_counter(cls):
            cls.init_counter()
            try:
                return cls._count
            finally:
                cls._count = 0

    return InstanceCounter


@instances_counter
class User:
    pass


if __name__ == '__main__':

    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    print(User.get_created_instances())  # 3
    print(User.reset_instances_counter())
    print(User.get_created_instances())# 3
    
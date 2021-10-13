def instances_counter(cls):
    class InstanceCounter:
        _count = 0

        def __init__(self):
            super(cls, cls).__new__(InstanceCounter)
            self.__class__._count += 1

        @classmethod
        def get_created_instances(cls):
            return cls._count

        @classmethod
        def reset_instances_counter(cls):
            try:
                return cls._count
            finally:
                cls._count = 0

    return InstanceCounter

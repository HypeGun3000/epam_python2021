def instances_counter(cls):
    class InstanceCounter(cls):
        _count = 0

        def __init__(self):
            super(cls, cls).__new__(InstanceCounter)
            self.__class__._count += 1

        @classmethod
        def get_created_instances(cls):
            return cls._count

        @classmethod
        def reset_instances_counter(cls):
            last_count = cls._count
            cls._count = 0
            return last_count

    return InstanceCounter

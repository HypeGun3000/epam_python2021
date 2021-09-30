from homework6.task1.oop_1_decorator import User


class TestDecoratorInstanceCounter:
    def test_count_created_class_instance(self):
        assert User.get_created_instances() == 0
        user, _, _ = User(), User(), User()
        assert User.get_created_instances() == 3
        assert User.reset_instances_counter() == 3
        assert User.get_created_instances() == 0



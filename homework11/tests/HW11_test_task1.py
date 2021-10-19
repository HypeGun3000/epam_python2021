from homework11.task1.remove_duplicate_metaclass import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


class TestMetaClass:
    def test_attribute_from_ColorsEnum(self):
        assert ColorsEnum.RED == "RED"

    def test_attribute_from_SizesEnum(self):
        assert SizesEnum.XL == "XL"

from enum import Enum, auto


class Brands(Enum):

    def _generate_next_value_(self, start, count, last_values):
        str_name = str(self)
        return str_name[0].upper() + str_name.lower()[1:]

    @classmethod
    def default_brand(cls):
        return cls.UNDEFINED

    def __str__(self):
        return self.value

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

    UNDEFINED = auto()
    SAMSUNG = auto()
    APPLE = auto()
    XIAOMI = auto()
    NOKIA = auto()
    SONYERICSSON = auto()
    HTC = auto()
    HUAWEI = auto()
    LG = auto()
    SONY = auto()

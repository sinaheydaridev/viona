from enum import Enum


class EnumBase(Enum):
    @classmethod
    def choices(cls):
        return [(i, i.value) for i in cls]

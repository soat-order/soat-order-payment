from enum import Enum

class TypePayment(Enum):
    MONEY = 1
    CREDIT_CARD = 2
    DEBIT_CARD = 3

    @classmethod
    def valueOfValid(cls, value) -> bool:
        return any(enumType for enumType in cls if enumType.value == str(value).upper() or enumType.name == str(value).upper())

    @classmethod
    def valueOf(cls, value):
        # return name in cls.__members__
        for enumType in cls:
            if (enumType.value == str(value).upper() or enumType.name == str(value).upper()):
                return enumType
        return None
    
from dataclasses import dataclass, field
import uuid
from datetime import datetime
from src.core.domain.enum.type_payment_enum import TypePayment

@dataclass
class Payment:
    _id: str = field(init=False, default=None)
    orderId: str
    type: TypePayment
    amountPaid: float
    dateTimePaid: datetime = field(init=False, default=None)

    def __post_init__(self):
        self.id = str(uuid.uuid4())

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value


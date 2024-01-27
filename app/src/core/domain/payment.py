from dataclasses import dataclass, field
from datetime import datetime
from src.core.domain.enum.type_payment_enum import TypePayment

@dataclass
class Payment:
    id: str = field(init=False, default=None)
    orderId: str
    type: TypePayment
    amountPaid: float
    dateTimePaid: datetime = field(init=False, default=None)

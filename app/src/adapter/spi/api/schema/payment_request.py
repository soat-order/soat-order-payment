from typing import List
from dataclasses import dataclass, field


@dataclass
class PaymentDataRequest:
    type: str
    amountPaid: float = field(default=0.00)

@dataclass
class PaymentRequest:
    orderId: str
    payments: List[PaymentDataRequest] = field(default_factory=List[PaymentDataRequest])

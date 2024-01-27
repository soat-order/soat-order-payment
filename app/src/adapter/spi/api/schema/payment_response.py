from dataclasses import dataclass, field


@dataclass
class PaymentResponse:
    id: str
    orderId: str
    type: str
    amount: float = field(default=0.00)
    amountPaid: float = field(default=0.00)
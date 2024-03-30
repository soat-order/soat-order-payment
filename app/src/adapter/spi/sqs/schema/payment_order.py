from dataclasses import dataclass, field, asdict
from datetime import datetime
from src.core.domain.enum.type_payment_status_enum import TypePaymentStatus

@dataclass
class PaymentOrder:
    orderId: str
    amountPaid: float
    dateTimePaid: datetime
    status: TypePaymentStatus = field(init=False)

    def toDict(self):
        # return asdict(self)
        return {
            'orderId': self.orderId,
            'amountPaid': self.amountPaid,
            'dateTimePaid': self.dateTimePaid.isoformat(),
            'status': self.status.name
        }

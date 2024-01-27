from abc import ABC
from src.core.domain.payment import Payment
from typing import List


class PaymentPostUseCase(ABC):
    def save(self, payment: Payment) -> Payment:
        raise NotImplementedError

    def savePayments(self, payments: List[Payment]) -> List[Payment]:
        raise NotImplementedError

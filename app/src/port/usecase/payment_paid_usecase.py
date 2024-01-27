from abc import ABC
from src.core.domain.payment import Payment


class PaymentPaidUseCase(ABC):
    def execute(self, id: str, mseconds: int) -> Payment:
        raise NotImplementedError

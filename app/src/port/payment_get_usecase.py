from typing import List
from abc import ABC, abstractclassmethod
from src.core.domain.payment import Payment


class PaymentGetUseCase(ABC):
    @abstractclassmethod
    def getById(self, id: str) -> Payment:
        raise NotImplementedError

    @abstractclassmethod
    def getByOrderId(self, orderId: str) -> List[Payment]:
        raise NotImplementedError

    @abstractclassmethod
    def getByIdAndDateTimePaid(self, id: str) -> Payment:
        raise NotImplementedError

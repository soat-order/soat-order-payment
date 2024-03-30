from typing import Any, List, Generic, TypeVar
from abc import abstractmethod, ABC

# tipagem para objeto
T = TypeVar("T")

class PaymentProducer(ABC, Generic[T]):
    @abstractmethod
    def sendMessagePayment(self, paymentOrder: T):
        pass

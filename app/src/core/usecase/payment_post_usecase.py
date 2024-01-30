from typing import List
from src.core.domain.payment import Payment
from src.core.domain.enum.type_payment_enum import TypePayment
from src.port.usecase.payment_post_usecase import PaymentPostUseCase
from src.port.spi.persistence.repository.repository import Repository
from src.core.exception.business_exception import BusinessException
from src.adapter.spi.persistence.repository.payment_repository import PaymentRepository
from src.adapter.spi.persistence.mapper.payment_mapper import PaymentMapper
from src.core.util.logger_custom import Logger


class PaymentPostUseCaseImpl(PaymentPostUseCase):
    def __init__(self) -> None:
        super().__init__()
        self.__respository: Repository = PaymentRepository()

    def save(self, payment: Payment) -> Payment:
        Logger.info(method=Logger.getMethodCurrent(), message="Start of use case to save payment")
        self.__validate(payment=payment)        
        payment = PaymentMapper.parseToDomain(self.__respository.save(PaymentMapper.parseToModel(payment)))
        self.__sendToGatewayPayment(payment=payment)
        return payment
    
    def savePayments(self, payments: List[Payment]) -> List[Payment]:
        Logger.info(method=Logger.getMethodCurrent(), message="Start of use case to save list payments")                
        self.__validatePayments(payments=payments)
        paymentsSaved = [self.save(payment) for payment in payments]
        return paymentsSaved

    def __validatePayments(self, payments: List[Payment]):
        Logger.info(method=Logger.getMethodCurrent(), message="Start validate to payments")
        totalPaid : float = sum(p.amountPaid for p in payments)
        if (totalPaid <= 0.00):
            raise BusinessException(status_code=400,
                    detail=f"Invalid amount paid to order")
            
    def __validate(self, payment: Payment) -> Payment:
        Logger.info(method=Logger.getMethodCurrent(), message="Start validate to payment")                
        return payment
    
    def __sendToGatewayPayment(self, payment: Payment):
        if (payment.type != TypePayment.MONEY):
            return True    

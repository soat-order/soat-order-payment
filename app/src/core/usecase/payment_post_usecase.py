from typing import List
from src.core.domain.order import Order
from src.core.domain.payment import Payment
from src.core.domain.enum.type_payment_enum import TypePayment
from src.port.usecase.payment_post_usecase import PaymentPostUseCase
from src.port.usecase.order_get_usecase import OrderGetUseCase
from src.port.spi.client.gateway_payment_port import GatewayPaymentPort
from src.port.spi.persistence.repository.repository import Repository
from src.core.usecase.order_get_usecase import OrderGetUseCaseImpl
from src.core.exception.business_exception import BusinessException
from src.adapter.spi.client.paybill.paybill_client import PayBillClient
from src.adapter.spi.persistence.repository.payment_repository import PaymentRepository
from src.adapter.spi.persistence.mapper.payment_mapper import PaymentMapper
from src.core.util.logger_custom import Logger


class PaymentPostUseCaseImpl(PaymentPostUseCase):
    def __init__(self) -> None:
        super().__init__()
        self.__respository: Repository = PaymentRepository()
        self.__gatewayPayment: GatewayPaymentPort = PayBillClient()
        self.__getOrderUseCase: OrderGetUseCase = OrderGetUseCaseImpl()
        self.__order : Order = None

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
        self.__getOrderById(orderId=payments[0].orderId)
        totalPaid : float = sum(p.amountPaid for p in payments)
        if (totalPaid != self.__order.total):
            raise BusinessException(status_code=400,
                    detail=f"Invalid amount paid to order id: {self.__order.id}")
            
    def __validate(self, payment: Payment) -> Payment:
        Logger.info(method=Logger.getMethodCurrent(), message="Start validate to payment")                
        self.__getOrderById(orderId=payment.orderId)
        return payment
    
    def __getOrderById(self, orderId: str) -> Order:
        if (self.__order is None):
            self.__order = self.__getOrderUseCase.getById(id=orderId)
        return self.__order

    def __sendToGatewayPayment(self, payment: Payment):
        if (payment.type != TypePayment.MONEY):
            self.__gatewayPayment.paid(payment.id)

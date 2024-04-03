from typing import List
from datetime import datetime
from src.core.domain.payment import Payment
from src.core.domain.enum.type_payment_enum import TypePayment
from src.port.usecase.payment_post_usecase import PaymentPostUseCase
from src.port.spi.persistence.repository.repository import Repository
from src.port.spi.sqs.sqs_payment_producer import PaymentProducer
from src.core.exception.business_exception import BusinessException
from src.adapter.spi.persistence.repository.payment_repository import PaymentRepository
from src.adapter.spi.persistence.mapper.payment_mapper import PaymentMapper
from src.adapter.spi.sqs.sqs_payment_producer import PaymentProducerImpl
from src.core.util.logger_custom import Logger


class PaymentPostUseCaseImpl(PaymentPostUseCase):
    def __init__(self) -> None:
        # super().__init__()
        self.__respository: Repository = PaymentRepository()
        self.__sqsPayment : PaymentProducer = PaymentProducerImpl()

    def save(self, payment: Payment) -> Payment:
        Logger.info(method=Logger.getMethodCurrent(), message="Start of use case to save payment")
        payment = self.__validate(payment=payment)        
        payment = PaymentMapper.parseToDomain(self.__respository.save(PaymentMapper.parseToModel(payment)))
        self.__sendToGatewayPayment(payment=payment)
        return payment
    
    def savePayments(self, payments: List[Payment]) -> List[Payment]:
        try:
            Logger.info(method=Logger.getMethodCurrent(), message="Start of use case to save list payments")                
            self.__validatePayments(payments=payments)
            paymentsSaved = [self.save(payment) for payment in payments]
            self.__sqsPayment.sendMessagePayment(PaymentMapper.parseToSchema(paymentsSaved))
            return paymentsSaved
        except BusinessException as ex:
            raise ex
        except Exception as ex:
            Logger.error(method=Logger.getClassMethodCurrent(), message=f"Error occurred to save exception: {str(ex)}")
            raise BusinessException(status_code=500,
                    detail=f"Error occurred to save")
    
    def __validatePayments(self, payments: List[Payment]):
        Logger.info(method=Logger.getMethodCurrent(), message="Start validate to payments")
        totalPaid : float = sum(p.amountPaid for p in payments)
        if (totalPaid <= 0.00):
            raise BusinessException(status_code=400,
                    detail=f"Invalid amount paid to order")
            
    def __validate(self, payment: Payment) -> Payment:
        Logger.info(method=Logger.getMethodCurrent(), message="Start validate to payment")                
        if (payment.type == TypePayment.MONEY):
            payment.dateTimePaid = datetime.now()
        else:
            payment.dateTimePaid = datetime.now()
        return payment
    
    def __sendToGatewayPayment(self, payment: Payment):
        if (payment.type == TypePayment.MONEY):
            return True
        else:
            # TODO implementation future para enviar wiremock GatewayPayBill
            return True

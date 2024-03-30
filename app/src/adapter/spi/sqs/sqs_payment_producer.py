from typing import List
from src.core.domain.enum.type_payment_status_enum import TypePaymentStatus
from src.port.spi.sqs.sqs_payment_producer import PaymentProducer
from src.adapter.spi.sqs.schema.payment_order import PaymentOrder
from src.core.util.logger_custom import Logger
from src.adapter.spi.sqs.sqs_producer import SqsProducer


class PaymentProducerImpl(PaymentProducer[PaymentOrder]):
    def __init__(self) -> None:
        Logger.info(method=Logger.getMethodCurrent(), message="Start config to SQS payment producer")
        self.__sqsProducer = SqsProducer()
    
    
    def sendMessagePayment(self, paymentOrder: PaymentOrder):
        if (paymentOrder.status == TypePaymentStatus.RECEIVED):
            self._sendMessagePaymentReceived(paymentOrder=paymentOrder)
        else:
            self._sendMessagePaymentError(paymentOrder=paymentOrder)    

    def _sendMessagePaymentReceived(self, paymentOrder: PaymentOrder):
        return self.__sqsProducer.send_message(queue_name="sqs-payment-received", payload=paymentOrder)

    def _sendMessagePaymentError(self, paymentOrder: PaymentOrder):
        return self.__sqsProducer.send_message(queue_name="sqs-payment-error", payload=paymentOrder)
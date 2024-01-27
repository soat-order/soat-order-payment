from typing import List
from src.core.domain.payment import Payment
from src.adapter.spi.api.schema.base_response import BaseResponse
from src.adapter.spi.api.schema.payment_request import PaymentRequest
from src.adapter.spi.api.schema.payment_response import PaymentResponse


class PaymentMapper:
    """
    Nao existe o PaymentMapper.parseToDomain(request) devido o pagamento sempre vai ser um array do ID do pedido
    {orderId: 999, payments:[...]}
    """

    @staticmethod
    def parseToDomainList(request: PaymentRequest) -> List[Payment]:
        return [
            Payment(
                orderId = request.orderId,
                type = payment.type,
                amountPaid = payment.amountPaid
            )
            for payment in request.payments
        ]

    @staticmethod
    def parseToResponse(domain: Payment) -> BaseResponse[PaymentResponse]:
        return BaseResponse(
            data = PaymentResponse(
                id = domain.id,
                orderId = domain.orderId,
                type = domain.type.name,
                amount = domain.amountPaid,
                amountPaid = 0.00 if domain.dateTimePaid is None else domain.amountPaid
            )
        )    
    
    @staticmethod
    def parseToResponseList(domainList: List[Payment]) -> BaseResponse[PaymentResponse]:
        return BaseResponse(
            data=[PaymentMapper.parseToResponse(domain).data for domain in domainList]
        ) if domainList is not None else None

from typing import List, Any
from src.adapter.spi.persistence.model.payment import Payment as PaymentModel
from src.adapter.spi.sqs.schema.payment_order import PaymentOrder as PaymentOrderSchema
from src.core.domain.payment import Payment
from src.core.domain.enum.type_payment_enum import TypePayment
from src.core.domain.enum.type_payment_status_enum import TypePaymentStatus


class PaymentMapper:
    @staticmethod
    def parseToModel(domain: Payment) -> PaymentModel:
        print(domain)
        paymentModel = PaymentModel(
            orderId=domain.orderId,
            type = domain.type,
            amountPaid = domain.amountPaid
        )
        if (domain.id != None):
            paymentModel.id = domain.id
        if (domain.dateTimePaid != None):    
            paymentModel.dateTimePaid = domain.dateTimePaid
        return paymentModel
    
    @staticmethod
    def parseToModelList(domainList: List[Payment]) -> List[PaymentModel]:
        return [PaymentMapper.parseToModel(domain) for domain in domainList]

    @staticmethod
    def parseToDomain(model: PaymentModel) -> Payment:
        payment = Payment(
            orderId = model.orderId,
            type = TypePayment.valueOf(model.type),
            amountPaid = model.amountPaid
        )
        payment.id = model.id
        payment.dateTimePaid = model.dateTimePaid
        return payment

    @staticmethod
    def parseToDomainList(modelList: List[Payment]) -> List[PaymentModel]:
        return [PaymentMapper.parseToDomain(model) for model in modelList]

    @staticmethod
    def parseDictToModel(dictModel) -> Any:
        # devido ao findAll retornar um CURSOR neste caso precisa chamar o metodo parseDictToModelList
        if (not isinstance(dictModel, dict)):
            return PaymentMapper.parseDictToModelList(dictModel)
        paymentModel = PaymentModel(
            orderId = dictModel['orderId'],
            type = dictModel['type'],
            amountPaid = dictModel['amountPaid']
        )
        paymentModel.id = dictModel['_id']
        paymentModel.dateTimePaid = dictModel['dateTimePaid']
        return paymentModel

    @staticmethod
    def parseDictToModelList(dictList: List[dict]) -> List[PaymentModel]:
        return list(PaymentMapper.parseDictToModel(dict) for dict in dictList)

    @staticmethod
    def parseToSchema(domainList: List[Payment]) -> PaymentOrderSchema:
        payReceived = next(filter(lambda p: (p.type != TypePayment.MONEY and p.amountPaid <= 10.00), domainList), None)
        totalPaid : float = sum(p.amountPaid for p in domainList)
        paymentOrderSchema = PaymentOrderSchema(
            orderId=domainList[0].orderId,
            amountPaid=totalPaid,
            dateTimePaid=domainList[0].dateTimePaid
        )
        paymentOrderSchema.status = TypePaymentStatus.RECEIVED if (payReceived == None) else TypePaymentStatus.CANCELED
        return paymentOrderSchema

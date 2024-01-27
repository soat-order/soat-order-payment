from typing import List, Any
from src.adapter.spi.persistence.model.payment import Payment as PaymentModel
from src.core.domain.payment import Payment
from src.core.domain.enum.type_payment_enum import TypePayment


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

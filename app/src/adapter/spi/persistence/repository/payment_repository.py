from typing import List
from src.core.util.logger_custom import Logger
from src.core.exception.business_exception import BusinessException
from src.adapter.spi.persistence.model.payment import Payment
from src.adapter.spi.persistence.repository.repository_default import RepositoryDefault
from src.adapter.spi.persistence.mapper.payment_mapper import PaymentMapper


class PaymentRepository(RepositoryDefault[Payment, str]):
    def __init__(self) -> None:
        super().__init__(Payment)

    def findByOrderId(self, orderId: str) -> List[Payment]:
        try:
            Logger.info(Logger.getClassMethodCurrent(), f"Start search by code: {orderId}")  
            return super().findByFilter(filter={'orderId': orderId})
        except Exception as ex:
            raise BusinessException(status_code=404,
                            detail=f"Not found payment by code :{orderId}")

    def updatePaid(self, payment: Payment) -> Payment:
        try:
            filter = { '_id': f"{payment.id}" }
            updateDateTimePaid: dict = {"$set": {'dateTimePaid': f"{payment.dateTimePaid}"}}
            return self._getSession().update_one(filter, updateDateTimePaid)
        except Exception as ex:
            raise ex

    def parseToModel(self, dict: dict) -> Payment:
        return PaymentMapper.parseDictToModel(dict)

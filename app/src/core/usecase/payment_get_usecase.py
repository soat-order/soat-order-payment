from typing import List
from src.core.domain.payment import Payment
from src.port.usecase.payment_get_usecase import PaymentGetUseCase
from src.port.spi.persistence.repository.repository import Repository
from src.adapter.spi.persistence.repository.payment_repository import PaymentRepository
from src.adapter.spi.persistence.mapper.payment_mapper import PaymentMapper
from src.core.util.logger_custom import Logger


class PaymentGetUseCaseImpl(PaymentGetUseCase):
    def __init__(self) -> None:
        super().__init__()
        self.__respository: Repository = PaymentRepository()

    def getById(self, id: str) -> Payment:
        Logger.info(method=Logger.getMethodCurrent(), message=f"Start of use case to search id: {id}")
        return PaymentMapper.parseToDomain(self.__respository.findById(id))

    def getByOrderId(self, orderId: str) -> List[Payment]:
        Logger.info(method=Logger.getMethodCurrent(), message=f"Start of use case to search id: {orderId}")
        return PaymentMapper.parseToDomainList(self.__respository.findByOrderId(orderId))
    
    def getByIdAndDateTimePaid(self, id: str) -> Payment:
        Logger.info(method=Logger.getMethodCurrent(), message=f"Start of use case to search id: {id} and dateTimePaid is None")
        return PaymentMapper.parseToDomain(self.__respository.findByFilterOne(filter={"_id": id, "dateTimePaid": None}))

    
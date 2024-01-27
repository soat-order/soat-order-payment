from datetime import timedelta
from src.core.domain.payment import Payment
from src.port.usecase.payment_paid_usecase import PaymentPaidUseCase
from src.port.usecase.payment_get_usecase import PaymentGetUseCase
from src.port.spi.persistence.repository.repository import Repository
from src.core.usecase.payment_get_usecase import PaymentGetUseCaseImpl
from src.adapter.spi.persistence.repository.payment_repository import PaymentRepository
from src.adapter.spi.persistence.mapper.payment_mapper import PaymentMapper
from src.core.util.datetime_util import DateTimeUtil
from src.core.util.logger_custom import Logger


class PaymentPaidUseCaseImpl(PaymentPaidUseCase):
    def __init__(self) -> None:
        super().__init__()
        self.__respository: Repository = PaymentRepository()
        self.__paymentGetUseCase : PaymentGetUseCase = PaymentGetUseCaseImpl()        
        
    def execute(self, id: str, mseconds: int) -> Payment:
        Logger.info(method=Logger.getMethodCurrent(), message=f"Start of use case for paid id {id}")
        payment: Payment = self.__paymentGetUseCase.getByIdAndDateTimePaid(id=id)
        if (payment is not None):
            payment.dateTimePaid = DateTimeUtil.parseToDateTime(mseconds=mseconds, tz=DateTimeUtil.getTimeZoneSaoPaulo())
            self.__respository.updatePaid(payment=PaymentMapper.parseToModel(payment))
        return payment

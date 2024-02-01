from unittest import TestCase
from unittest.mock import patch
from src.core.usecase.payment_paid_usecase import PaymentPaidUseCaseImpl
from src.core.domain.enum.type_payment_enum import TypePayment
from src.core.domain.payment import Payment
from src.adapter.spi.persistence.model.payment import Payment as PaymentModel
from src.adapter.spi.persistence.repository.payment_repository import PaymentRepository
from src.core.usecase.payment_get_usecase import PaymentGetUseCaseImpl
from src.core.exception.business_exception import BusinessException

class PaymentPutUseCase(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.useCase : PaymentPaidUseCaseImpl = PaymentPaidUseCaseImpl()
        self.paymentMock: Payment = Payment("1", TypePayment.DEBIT_CARD, 10.0)
        self.paymentModelMock: PaymentModel = PaymentModel("1", TypePayment.DEBIT_CARD, 10.0)

    @patch.object(PaymentRepository, 'updatePaid')
    @patch.object(PaymentGetUseCaseImpl, 'getByIdAndDateTimePaid')
    def test_execute_ok(self, mock_repository_updatePaid, mock_usecase_getByIdAndDateTimePaid):
        mock_repository_updatePaid.return_value = self.paymentMock
        mock_usecase_getByIdAndDateTimePaid.return_value = self.paymentMock
        result = self.useCase.execute("1", 10)
        self.assertIsNotNone(result)
        self.assertEqual(type(result), Payment)
        self.assertEqual(result.orderId, "1")

    # @patch("src.core.usecase.payment_paid_usecase.PaymentPaidUseCaseImpl")
    # def test_execute_exception(self, mock_usecase):
    #     mock_usecase.__paymentGetUseCase.getByIdAndDateTimePaid.return_value = self.paymentMock
    #     with self.assertRaises(BusinessException) as context:
    #         self.useCase.execute(self.paymentMock.orderId, 10)        
    #     self.assertEqual(type(context.exception), BusinessException)        

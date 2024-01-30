from unittest import TestCase
from unittest.mock import patch
from src.core.usecase.payment_paid_usecase import PaymentPaidUseCaseImpl
from src.core.domain.enum.type_payment_enum import TypePayment
from src.core.domain.payment import Payment
from src.core.exception.business_exception import BusinessException

class PaymentPostUseCase(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.useCase : PaymentPaidUseCaseImpl = PaymentPaidUseCaseImpl()
        self.paymentMock: Payment = Payment("1", TypePayment.DEBIT_CARD, 10.0)

    @patch("src.core.usecase.payment_paid_usecase.PaymentPaidUseCaseImpl")
    def test_execute_exception(self, mock_usecase):
        mock_usecase.__paymentGetUseCase.getByIdAndDateTimePaid.return_value = self.paymentMock
        with self.assertRaises(BusinessException) as context:
            self.useCase.execute(self.paymentMock.orderId, 10)        
        self.assertEqual(type(context.exception), BusinessException)        

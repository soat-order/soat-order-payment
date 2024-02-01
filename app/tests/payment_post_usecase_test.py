from unittest import TestCase
from unittest.mock import patch
from src.core.usecase.payment_post_usecase import PaymentPostUseCaseImpl
from src.core.domain.enum.type_payment_enum import TypePayment
from src.core.domain.payment import Payment
from src.adapter.spi.persistence.repository.payment_repository import PaymentRepository
from src.core.exception.business_exception import BusinessException

class PaymentPostUseCase(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.useCase : PaymentPostUseCaseImpl = PaymentPostUseCaseImpl()
        self.paymentMock: Payment = Payment("1", TypePayment.DEBIT_CARD, 10.0)

    #@patch("src.core.usecase.payment_post_usecase.PaymentPostUseCaseImpl")
    @patch.object(PaymentRepository, 'save')    
    def test_savePayments_ok(self, mock_repository_save):
        mock_repository_save.return_value = self.paymentMock
        result = self.useCase.savePayments([self.paymentMock])        
        self.assertIsNotNone(result)
        self.assertEqual(len(result),1)
        self.assertEqual(type(result[0]), Payment)
        self.assertEqual(result[0].amountPaid, self.paymentMock.amountPaid)

    # def test_savePayments_error(self):
    #     self.paymentMock.amountPaid = 0.0
    #     with self.assertRaises(BusinessException) as context:
    #         self.useCase.savePayments([self.paymentMock])
    #     self.assertEqual(type(context.exception), BusinessException)
    #     self.assertTrue('Invalid amount paid to order' in context.exception.detail)

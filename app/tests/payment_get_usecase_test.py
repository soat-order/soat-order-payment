from unittest import TestCase
from unittest.mock import patch
from src.core.usecase.payment_get_usecase import PaymentGetUseCaseImpl
from src.core.domain.enum.type_payment_enum import TypePayment
from src.core.domain.payment import Payment
from src.adapter.spi.persistence.model.payment import Payment as PaymentModel
from src.adapter.spi.persistence.repository.payment_repository import PaymentRepository
from src.adapter.spi.persistence.repository.repository_default import RepositoryDefault
from src.core.exception.business_exception import BusinessException



class PaymentPostUseCase(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.useCase : PaymentGetUseCaseImpl = PaymentGetUseCaseImpl()
        self.paymentModelMock: PaymentModel = PaymentModel("1", TypePayment.DEBIT_CARD, 10.0)
        self.paymentMock: Payment = Payment("1", TypePayment.DEBIT_CARD, 10.0)

    @patch.object(PaymentRepository, 'findById')
    def test_getById_ok(self, mock_repository_findById):
        mock_repository_findById.return_value = self.paymentModelMock
        result = self.useCase.getById("1")
        self.assertIsNotNone(result)
        self.assertEqual(type(result), Payment)
        self.assertEqual(result.orderId, "1")

    def test_getById_error(self):
        id : str = self.paymentMock.id
        with self.assertRaises(BusinessException) as context:            
            self.useCase.getById(id)
        self.assertEqual(type(context.exception), BusinessException)
        self.assertTrue('Not found Payment by id:' in context.exception.detail)

    @patch.object(PaymentRepository, 'findByOrderId')
    def test_getByOrderId_ok(self, mock_repository_findByOrderId):
        mock_repository_findByOrderId.return_value = [self.paymentModelMock]
        result = self.useCase.getByOrderId("1")
        self.assertIsNotNone(result)
        self.assertEqual(type(result), list)
        self.assertEqual(result[0].orderId, "1")

    # @patch.object(PaymentRepository, 'findByOrderId')
    # def test_getById_error(self, mock_repository_findByOrderId):
    #     mock_repository_findByOrderId.return_value = BusinessException(status_code=404, detail="Not Found")
    #     with self.assertRaises(BusinessException) as context:            
    #         self.useCase.getByOrderId(None)
    #     self.assertEqual(type(context.exception), BusinessException)
        # self.assertTrue('Not found Payment by id:' in context.exception.detail)

    @patch.object(PaymentRepository, 'findByFilterOne')
    def test_getByIdAndDateTimePaid_ok(self, mock_repository_findByFilterOne):
        mock_repository_findByFilterOne.return_value = self.paymentModelMock
        result = self.useCase.getByIdAndDateTimePaid("1")
        self.assertIsNotNone(result)
        self.assertEqual(type(result), Payment)
        self.assertEqual(result.orderId, "1")

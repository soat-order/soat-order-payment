from unittest import TestCase
from unittest.mock import patch
from src.core.usecase.payment_get_usecase import PaymentGetUseCaseImpl
from src.core.domain.enum.type_payment_enum import TypePayment
from src.core.domain.payment import Payment
from src.core.exception.business_exception import BusinessException
from src.adapter.spi.persistence.model.payment import Payment as PaymentModel


class PaymentPostUseCase(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.useCase : PaymentGetUseCaseImpl = PaymentGetUseCaseImpl()
        self.paymentModelMock: PaymentModel = PaymentModel("1", TypePayment.DEBIT_CARD, 10.0)
        self.paymentMock: Payment = Payment("1", TypePayment.DEBIT_CARD, 10.0)

    # @patch("src.core.usecase.payment_post_usecase.PaymentPostUseCaseImpl")
    # @patch("src.adapter.spi.persistence.repository.repository_default.RepositoryDefault")
    # @patch("src.adapter.spi.persistence.database.database_mongodb.Database")
    # def test_getById_ok(self, mock_repository):
    #     mock_repository.findById.return_value = {
    #         '_id': '1',
    #         'orderId': '1',
    #         'type': 'DEBIT_CARD',
    #         'amountPaid': 10.0 
    #     }
    #     # mock_usecase.__repository.findById.return_value = self.paymentModelMock

    #     id : str = self.paymentMock.id
    #     result = self.useCase.getById("1")
    #     self.assertIsNotNone(result)
    #     # self.assertEqual(type(result), Payment)
    #     # self.assertEqual(id, self.paymentMock.orderId)

    # @patch("src.core.usecase.payment_post_usecase.PaymentPostUseCaseImpl")
    # @patch("src.adapter.spi.persistence.repository.payment_repository.PaymentRepository")
    # @patch("src.adapter.spi.persistence.repository.repository_default.RepositoryDefault")
    # def test_getByIdAndDateTimePaid_ok(self, mock_usecase, mock_repositor, mock_repo_default):
    #     mock_repo_default.db.findById.return_value = {
    #         '_id': '1',
    #         'orderId': '1',
    #         'type': 'DEBIT_CARD',
    #         'amountPaid': 10.0 
    #     }
    #     mock_usecase.findByFilterOne.return_value = self.paymentModelMock

    #     id : str = self.paymentMock.id
    #     result = self.useCase.getByIdAndDateTimePaid("1")
    #     self.assertIsNotNone(result)
        # self.assertEqual(type(result), Payment)
        # self.assertEqual(id, self.paymentMock.orderId)

    def test_savePayments_error(self):
        id : str = self.paymentMock.id
        with self.assertRaises(BusinessException) as context:            
            self.useCase.getById(id)

        self.assertEqual(type(context.exception), BusinessException)
        self.assertTrue('Not found Payment by id:' in context.exception.detail)

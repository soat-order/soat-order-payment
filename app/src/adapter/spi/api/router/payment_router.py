from fastapi import APIRouter, status, Path
from datetime import datetime
from src.port.usecase.payment_post_usecase import PaymentPostUseCase
from src.port.usecase.payment_paid_usecase import PaymentPaidUseCase
from src.port.usecase.payment_get_usecase import PaymentGetUseCase
from src.core.usecase.payment_post_usecase import PaymentPostUseCaseImpl
from src.core.usecase.payment_paid_usecase import PaymentPaidUseCaseImpl
from src.core.usecase.payment_get_usecase import PaymentGetUseCaseImpl
from src.adapter.spi.api.validator.validator import Validator
from src.adapter.spi.api.mapper.payment_mapper import PaymentMapper
from src.adapter.spi.api.schema.payment_request import PaymentRequest


router = APIRouter()
__paymentPostUseCase: PaymentPostUseCase = PaymentPostUseCaseImpl()
__paymentPaidUseCase: PaymentPaidUseCase = PaymentPaidUseCaseImpl()
__paymentGetUseCase: PaymentGetUseCase = PaymentGetUseCaseImpl()


validator: Validator = Validator()

@router.post(path='/', status_code=status.HTTP_201_CREATED)
async def save(payment: PaymentRequest):
    __paymentPostUseCase.savePayments(PaymentMapper.parseToDomainList(payment))    

@router.put(path='/{id}/paid', status_code=status.HTTP_204_NO_CONTENT)
async def paid(id: str):
   mseconds: int = int(datetime.now().timestamp() * 1000)
   __paymentPaidUseCase.execute(id=id, mseconds=mseconds)

    
@router.get(path='/{id}', status_code=status.HTTP_200_OK)
async def getById(id: str):
    return PaymentMapper.parseToResponse(__paymentGetUseCase.getById(id))

@router.get(path='/order/{orderId}', status_code=status.HTTP_200_OK)
async def getByOrderId(orderId: str):
    return PaymentMapper.parseToResponseList(__paymentGetUseCase.getByOrderId(orderId))

from typing import Generic, TypeVar
from dataclasses import dataclass

# tipagem para model
T = TypeVar("T")


@dataclass
class BaseResponse(Generic[T]):
    data: T


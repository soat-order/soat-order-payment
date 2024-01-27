from typing import Any, List, TypeVar
from abc import ABC, abstractmethod
from src.port.spi.persistence.repository.repository import Repository
from src.adapter.spi.persistence.model.customer import Customer
# from src.adapter.spi.persistence.database.database import getSession
from src.port.spi.persistence.database.database_port import DatabasePort
from src.adapter.spi.persistence.database.database_mongodb import Database
from src.core.util.logger_custom import Logger
from src.core.exception.business_exception import BusinessException

# tipagem para model
T = TypeVar("T")

# tipagem para primary key
K = TypeVar("K")

customerList : List[Customer] = [Customer(name='Joao', documentNumber='000.000.000-00', email='joao@email.com', phoneNumber='019987654321'),
                                 Customer(name='Vitor', documentNumber='999.999.999-99', email='vitor@email.com', phoneNumber='019987654321')]

# db: DatabasePort = Database[T,K]


class RepositoryDefault(Repository[T,K],ABC):
    def __init__(self, modelType: T = None) -> None:
        self.db = Database(modelType=modelType)
        self.modelType : T = modelType
        
    def save(self, entity: T) -> T:        
        try:
            Logger.info(Logger.getClassMethodCurrent(), f"Start to save {type(entity)}")
            # db: DatabasePort = Database()
            self.db.insert(entity)
            # self._getSession().begin
            # self._getSession().add(entity)
            # self._getSession().commit()
            Logger.info(Logger.getClassMethodCurrent(), f"Done to save {entity.__class__}")
            return entity
        except Exception as ex:
            raise ex
    
    def update(self, entity: T) -> T:        
        try:
            Logger.info(Logger.getClassMethodCurrent(), f"Start to update {type(entity)}")
            updated = self.db.update(entity)
            Logger.info(Logger.getClassMethodCurrent(), f"Done to update {entity.__class__}")
            return entity
        except Exception as ex:
            raise ex

    def delete(self, entity: T) -> bool:
        try:
            Logger.info(Logger.getClassMethodCurrent(), f"Start to delete {type(entity)}", data=entity)
            print(f'Delete data with success: {type(entity)}')
            # return self.getSession().delete(entity)            
            return True
        except Exception as ex:
            raise ex
    
    def findById(self, id: K) -> Any:
        try:
            Logger.info(Logger.getClassMethodCurrent(), f"Start search by id: {id}")
            return self.parseToModel(self.db.findById(id, self.modelType))
        except Exception as ex:
            raise BusinessException(status_code=404,
                    detail=f"Not found {self.modelType.__name__} by id: {id}")
            # Logger.error(Logger.getClassMethodCurrent(), f"Exception erro: {str(ex)}")        
            print(ex)

    
    def findByAll(self) -> List[T]:
        Logger.info(Logger.getClassMethodCurrent(), f"Start search all by {self.modelType}")        
        return self.parseToModel(self.db.findByAll(modelType=self.modelType))

    def findByFilter(self, filter: Any) -> List[T]:
        try:
            Logger.info(Logger.getClassMethodCurrent(), f"Start search {self.modelType.__name__} by filter: {filter}")        
            return self.parseToModel(self.db.findByFilter(self.modelType, filter=filter))
        except Exception as ex:
            raise BusinessException(status_code=404,
                            detail=f"Not found product by filter: {filter}")

    def findByFilterOne(self, filter: Any) -> T:
        try:
            Logger.info(Logger.getClassMethodCurrent(), f"Start search {self.modelType} by filter one: {filter}")            
            return self.parseToModel(self.db.findByFilterOne(filter=filter))
        except Exception as ex:
            raise BusinessException(status_code=404,
                            detail=f"Not found product by filter: {filter}")

    @abstractmethod
    def parseToModel(self, dict: dict) -> T:
        raise NotImplementedError

    def _getSession(self):
        self.db._getModelType(self.modelType)
        return self.db._getSession()
    
    def getDB(self):
        return self.db
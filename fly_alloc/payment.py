from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
import uuid

class PaymentStatus(Enum):
    PENDING = "Pendente"
    COMPLETED = "Concluído"
    FAILED = "Falhou"
    REFUNDED = "Reembolsado"
class PaymentMethod(ABC):

    @abstractmethod
    def process_payment(self, amount: float) -> str:
        ...
        
    @abstractmethod         
    def history(self) -> str:
        ...

class CashPayment(PaymentMethod):
    ...

class Payment:
    def __init__(self, id: str, amount: float, method: PaymentMethod):
        self._id = uuid.uuid4()
        self._amount = amount
        self._method = method
        self._status = PaymentStatus.PENDING
        self._timestamp = datetime.now()
        self._history = [
            (self._status.value, self._timestamp.strftime("%Y-%m-%d %H:%M:%S"))
        ]

    @property
    def id(self):
        return self._id

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value):
        self._method = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value

    @property
    def history(self):
        return self._history

    @history.setter
    def history(self, value):
        self._history = value
        
    def pay(self):
        """Processa o pagamento e atualiza o status"""
        try:
            self._method.process_payment(self._amount)
            self._status = PaymentStatus.COMPLETED
        except Exception as e:
            self._status = PaymentStatus.FAILED
            raise e
        finally:
            self._history.append((self._status.value, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

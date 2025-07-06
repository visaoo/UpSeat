

from abc import ABC, abstractmethod
from enum import Enum   

class PaymentStatus(Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"
    FAILED = "Failed"
    REFUNDED = "Refunded"   


class PaymentMethod(ABC):

    @abstractmethod
    def process_payment(self, amount: float) -> str:
        ...
        
    @abstractmethod         
    def history(self) -> str:
        ...
        
    def status(self) -> PaymentStatus:
        ...
    
from abc import ABC, abstractmethod

class IOrderObserver(ABC):
    @abstractmethod
    def on_order_created(self, order):
        pass
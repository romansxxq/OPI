from abc import ABC, abstractmethod

class IPriceStrategy(ABC):
    @abstractmethod
    def calculate_price(self, price):
        pass
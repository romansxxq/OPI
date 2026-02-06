from observers.observer import IOrderObserver

class OrderService:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer: IOrderObserver):
        self._observers.append(observer)

    def create_order(self, order):
        print(f"OrderService: створюємо замовлення {order['id']}")
        for observer in self._observers:
            observer.on_order_created(order)

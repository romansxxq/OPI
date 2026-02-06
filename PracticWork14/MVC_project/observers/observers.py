from .observer import IOrderObserver

class LoggerObserver(IOrderObserver):
    def on_order_created(self, order):
        print(f"[LOG] Створено замовлення ID={order['id']} з сумою {order['amount']}")

class StatisticsObserver(IOrderObserver):
    def __init__(self):
        self.total_amount = 0

    def on_order_created(self, order):
        self.total_amount += order['amount']
        print(f"[STATS] Загальна сума всіх замовлень зараз: {self.total_amount}")

from model.service import IService
class BaseOrderService(IService):
    def execute(self):
        print("Обробка замовлення...")
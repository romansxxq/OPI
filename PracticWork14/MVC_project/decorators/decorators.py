import time
from model.service import IService

class ServiceDecorator(IService):
    def __init__(self, service: IService):
        self._service = service

    def execute(self):
        self._service.execute()

class LoggingDecorator(ServiceDecorator):
    def execute(self):
        print("[Logging] Початок виконання сервісу")
        super().execute()
        print("[Logging] Кінець виконання сервісу")

class TimingDecorator(ServiceDecorator):
    def execute(self):
        start = time.time()
        super().execute()
        print(f"[Timing] Час виконання: {time.time() - start:.4f} сек")

class AccessCheckDecorator(ServiceDecorator):
    def __init__(self, service: IService, user_role: str):
        super().__init__(service)
        self.user_role = user_role

    def execute(self):
        if self.user_role != "admin":
            print("[AccessCheck] Доступ заборонено!")
            return
        print("[AccessCheck] Доступ дозволено")
        super().execute()
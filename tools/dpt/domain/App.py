from builders.ConsumerDomain import ConsumerDomain
from builders.ServiceDomain import ServiceDomain

class App:
    def __init__(self, type) -> None:
        self.type = type
        print(self.type)
        self._domain = ServiceDomain() if self.type == "service" else ConsumerDomain()
        print(self._domain)

    def build(self):
        self._domain.build()
        

    def destroy(self):
        self._domain.destroy()


if __name__ == '__main__':
    domain_app = App(type="service")
    domain_app.build()

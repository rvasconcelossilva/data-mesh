from domain.abstract.DomainBuilderInterface import DomainBuilderInterface

class ConsumerDomain(DomainBuilderInterface):

    def __init__(self) -> None:
        super().__init__("consumer")
        
    def build(self) -> None:
        self.apply_database()
        self.apply_schema()

    def destroy(self) -> None:
        self.destroy_database()
        self.destroy_schema()

         
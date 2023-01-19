from domain.abstract.DomainBuilderInterface import DomainBuilderInterface

class ServiceDomain(DomainBuilderInterface):

    def __init__(self) -> None:
        super().__init__("service")
        super().apply_database()
        super().build()


    def destroy(self) -> None:
        self.destroy_database()
        self.destroy_schema()
        self.destroy_storage_integration()

         
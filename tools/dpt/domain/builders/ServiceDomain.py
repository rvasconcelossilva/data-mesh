from domain.abstract.DomainBuilderInterface import DomainBuilderInterface

class ServiceDomain(DomainBuilderInterface):

    def __init__(self) -> None:
        super().__init__()

    def build(self):
        self.apply_database()
        self.apply_schema()
        self.apply_storage_integration()

    def destroy(self) -> None:
        self.destroy_database()
        self.destroy_schema()
        self.destroy_storage_integration()

         
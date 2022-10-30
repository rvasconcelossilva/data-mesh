from abc import ABC, abstractmethod

class DomainBuilderInterface():
    """
    """

    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def destroy(self):
        pass

    def apply_database(self) -> None:
        print("Database has been created/update.")

    def apply_schema(self) -> None:
        print("Schemas have been created/update.") 

    def apply_storage_integration(self) -> None:
        print("Storage Integration has been created/update.")         

    def destroy_database(self) -> None:
        print("Database has been destroyed.")

    def destroy_schema(self) -> None:
        print("Schemas have been destroyed.") 

    def destroy_storage_integration(self) -> None:
        print("Storage Integrations have been destroyed.")                          

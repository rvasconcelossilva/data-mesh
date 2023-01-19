from abc import ABC, abstractmethod
import string
import pulumi
import pulumi_snowflake as snowflake

class DomainBuilderInterface(ABC):
    """
    """

    def __init__(self, domain) -> None: 
        self._domain = domain
        self._workspace = pulumi.automation.LocalWorkspace(work_dir='/Users/rvasconcelos/Documents/rafa_projects/repos/data-warehouse-as-product/tools/dpt/domain/infrastructure')
        self._stack = pulumi.automation.select_stack('dev', project_name="mesh", work_dir=self._workspace.work_dir)
        #self._stack = pulumi.automation.create_stack('dev', project_name="mesh", work_dir=self._workspace.work_dir)
        
    def build(self):
        self._stack.preview()
        self._stack.up()

    @abstractmethod
    def destroy(self):
        pass

    def apply_database(self) -> None:
        print(" Aqui Database has been created/update.")

    def apply_schema(self) -> None:
        print("Aqui Schemas have been created/update.") 

    def apply_storage_integration(self) -> None:
        print("Storage Integration has been created/update.")         

    def destroy_database(self) -> None:
        print("Database has been destroyed.")

    def destroy_schema(self) -> None:
        print("Schemas have been destroyed.") 

    def destroy_storage_integration(self) -> None:
        print("Storage Integrations have been destroyed.")                          

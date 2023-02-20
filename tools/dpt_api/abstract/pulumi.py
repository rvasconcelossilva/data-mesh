from abc import ABC, abstractmethod
from pulumi import CustomResource

class Resource(ABC):

    def __init__(self, resource_name:str): #, opts: Optional[ResourceOptions], args:object):
        self._resource_name = resource_name

    @abstractmethod
    def resource_program() -> CustomResource:
        pass

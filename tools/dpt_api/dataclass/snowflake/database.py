import dataclasses
from dataclasses import dataclass
from typing import Optional, Mapping
from pulumi.resource import ResourceOptions

@dataclass
class DatabaseProperty:
    resource_name: str
    opts: Optional[ResourceOptions] = None
    comment: Optional[str] = None
    data_retention_time_in_days: Optional[int] = None
    from_database: Optional[str] = None
    from_replica: Optional[str] = None
    from_share: Optional[Mapping[str, str]] = None
    is_transient: Optional[bool] = None
    name: Optional[str] = None
    #TODO: Review below paramters
    #replication_configuration: Optional[DatabaseReplicationConfigurationArgs] = None
    #tags: Optional[Sequence[DatabaseTagArgs]] = None

    def load():
        pass

    def asdict(self):
       return dataclasses.asdict(self) 
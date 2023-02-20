import pulumi_snowflake
from dataclass.snowflake.database import DatabaseProperty
from abstract.pulumi import Resource


class Database(Resource):

    def __init__(self, resource_name:str):
        super().__init__(resource_name)


    def resource_program(self):
        database_dict = DatabaseProperty(resource_name=self._resource_name, name='db_domain')
        _database = pulumi_snowflake.Database(**database_dict.asdict())

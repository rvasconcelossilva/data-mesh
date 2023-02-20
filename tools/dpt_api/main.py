from typing import Union, List
from fastapi import FastAPI
import pulumi
import pulumi_snowflake
import pulumi.automation as auto
from dataclass.common.config import EnvironmentVariables
from builder.pulumi.stack import Stack
from builder.snowflake.database import Database
from pulumi import CustomResource
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/database")
def database():
    create()

#def database():
#    _database = pulumi_snowflake.Database(resource_name="domain.dev.database", name='db_domain')

def create():
    env_variables = EnvironmentVariables()

    resources = list()
    resources.append(Database("domain.dev.database"))

    pulumi_stack = Stack(
        stack_name="otm.domain.dev.database",
        project_name="mesh",
        resources = resources
    )
    pulumi_stack.build()
    pulumi_stack.set_config(json.loads(env_variables.to_json()))
    pulumi_stack.up()

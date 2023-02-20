import os
import dataclasses
from dataclasses import dataclass, field
from dataclasses_json import config, dataclass_json
from typing import Optional

@dataclass_json
@dataclass
class EnvironmentVariables:
    _snowflake_username: Optional[str] = field(metadata=config(field_name="snowflake:username")) 
    _snowflake_role: Optional[dict] = field(metadata=config(field_name="snowflake:role")) 
    _snowflake_account: Optional[dict] = field(metadata=config(field_name="snowflake:account"))
    _snowflake_browserAuth: Optional[dict] = field(metadata=config(field_name="snowflake:browserAuth")) #TODO: add an environment variable to .envrc and create the condition to keep default true in case the variable does not exist in the env file
    
    def __init__(self) -> None:
        self._snowflake_username = os.environ.get('SNOWFLAKE_USER')
        self._snowflake_role = os.environ.get('SNOWFLAKE_ROLE')
        self._snowflake_account = os.environ.get('SNOWFLAKE_ACCOUNT')
        self._snowflake_browserAuth = "true"